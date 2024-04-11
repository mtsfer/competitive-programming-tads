#include <iostream>

int main()
{
    int n {};
    const int gap { 30 };

    while (std::cin >> n) {
        int next_time { 420 };
        int reached_critical { 0 };

        for (int i = 0; i < n; i++) {
            int hour {}; 
            int min {}; 
            int until_critical {};

            std::cin >> hour >> min >> until_critical;

            int arrived_at = hour * 60 + min;

            if (arrived_at > next_time)
                next_time = (int) ((arrived_at - 1) / gap + 1) * gap;

            if (next_time > arrived_at + until_critical)
                reached_critical++;

            next_time += gap;
        }

        std::cout << reached_critical << "\n";
    }

    return 0;
}

