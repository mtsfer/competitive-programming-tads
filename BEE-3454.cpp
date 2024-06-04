#include <iostream>
#include <string>

using namespace std;

int main()
{
    string transcription;
    cin >> transcription;

    if (transcription == "XXO" || transcription == "OXX")
    {
        cout << "Alice" << "\n";
    }
    else if (transcription == "XOX")
    {
        cout << '*' << "\n";
    }
    else
    {
        cout << '?' << "\n";
    }

    return 0;
}
