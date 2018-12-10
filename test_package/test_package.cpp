#include <FreeImage.h>

#include <iostream>
#include <cstdlib>


int main(int, char**) {
    std::cout << "FreeImage_GetVersion(): " << FreeImage_GetVersion() << std::endl;
    return EXIT_SUCCESS;
}
