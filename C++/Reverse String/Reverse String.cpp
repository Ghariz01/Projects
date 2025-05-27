#include <iostream>
#include <string>
using namespace std;

int main()
{
    string leksi;

    cout << "Vale ena string";
    getline(cin , leksi);

    string reversedString = string(leksi.rbegin(), leksi.rend());

    cout << "Anapoda einai" << reversedString << endl;

    return 0;
}
