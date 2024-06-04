#include <iostream>

int eight_pow(int p) {
    int n = 8;
    while(p-- > 0) n *= 8;
    return n;
}

int main()
{
    int p {};
    std::cin >> p;

    if (p == 0) {
        std::cout << "1\n";
    } else {
        std::cout << eight_pow((p - 1) % 4) % 10 << "\n";
    }

    return 0;
}

