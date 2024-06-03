#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    int qtt = 0;
    for (int i = 0; i < n; i++) {
        int p, q;
        cin >> p >> q;
        if (q - p >= 2) {
            qtt++;
        }
    }

    cout << qtt << '\n';

    return 0;
}
