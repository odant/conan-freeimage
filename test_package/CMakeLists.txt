project(PackageTest CXX)
cmake_minimum_required(VERSION 3.0)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

enable_testing()

# CONAN_PKG::freeimage imported targets

add_executable(test_package_CONAN_PKG test_package.cpp)
target_link_libraries(test_package_CONAN_PKG CONAN_PKG::freeimage)
set_target_properties(test_package_CONAN_PKG
    PROPERTIES
    INSTALL_RPATH "$ORIGIN"
    BUILD_WITH_INSTALL_RPATH True
)
add_test(
    NAME test_package_CONAN_PKG
    WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin
    COMMAND test_package_CONAN_PKG
)
