#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    string n1;
    cin >> n1;
    string n2;
    cin >> n2;

    string result;
    for (int i = 0; i < n1.length(); i++) {
        if (n1[i] == n2[i]) {
            result += '0';
        }
        else {
            result += '1';
        }
    }

    cout << result << "\n";

    return 0;
}
