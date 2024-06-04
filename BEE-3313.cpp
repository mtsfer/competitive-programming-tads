#include <iostream>
#include <string>

int main()
{
    std::string word {};
    std::cin >> word;

    int round { 1 };

    while (word != "*") {
        int size = word.size();

        std::string min { word };
        std::string max { word };

        for (int i = 1; i < size; i++) {
            std::string shifted = word.substr(i) + word.substr(0, i);
            if (shifted < min) {
                min = shifted;
            } else if (shifted > max) {
                max = shifted;
            }
        }

        std::cout << "Caso " << round << ": " << min << " " << max << "\n";

        std::cin >> word;
        round++;
    }

    return 0;
}
