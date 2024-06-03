#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;

    vector<int> result(n);
    for (int i = 1; i <= n; i++) {
        int receiver;
        cin >> receiver;
        result[receiver - 1] = i;
    }

    for (int i = 0; i < n - 1; i++) {
        cout << result[i] << " ";
    }
    cout << result[n - 1] << "\n";

    return 0;
}
