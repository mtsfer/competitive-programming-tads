#include <iostream>
#include <string>

int main()
{
    int n {};
    int m {};

    while (true) {
        std::cin >> n >> m;
        std::string sum { std::to_string(n + m) };

        if (sum == "0") break;

        std::string output {};
        for (int i = 0; i < sum.size(); i++) {
            char curr = sum[i];
            if (curr != '0') output += curr;
        }
        std::cout << output << "\n";
    }

    return 0;
}
