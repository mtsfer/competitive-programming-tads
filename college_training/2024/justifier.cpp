#include <iostream>
#include <iomanip>
#include <string>
#include <vector>

int main()
{
    int n {}; 
    std::cin >> n;

    while (n) {
        std::vector<std::string> names(n);
        int longer_len {};

        for (int i = 0; i < n; i++) {
            std::string name;
            std::cin >> name;
            names[i] = name;

            int curr_len = name.length();
            if (curr_len > longer_len) {
                longer_len = curr_len; 
            }
        }

        for (int i = 0; i < n; i++) {
            std::cout << std::setw(longer_len) << names[i] << "\n";
        }

        std::cin >> n;

        if (n != 0) {
            std::cout << "\n";
        }
   }
}
