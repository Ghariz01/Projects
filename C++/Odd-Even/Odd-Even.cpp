#include <iostream>
using namespace std;

string EvenOdd(int number)
{
    string res = "placeholder";
    if (number%2 == 0) {
        res = "even";
    } else {
        res = "odd";
    }
    return res;

}

int main()
{
    int num;

    cout << "Vale Arithmo";
    cin >> num;

    cout << num << "einai" << EvenOdd(num) << endl;

    return 0;
}
