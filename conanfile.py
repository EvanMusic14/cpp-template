from conan import ConanFile
from conan.tools.cmake import CMake, CMakeToolchain, CMakeDeps


class CompressorRecipe(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeToolchain", "CMakeDeps"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

