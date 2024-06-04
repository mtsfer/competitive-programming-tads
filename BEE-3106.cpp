#include <iostream>

int main()
{
    const int team_size = 3;

    int n {};
    std::cin >> n;

    int contestants_total { 0 };
    for (int i = 0; i < n; i++) {
        int students_number {};
        std::cin >> students_number;

        contestants_total += students_number / team_size * team_size;
    }

    std::cout << contestants_total << "\n";

    return 0;
}
