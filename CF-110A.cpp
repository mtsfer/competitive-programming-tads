#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    string n;
    cin >> n;

    int ldn = 0;
    for (int i = 0; i < n.size(); i++) {
        if (n[i] == '4' || n[i] == '7') {
            ldn++;
        }
    }

    if (ldn == 4 || ldn == 7) {
        cout << "YES\n";
    }
    else {
        cout << "NO\n";
    }

    return 0;
}
