#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int t;
    cin >> t;

    while (t--) {
        int n;
        cin >> n;

        vector<int> result;
        int power = 1;
        while (n > 0) {
            int alg = n % 10;
            if (alg != 0) {
                result.push_back(alg * power);
            }
            n /= 10;
            power *= 10;
        }

        cout << result.size() << '\n';
        for (int i = 0; i < result.size() - 1; i++) {
            cout << result[i] << ' ';
        }
        cout << result.back() << '\n';
    }

    return 0;
}
