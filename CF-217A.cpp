#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int year;
    cin >> year;

    bool found = false;
    while (!found) {
        year++;
        vector<int> digits(10);

        found = true;
        for (int i = 4; i > 0; i--) {
            int ord = pow(10, i - 1);
            int digit = year / ord % 10;
            if (digits[digit] != 0) {
                found = false;
                break;
            }
            digits[digit]++;
        }
    }

    cout << year << "\n";

    return 0;
}
