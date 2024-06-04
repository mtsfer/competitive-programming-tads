#include <iostream>

int main()
{
    int p {};
    std::cin >> p;

    int n = p / 2;

    int shuffles { 0 };
    int position { 1 };

    bool left_side { true };

    do {
        position += left_side ? position : (p - position + 1) * -1;
        shuffles++;
        left_side = position <= n;
    } while (position != 1);

    std::cout << shuffles << "\n";

    return 0;
}
