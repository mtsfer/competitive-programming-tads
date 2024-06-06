#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int a, b;
    cin >> a >> b;

    int min = a;
    int max = b;

    if (a > b) {
        min = b;
        max = a;
    }

    int same = (max - min) / 2;
    cout << min << ' ' << same << '\n';

    return 0;
}
