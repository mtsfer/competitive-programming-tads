#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    vector<int> ns(4);
    for (int i = 0; i < 4; i++) {
        cin >> ns[i];
    }

    sort(ns.begin(), ns.end());

    int max = ns[3];
    cout << max - ns[0] << ' ' << max - ns[1] << ' ' << max - ns[2] << '\n';

    return 0;
}
