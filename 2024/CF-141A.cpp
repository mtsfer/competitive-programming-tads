#include <bits/stdc++.h>

using namespace std;

void fill_count_letters(vector<int> &letters_count, string name) {
    for (char letter : name) {
        int idx = letter - 'A';
        letters_count[idx]++;
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    string guest, host, pile;
    cin >> guest >> host >> pile;

    vector<int> names_letters_count(26);
    vector<int> pile_letters_count(26);

    fill_count_letters(names_letters_count, guest);
    fill_count_letters(names_letters_count, host);
    fill_count_letters(pile_letters_count, pile);

    bool restorable = true;
    for (int i = 0; i < 26; i++) {
        if (names_letters_count[i] != pile_letters_count[i]) {
            restorable = false;
            break;
        }
    }

    if (restorable) {
        cout << "YES\n";
    }
    else {
        cout << "NO\n";
    }

    return 0;
}
