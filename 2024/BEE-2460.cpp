#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int n;
    cin >> n;

    vector<int> ids(n);

    for (int i = 0; i < n; i++) {
        int id;
        cin >> id;
        ids[i] = id;
    }

    int m;
    cin >> m;

    for (int i = 0; i < m; i++) {
        int id;
        cin >> id;
        for (int j = 0; j < n; j++) {
            if (ids[j] != id) continue;
            ids.erase(ids.begin() + j);
            break;
        }
    }

    for (int i = 0; i < ids.size() - 1; i++) {
        int id = ids[i];
        if (id != 0) cout << id << " ";
    }

    int last_id = ids.back();
    if (last_id != 0) cout << last_id;

    cout << "\n";

    return 0;
}
