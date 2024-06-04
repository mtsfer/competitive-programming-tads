#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    string hate = "I hate";
    string love = "I love";

    bool hating = true;
    for (int i = 0; i < n - 1; i++) {
        if (hating) {
            cout << hate;
        }
        else {
            cout << love;
        }
        cout << " that ";
        hating = !hating;
    }

    if (hating) {
        cout << hate;
    }
    else {
        cout << love;
    }

    cout << " it\n";

    return 0;
}
