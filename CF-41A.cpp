#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    string bir, ber;
    cin >> bir >> ber;

    int end = bir.size() - 1;

    string result = "YES";
    for (int i = 0; i <= end; i++) {
        if (bir[i] != ber[end - i]) {
            result = "NO";
            break;
        }
    }

    cout << result << "\n";

    return 0;
}
