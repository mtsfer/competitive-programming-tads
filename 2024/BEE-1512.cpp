#include <iostream>
#include <numeric>

int main() {

    while (true) {
        int n, a, b;
        std::cin >> n >> a >> b;

        if (n == 0 && a == 0 && b == 0) break;
        
        int aqtt = (n - a) / a + 1;
        int bqtt = (n - b) / b + 1;

        long long int ablcm = (long long int) a * b / std::gcd(a, b);

        int abqtt = ablcm > n ? 0 : (n - ablcm) / ablcm + 1;

        int result = aqtt - abqtt + bqtt;
        std::cout << result << "\n";
    }

    return 0;
}
