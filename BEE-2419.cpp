#include <iostream>
#include <vector>

int main()
{
    int m {};
    int n {};

    std::cin >> m >> n;

    int terrn = m * n;

    std::vector<int> map(terrn);
    std::vector<int> landCoords;

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            char territory {};
            std::cin >> territory;
            if (territory == '.') continue;
            int idx = i * n + j;
            map[idx] = 1;
            landCoords.push_back(idx);
        }
    }

    int coastn {};

    for (int idx : landCoords) {
        int i = (int) idx / n;
        int j = idx % n;

        if (i == 0 || i == m - 1 || 
                j == 0 || j == n - 1 || 
                map[idx - n] == 0 || map[idx + n] == 0 || 
                map[idx - 1] == 0 || map[idx + 1] == 0) {
            coastn++;
        }
    }

    std::cout << coastn << "\n";

    return 0;
}
