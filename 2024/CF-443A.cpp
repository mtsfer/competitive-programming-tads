#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    string setstr;
    getline(cin, setstr);

    set<char> letters;

    for (int i = 1; i < setstr.size() - 1; i += 3) {
        letters.insert(setstr[i]);
    }

    cout << letters.size() << '\n';

    return 0;
}
