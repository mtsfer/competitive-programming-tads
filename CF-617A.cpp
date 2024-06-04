#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int dist;
    cin >> dist;

    int steps = 0;

    for (int i = 5; i > 0; i--) {
        steps += dist / i;
        dist %= i;
        if (dist <= 0) {
            break;
        }
    }

    cout << steps << "\n";

    return 0;
}
