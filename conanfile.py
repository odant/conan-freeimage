# FreeImage Conan package
# Dmitriy Vetutnev, ODANT 2018-2020
# Arkady Yudintsev, ODANT 2021-2025


from conan import ConanFile, tools
import os, glob, platform


class FreeImageConan(ConanFile):
    name = "freeimage"
    version = "3.19.1+0"
    license = "FreeImage is licensed under the GNU General Public License, version 2.0 (GPLv2) or version 3.0 (GPLv3), and the FreeImage Public License (FIPL)"
    description = "FreeImage is an Open Source library project for developers who would like to support popular graphics image formats like PNG, BMP, JPEG, TIFF and others as needed by today's multimedia applications"
    url = "https://github.com/odant/conan-freeimage"
    settings = "os", "compiler", "build_type", "arch"
    options = {
        "dll_sign": [True, False]
    }
    default_options = {
        "dll_sign": True
    }
    exports_sources = "src/*", "autoselect_win_sdk.patch", "fix_sources_list.patch", "fix_dll_version.patch", "remove_std_binary_function.patch", "fix_gcc14_build.patch"
    no_copy_source = False
    build_policy = "missing"
    python_requires = "windows_signtool/[>=1.2]@odant/stable"

    def configure(self):
        # DLL sign
        if self.settings.os != "Windows":
            self.options.rm_safe("dll_sign")

    def source(self):
        tools.files.patch(self, patch_file="autoselect_win_sdk.patch")
        if platform.system() == "Windows":
            tools.files.patch(self, patch_file="fix_dll_version.patch")
            tools.files.patch(self, patch_file="remove_std_binary_function.patch")
        else:
            tools.files.patch(self, patch_file="fix_sources_list.patch")
            
    def generate(self):
        benv = tools.env.VirtualBuildEnv(self)
        benv.generate()
        renv = tools.env.VirtualRunEnv(self)
        renv.generate()
        if tools.microsoft.is_msvc(self):
            mstc = tools.microsoft.MSBuildToolchain(self)
            mstc.generate()
            
    def build(self):
        if self.settings.compiler == "gcc": 
            tools.files.patch(self, patch_file="fix_gcc14_build.patch")
        if tools.microsoft.is_msvc(self):
            self.msvc_build()
        else:
            self.unix_build()

    def msvc_build(self):
        with tools.files.chdir(self, "src"):
            projectFile = "FreeImage.2017.vcxproj"
            self.run(f"devenv {projectFile} /upgrade")
            builder = tools.microsoft.MSBuild(self)
            # use Release instead of the RelWithDebInfo
            builder.build_type = "Release" if self.settings.build_type == "RelWithDebInfo" else builder.build_type
            #builder.build_env.cxx_flags = ["/std=c++14"]
            builder.build(projectFile)

    def unix_build(self):
        env = tools.env.Environment()
        env.define("CFLAGS", "-fPIC -fexceptions -fvisibility=hidden")
        env.define("CXXFLAGS", "-fPIC -fexceptions -fvisibility=hidden -Wno-ctor-dtor-privacy -std=c++14")
        if self.settings.build_type == "Debug":
            env.append("CFLAGS", "-Og -g -ggdb")
            env.append("CXXFLAGS", "-Og -g -ggdb")
        else:
            env.append("CFLAGS", "-O3 -DNDEBUG")
            env.append("CXXFLAGS", "-O3 -DNDEBUG")
        if self.settings.arch == "x86_64":
            env.append("CFLAGS", "-m64")
            env.append("CXXFLAGS", "-m64")
            env.define("LDFLAGS", "-m64")
        elif self.settings.arch == "x86":
            env.append("CFLAGS", "-m32")
            env.append("CXXFLAGS", "-m32")
            env.define("LDFLAGS", "-m32")
        #
        with tools.files.chdir(self, "src"), env.vars(self).apply():
            self.run("make -j %s" % tools.build.build_jobs(self))

    def package(self):
        tools.files.copy(self, "FreeImage.h", dst=os.path.join(self.package_folder, "include"), src=os.path.join(self.source_folder, "src", "Source"), keep_path=False)
        # MSVC
        if self.settings.os == "Windows":
            for releasePath in [ "src/x64/Release", "src/Win32/Release" ]:
                tools.files.copy(self, "FreeImage.lib", dst=os.path.join(self.package_folder, "lib"), src=os.path.join(self.source_folder, releasePath), keep_path=False)
                tools.files.copy(self, "FreeImage.dll", dst=os.path.join(self.package_folder, "bin"), src=os.path.join(self.source_folder, releasePath), keep_path=False)
                tools.files.copy(self, "FreeImage.pdb", dst=os.path.join(self.package_folder, "bin"), src=os.path.join(self.source_folder, releasePath), keep_path=False)
            for debugPath in [ "src/x64/Debug", "src/Win32/Debug" ]:
                tools.files.copy(self, "FreeImaged.lib", dst=os.path.join(self.package_folder, "lib"), src=os.path.join(self.source_folder, debugPath), keep_path=False)
                tools.files.copy(self, "FreeImaged.dll", dst=os.path.join(self.package_folder, "bin"), src=os.path.join(self.source_folder, debugPath), keep_path=False)
                tools.files.copy(self, "FreeImaged.pdb", dst=os.path.join(self.package_folder, "bin"), src=os.path.join(self.source_folder, debugPath), keep_path=False)
            # Sign DLL
            if self.options.get_safe("dll_sign"):
                self.python_requires["windows_signtool"].module.sign(self, [os.path.join(self.package_folder, "bin", "*.dll")])
        # GNU
        if self.settings.os == "Linux":
            tools.files.copy(self, "libfreeimage-3.19.0.so", dst=os.path.join(self.package_folder, "lib"), src=os.path.join(self.source_folder, "src"), keep_path=False)
            with tools.files.chdir(self, os.path.join(self.package_folder, "lib")):
                self.run("ln --symbolic libfreeimage-3.19.0.so libfreeimage.so.3")

    def package_info(self):
        self.cpp_info.set_property("cmake_find_mode", "both")
        self.cpp_info.set_property("cmake_file_name", "freeimage")
        self.cpp_info.set_property("cmake_target_name", "freeimage::freeimage")
        self.cpp_info.libs = tools.files.collect_libs(self)
