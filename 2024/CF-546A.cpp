#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int k, n, w;
    cin >> k >> n >> w;

    int lastc = k + (w - 1) * k;
    int totalc = (k + lastc) * w / 2;

    if (n >= totalc) {
        cout << "0\n";
    }
    else {
        cout << totalc - n << "\n";
    }

    return 0;
}
