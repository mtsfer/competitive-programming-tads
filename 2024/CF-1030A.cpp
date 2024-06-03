#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;
    
    string result = "EASY";
    for (int i = 0; i < n; i++) {
        int opinion;
        cin >> opinion;
        if (opinion == 1) {
            result = "HARD";
            break;
        }
    }

    cout << result << "\n";

    return 0;
}
