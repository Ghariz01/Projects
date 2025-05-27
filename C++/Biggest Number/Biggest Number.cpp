#include <iostream>
using namespace std;

int main()
{
    int max;
    int a,b,c;
    cout << "Enter 3 Numbers" << endl;
    cin >> a >> b >> c;


    max = a;

    if(b>max)
    {
        max = b;
    }

    if(c>max)
    {
        max = c;
    }

    cout << "The Highest Number Is" << max << endl;

    return 0;
}
