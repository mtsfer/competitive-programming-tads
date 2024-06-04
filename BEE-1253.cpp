#include <iostream>

int main()
{
    int n {};
    std::cin >> n;

    while (n-- != 0) {
        std::string encoded {};
        std::cin >> encoded;

        int shift {};
        std::cin >> shift;

        for (int i = 0; i < encoded.size(); i++) {
            int unshifted = encoded[i] - shift; 
            char decoded = 90 - (90 - unshifted) % 26;
            std::cout << decoded;
        }

        std::cout << "\n";
    }

    return 0;
}
