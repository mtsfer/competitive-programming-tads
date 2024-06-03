#include <bits/stdc++.h>

using namespace std;

int lcm3(int x, int y, int z) {
    return lcm(x, lcm(y, z));
}

int lcm4(int w, int x, int y, int z) {
    return lcm(w, lcm3(x, y, z));
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int k, l, m, n, d;
    cin >> k >> l >> m >> n >> d;

    int n1 = d/k + d/l + d/m + d/n;
    int n2 = d/lcm(k, l) + d/lcm(k, m) + d/lcm(k, n) + d/lcm(l, m) + d/lcm(l, n) + d/lcm(m, n);
    int n3 = d/lcm3(k, l, m) + d/lcm3(k, l, n) + d/lcm3(k, m, n) + d/lcm3(l, m, n);
    int n4 = d/lcm4(k, l, m, n);

    int result = n1 - n2 + n3 - n4;

    cout << result << "\n";

    return 0;
}
