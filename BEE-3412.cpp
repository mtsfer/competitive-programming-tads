#include <iostream>
#include <string>
#include <sstream>
#include <iomanip>
#include <algorithm>

using namespace std;

int main()
{
   int n;
   cin >> n;

   while (n-- > 0)
   {
      string name;
      getline(cin >> ws, name);

      string scores;
      getline(cin, scores);
      istringstream is(scores);

      int qtt = 0;
      float sum = 0;
      float lowest = 10.0;

      float score;
      while (is >> score)
      {
         sum += score;
	 lowest = min(score, lowest);
	 qtt++;
      }

      if (qtt == 4)
      {
         sum -= lowest;
	 qtt--;
      }

      float grade = sum / max(2, qtt);
      cout << name << ": " << fixed << setprecision(1) << grade << "\n";
   }

   return 0;
}
