#include <iostream>
using namespace std;

int calculateFac(int number)
{
    int fac = 1;
    for(int i=1;i<=number;++i) {
        fac = fac *i;
    }
    return fac;
}

int main()
{
    int num;

    cout << "Dwse arithmo";
    cin >> num;

    cout << "factorial of" << num << "is" << calculateFac(num) << endl;

    return 0;
}
