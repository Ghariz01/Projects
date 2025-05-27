#include <iostream>
using namespace std;

double power(double base , int exponent)
{
    double result = 1.0;
    for(int i = 0; i <exponent; ++i)
    {
        result *= base;
    }

    return result;
}

int main()
{
    double base;
    int exponent;

    cout << "vale basi";
    cin >> base;
    cout << "Vale ek8eti";
    cin >> exponent;

    double result = power(base , exponent);

    cout << base << "upsomeno sti dinami tou" << exponent << "einai" << result <<endl;

    return 0;
}
