#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

int main()
{
    srand(time(0));

    int player1 = rand() % 6 + 1;
    cout << "o paiktis 1 erikse" << player1 << endl;

    int player2 = rand() % 6 + 1;
    cout << "o paiktis 2 erikse" << player2 <<endl;

    if(player1 > player2)
    {
        cout << "o paiktis 1 kerdise" << endl;
    }
    else if(player2 > player1)
    {
        cout << "o paiktis 2 kerdise" << endl;
    }
    else
    {
        cout << "Isopalia" << endl;
    }

    return 0;
}
