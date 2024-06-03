#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n, t;
    cin >> n >> t;

    string queue;
    cin >> queue;

    while (t-- > 0) {
        for (int i = 0; i < n - 1; i++) {
            if (queue[i] == 'B' && queue[i + 1] == 'G') {
                queue[i] = 'G';
                queue[i + 1] = 'B';
                i++;
            }
        }
    }

    cout << queue << "\n";

    return 0;
}
