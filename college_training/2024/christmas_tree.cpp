#include <iostream>
#include <string>

void print_tree(int n, int stages) {
    for (int i = 0; i < stages; i++) {
        int starsn = 1 + i * 2;
        int spacesn = (int) (n - starsn) / 2;
        std::cout << std::string(spacesn, ' ') << std::string(starsn, '*') << "\n";
    }
}

int main() {
    int n {};
    while (std::cin >> n) {
        int stages = (int) (n + 1) / 2;
        print_tree(n, stages);
        print_tree(n, 2);
        std::cout << "\n";
    }
    return 0;
}

