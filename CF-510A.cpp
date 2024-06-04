#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n, m;
    cin >> n >> m;

    cout << string(m, '#') << '\n';

    for (int i = 0; i < n - 2; i++) {
        if (i % 4 == 0) {
            cout << string(m - 1, '.') << '#' << '\n';
        }
        else if (i % 2 == 0) {
            cout << '#' << string(m - 1, '.') << '\n';
        }
        else {
            cout << string(m, '#') << '\n';
        }
    }

    cout << string(m, '#') << '\n';

    return 0;
}
