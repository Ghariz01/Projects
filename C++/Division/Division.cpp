#include <iostream>
#include <stdexcept>
using namespace std;

double dieresi (double ari8mitis , double dieretis)
{
    if (dieretis == 0)
    {
        throw runtime_error("Diereses me to mhden");
    }
    return ari8mitis / dieretis;
}

int main()
{
    double number1 , number2;

    cout << "Vale ari8miti";
    cin >> number1;
    cout << "Vale diereti";
    cin >> number2;

    try
    {
        double result = dieresi(number1 , number2);
        cout << "Apotelesma" << result << endl;
    }
    catch (const runtime_error&e)
    {
        cout << "oops" << e.what() << endl;
    }

    return 0;
}
