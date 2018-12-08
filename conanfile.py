# FreeImage Conan package
# Dmitriy Vetutnev, ODANT 2018


from conans import ConanFile, MSBuild, tools


class FreeImageConan(ConanFile):
    name = "freeimage"
    version = "3.18.0+0"
    license = "FreeImage is licensed under the GNU General Public License, version 2.0 (GPLv2) or version 3.0 (GPLv3), and the FreeImage Public License (FIPL)"
    description = "FreeImage is an Open Source library project for developers who would like to support popular graphics image formats like PNG, BMP, JPEG, TIFF and others as needed by today's multimedia applications"
    url = "https://github.com/odant/conan-freeimage"
    settings = {
        "os": ["Windows", "Linux"],
        "compiler": ["Visual Studio", "gcc"],
        "build_type": ["Debug", "Release"],
        "arch": ["x86_64", "x86", "mips"]
    }
    options = {
        "dll_sign": [True, False]
    }
    default_options = "dll_sign=True"
    exports_sources = "src/*", "msbuild_suffix.patch"
    no_copy_source = False
    build_policy = "missing"

    def source(self):
        tools.patch(patch_file="msbuild_suffix.patch")

    def build(self):
        if self.settings.compiler == "Visual Studio":
            self.msvc_build()
        else:
            self.unix_build()

    def msvc_build(self):
        with tools.chdir("src"):
            builder = MSBuild(self)
            builder.build("FreeImage.2017.vcxproj", upgrade_project=False)

    def unix_build(self):
        pass

    def package(self):
        self.copy("FreeImage.h", dst="include", src="src/Source", keep_path=False)
        # MSVC
        self.copy("FreeImage64.lib", dst="lib", src="src/x64/Release", keep_path=False)
        self.copy("FreeImage64.dll", dst="bin", src="src/x64/Release", keep_path=False)
        self.copy("FreeImage64.pdb", dst="bin", src="src/x64/Release", keep_path=False)
        self.copy("FreeImage64d.lib", dst="lib", src="src/x64/Debug", keep_path=False)
        self.copy("FreeImage64d.dll", dst="bin", src="src/x64/Debug", keep_path=False)
        self.copy("FreeImage64d.pdb", dst="bin", src="src/x64/Debug", keep_path=False)
        self.copy("FreeImage.lib", dst="lib", src="src/Win32/Release", keep_path=False)
        self.copy("FreeImage.dll", dst="bin", src="src/Win32/Release", keep_path=False)
        self.copy("FreeImage.pdb", dst="bin", src="src/Win32/Release", keep_path=False)
        self.copy("FreeImaged.lib", dst="lib", src="src/Win32/Debug", keep_path=False)
        self.copy("FreeImaged.dll", dst="bin", src="src/Win32/Debug", keep_path=False)
        self.copy("FreeImaged.pdb", dst="bin", src="src/Win32/Debug", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
