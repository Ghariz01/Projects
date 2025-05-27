#include <iostream>
using namespace std;


int factorial(int n)
{
    if (n==0) return 1;
    int result = 1;
    for (int i = 1; i<=n; ++i)
    {
        result *=i;
    }

    return result;
}

int main()
{
    int number;

    cout << "vale ari8mo gia paragontiko";
    cin >> number;

    if (number <0)
    {
        cout << "to paragontiko den orizetai me arnitikous ari8mous" << endl;
    } else
    {
        int result = factorial(number);
        cout << "to paragontiko tou" << number << "einai" << result <<endl;
    }

    return 0;
}
