#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    int result = 0;
    while (n-- > 0) {
        string op;
        cin >> op;
        if (op == "++X" || op == "X++") {
            result++;
        }
        else {
            result--;
        }
    }

    cout << result << "\n";

    return 0;
}
