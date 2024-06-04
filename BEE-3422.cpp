#include <iostream>
#include <string>

using namespace std;

int main()
{
   int n;
   cin >> n;

   while (n-- > 0)
   {
      int half_minutes;
      string half;
      cin >> half_minutes >> half;

      int extra = half_minutes > 45 ? half_minutes - 45 : 0;
      int total_minutes = half_minutes - extra;

      if (half == "2T") total_minutes += 45;

      cout << total_minutes;
      if (extra != 0) cout << '+' << extra;
      cout << "\n";
   }

   return 0;
}
