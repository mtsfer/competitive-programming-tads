#include <iostream>

int main()
{
    int n {};
    std::cin >> n;

    while (n-- > 0) {

        int num {};
        std::cin >> num;

        int spheres { 0 };

        for (int i = 1; i <= num; i++) {
            int divisors { 0 };

            for (int j = 1; j <= i; j++) {
                if (i % j == 0) divisors++;
            }

            if (divisors % 2 == 0) spheres++;
        }

        std::cout << spheres << "\n";
    }

    return 0;
}
