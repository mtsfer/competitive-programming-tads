#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    vector<int> bills { 100, 20, 10, 5, 1 };
    int billsn = 0;

    for (int i = 0; i < bills.size(); i++) {
        billsn += n / bills[i];
        n %= bills[i];
        if (n == 0) {
            break;
        }
    }

    cout << billsn << '\n';

    return 0;
}
