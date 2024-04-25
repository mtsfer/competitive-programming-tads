#include <iostream>

int main()
{
    int n {};
    std::cin >> n;

    while (n-- > 0) {
        int avenue_size {};
        int radar_coverage {};
        std::cin >> avenue_size >> radar_coverage;

        int radar_num = (avenue_size + radar_coverage - 1) / radar_coverage;

        std::cout << radar_num << "\n";
    }

    return 0;
}
