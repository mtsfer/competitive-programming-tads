#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    vector<int> line(n);

    int taller = 0;
    int taller_idx = -1;

    int shorter = 1000;
    int shorter_idx = -1;

    for (int i = 0; i < n; i++) {
        int h;
        cin >> h;
        line[i] = h;
        if (h > taller) {
            taller = h;
            taller_idx = i;
        }
        if (h <= shorter) {
            shorter = h;
            shorter_idx = i;
        }
    }

    int swaps = taller_idx + n - 1 - shorter_idx;
    if (taller_idx > shorter_idx) {
        swaps--;
    }

    cout << swaps << '\n';

    return 0;
}
