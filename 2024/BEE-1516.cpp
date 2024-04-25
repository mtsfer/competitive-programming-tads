#include <iostream>
#include <vector>

int main()
{
    while (true) {
        std::vector<std::string> map {};

        int n, m;
        std::cin >> n >> m;

        if (n + m == 0) break;

        for (int i = 0; i < n; i++) {
            std::string line {};
            std::cin >> line;
            map.push_back(line);
        }

        int a, b;
        std::cin >> a >> b;

        int msc = b / m;
        int nsc = a / n;

        for (int i = 0; i < n; i++) {
            std::string line = map[i];
            std::string scaled {};
            for (int j = 0; j < m; j++) {
                char element = line[j];
                scaled += std::string(msc, element);
            }
            for (int j = 0; j < nsc; j++) {
                std::cout << scaled << "\n";
            }
        }

        std::cout << "\n";
    }

    return 0;
}
