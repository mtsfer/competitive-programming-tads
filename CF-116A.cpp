#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    int curr = 0;
    int mincap = 0;
    for (int i = 0; i < n; i++) {
        int out, in;
        cin >> out >> in;
        curr += in - out;
        mincap = max(mincap, curr);
    }

    cout << mincap << "\n";

    return 0;
}
