#include <iostream>

int main()
{
    short tries;
    while (std::cin >> tries) {
        float best;
        std::cin >> best;
        for (short i = 0; i < tries - 1; i++) {
            float current;
            std::cin >> current;
            if (current < best) {
                best = current;
            }
        }
        std::cout << best << std::endl;
    }

    return 0;
}
