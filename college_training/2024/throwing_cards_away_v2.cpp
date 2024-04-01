#include <iostream>

int main()
{
    int n {};

    while (std::cin >> n && n != 0) {
        if (n == 1) {
            std::cout << "Discarded cards:\nRemaining card: 1\n";
            continue;
        }

        std::cout << "Discarded cards: ";

        int last_even {};
        int last_odd {};
        
        bool is_even = n % 2 == 0;
        if (is_even) {
            last_even = n;
            last_odd = n - 1;
        } else {
            last_even = n - 1;
            last_odd = n;
        }

        for (int i = 1; i < last_odd; i += 2) {
            std::cout << i << ", "; 
        }
        std::cout << last_odd;

        int starts_at { 2 };
        int ends_at { last_even };

        int curr_num { 2 };
        int jump_factor { 2 };

        bool discard_next = is_even;

        while (starts_at != ends_at) {
            if (curr_num > ends_at) {
                curr_num = starts_at;
                jump_factor *= 2;
            }

            if (discard_next) {
                if (curr_num == starts_at) {
                    starts_at += jump_factor;
                } else if (curr_num == ends_at) {
                    ends_at -= jump_factor;
                }
                std::cout << ", " << curr_num;
                discard_next = false;
            } else {
                discard_next = true;
            }

            curr_num += jump_factor;
        }

        std::cout << "\n";
        std::cout << "Remaining card: " << starts_at << "\n";
    }

    return 0;
}

