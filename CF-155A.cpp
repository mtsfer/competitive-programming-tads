#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    int p;
    cin >> p;
    n--;

    int min = p;
    int max = p;

    int amaz = 0;
    while (n--) {
        cin >> p;
        if (p > max) {
            max = p;
            amaz++;
        }
        else if (p < min) {
            min = p;
            amaz++;
        }
    }

    cout << amaz << '\n';

    return 0;
}
