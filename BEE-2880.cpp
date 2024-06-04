#include <iostream>
#include <string>

bool has_similarity(std::string &s1, std::string &s2, int size) {
    for (int i = 0; i < size; i++) {
        if (s1[i] == s2[i]) return true;
    }
    return false;
}

int main()
{
    std::string encrypted {};
    std::cin >> encrypted;

    std::string crib {};
    std::cin >> crib;

    int crib_size = crib.size();
    int slides = encrypted.size() - crib_size;

    int possibilities { 0 };
    for (int i = 0; i <= slides; i++) {
        std::string slice = encrypted.substr(i, crib_size);
        if (!has_similarity(slice, crib, crib_size)) possibilities++;
    }

    std::cout << possibilities << "\n";

    return 0;
}
