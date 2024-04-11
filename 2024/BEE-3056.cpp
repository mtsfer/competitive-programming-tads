#include <iostream>

int main()
{
    int n {};
    std::cin >> n;

    long long int result = (1 << n) + 1;
    result *= result;

    std::cout << result << "\n";

    return 0;
}
