#include <iostream>
using namespace std;

bool IsEven(int number)
{
    return number % 2 ==0;
}

int main()
{
    int number;

    cout << "vale akaireo ari8mo";
    cin >> number;

    if (IsEven(number))
    {
        cout << "o ari8mos "<< number << "einai artios"<< endl;
    } else
    {
        cout << "o ari8mos" << number << "einai perittos" << endl;
    }

    return 0;
}
