#include <iostream>
#include <iomanip>

int main()
{
    int n {};

    while (std::cin >> n) {
        int total_workloaded_grades { 0 };
        int total_workload { 0 };

        for (int i = 0; i < n; i++) {
            int grade {};
            int workload {};
            std::cin >> grade >> workload;

            total_workloaded_grades += grade * workload;
            total_workload += workload;
        }

        float result = (float) total_workloaded_grades / (total_workload * 100);
        std::cout << std::fixed << std::setprecision(4) << (result) << "\n";
    }

    return 0;
}
