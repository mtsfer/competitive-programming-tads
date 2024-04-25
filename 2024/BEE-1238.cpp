#include <iostream>

int main()
{
    int n {};
    std::cin >> n;

    while (n-- > 0) {
        std::string w1 {};
        std::string w2 {};

        std::cin >> w1 >> w2;
        int w1_len = w1.size();
        int w2_len = w2.size();

        int shorter_len = w1_len < w2_len ? w1_len : w2_len;

        for (int i = 0; i < shorter_len; i++) {
            std::cout << w1[i] << w2[i];
        }

        std::cout << w1.substr(shorter_len) << w2.substr(shorter_len) << "\n";
    }

    return 0;
}
