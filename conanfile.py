# FreeImage Conan package
# Dmitriy Vetutnev, ODANT 2018, 2020


from conans import ConanFile, MSBuild, tools
import os, glob


class FreeImageConan(ConanFile):
    name = "freeimage"
    version = "3.19.0-beta2+3"
    license = "FreeImage is licensed under the GNU General Public License, version 2.0 (GPLv2) or version 3.0 (GPLv3), and the FreeImage Public License (FIPL)"
    description = "FreeImage is an Open Source library project for developers who would like to support popular graphics image formats like PNG, BMP, JPEG, TIFF and others as needed by today's multimedia applications"
    url = "https://github.com/odant/conan-freeimage"
    settings = {
        "os": ["Windows", "Linux"],
        "compiler": ["Visual Studio", "gcc"],
        "build_type": ["Debug", "Release"],
        "arch": ["x86_64", "x86", "mips", "armv7"]
    }
    options = {
        "dll_sign": [True, False]
    }
    default_options = {
        "dll_sign": True
    }
    exports_sources = "src/*", "autoselect_win_sdk.patch", "fix_sources_list.patch", "fix_dll_version.patch", "remove_std_binary_function.patch"
    no_copy_source = False
    build_policy = "missing"

    def configure(self):
        # DLL sign
        if self.settings.os != "Windows":
            del self.options.dll_sign

    def build_requirements(self):
        if self.options.get_safe("dll_sign"):
            self.build_requires("windows_signtool/[~=1.1]@%s/stable" % self.user)

    def source(self):
        tools.patch(patch_file="autoselect_win_sdk.patch")
        if self.settings.os == "Windows":
            tools.patch(patch_file="fix_dll_version.patch")
            tools.patch(patch_file="remove_std_binary_function.patch")
        else:
            tools.patch(patch_file="fix_sources_list.patch")

    def build(self):
        if self.settings.compiler == "Visual Studio":
            self.msvc_build()
        else:
            self.unix_build()

    def msvc_build(self):
        with tools.chdir("src"):
            builder = MSBuild(self)
            #builder.build_env.cxx_flags = ["/std=c++14"]
            builder.build("FreeImage.2017.vcxproj", upgrade_project=False)

    def unix_build(self):
        build_env = {
            "CFLAGS": "-fPIC -fexceptions -fvisibility=hidden",
            "CXXFLAGS": "-fPIC -fexceptions -fvisibility=hidden -Wno-ctor-dtor-privacy -std=c++14"
        }
        if self.settings.build_type == "Debug":
            build_env["CFLAGS"] = "-Og -g -ggdb " + build_env["CFLAGS"]
            build_env["CXXFLAGS"] = "-Og -g -ggdb " + build_env["CXXFLAGS"]
        else:
            build_env["CFLAGS"] = "-O3 -DNDEBUG" + build_env["CFLAGS"]
            build_env["CXXFLAGS"] = "-O3 -DNDEBUG" + build_env["CXXFLAGS"]
        if self.settings.arch == "x86_64":
            build_env["CFLAGS"] = "-m64 " + build_env["CFLAGS"]
            build_env["CXXFLAGS"] = "-m64 " + build_env["CXXFLAGS"]
            build_env["LDFLAGS"] = "-m64"
        elif self.settings.arch == "x86":
            build_env["CFLAGS"] = "-m32 " + build_env["CFLAGS"]
            build_env["CXXFLAGS"] = "-m32 " + build_env["CXXFLAGS"]
            build_env["LDFLAGS"] = "-m32"
        #
        with tools.chdir("src"), tools.environment_append(build_env):
            self.run("make -j %s" % tools.cpu_count())

    def package(self):
        self.copy("FreeImage.h", dst="include", src="src/Source", keep_path=False)
        # MSVC
        if self.settings.os == "Windows":
            for releasePath in [ "src/x64/Release", "src/Win32/Release" ]:
                self.copy("FreeImage.lib", dst="lib", src=releasePath, keep_path=False)
                self.copy("FreeImage.dll", dst="bin", src=releasePath, keep_path=False)
                self.copy("FreeImage.pdb", dst="bin", src=releasePath, keep_path=False)
            for debugPath in [ "src/x64/Debug", "src/Win32/Debug" ]:
                self.copy("FreeImaged.lib", dst="lib", src=debugPath, keep_path=False)
                self.copy("FreeImaged.dll", dst="bin", src=debugPath, keep_path=False)
                self.copy("FreeImaged.pdb", dst="bin", src=debugPath, keep_path=False)
            # Sign DLL
            if self.options.get_safe("dll_sign"):
                import windows_signtool
                pattern = os.path.join(self.package_folder, "bin", "*.dll")
                for fpath in glob.glob(pattern):
                    fpath = fpath.replace("\\", "/")
                    for alg in ["sha1", "sha256"]:
                        is_timestamp = True if self.settings.build_type == "Release" else False
                        cmd = windows_signtool.get_sign_command(fpath, digest_algorithm=alg, timestamp=is_timestamp)
                        self.output.info("Sign %s" % fpath)
                        self.run(cmd)
        # GNU
        if self.settings.os == "Linux":
            self.copy("libfreeimage-3.19.0.so", dst="lib", src="src", keep_path=False)
            with tools.chdir(os.path.join(self.package_folder, "lib")):
                self.run("ln --symbolic libfreeimage-3.19.0.so libfreeimage.so.3")

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
