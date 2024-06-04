#include <iostream>

int main()
{
    int n {};
    std::cin >> n;

    int total = n * n;
    int black = total / 2;
    int white = total - black;

    std::cout << white << " casas brancas e " << black << " casas pretas\n";

    return 0;
}
