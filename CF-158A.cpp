#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n, k;
    cin >> n >> k;

    int next = 0;
    int kscore = -1;

    for (int i = 1; i <= n; i++) {
        int score;
        cin >> score;
        if (score == 0 || score < kscore) {
            break;
        }
        if (i == k) {
            kscore = score;
        }
        next++;
    }

    cout << next << "\n";

    return 0;
}
