#include <iostream>
using namespace std;

int main()
{
    char praksi;
    float num1 , num2;

    cout << "Dwse 2 ari8mous" << endl;
    cin >> num1 >> num2;

    cout << "Dwse praksi poy tha ginei" << endl;
    cin >> praksi;

    switch(praksi)
    {
         case '+':
             cout << num1 + num2;
             break;
         case '-':
             cout << num1 - num2;
             break;
         case '*':
             cout << num1 * num2;
             break;
         case '/':
             cout << num1 / num2;
             break;


    }

    return 0;
}
