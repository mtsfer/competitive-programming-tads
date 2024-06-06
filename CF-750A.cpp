#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n, k;
    cin >> n >> k;

    int ps = 0;
    int ft = 240 - k;
    for (int i = 1; i <= n; i++) {
        ft -= 5 * i;
        if (ft < 0) break; 
        ps++;
    } 

    cout << ps << '\n';

    return 0;
}
