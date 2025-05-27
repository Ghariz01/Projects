#include <iostream>
using namespace std;

double CalculateAverage(double sum, int count)
{
    return sum/count;
}

int main()
{
    double number1 , number2 , number3 , number4 , number5;
    const int COUNT = 5;

    cout << "Vale 5 ari8mous" << endl;

    cout << "ari8mos 1";
    cin >> number1;
    cout << "ari8mos 2";
    cin >> number2;
    cout << "ari8mos 3";
    cin >> number3;
    cout << "ari8mos 4";
    cin >> number4;
    cout << "ari8mos 5";
    cin >> number5;


    double sum = number1 + number2 + number3 + number4 + number5;

    double average = CalculateAverage(sum , COUNT);

    cout << "o mesos oros einai " << average << endl;

    return 0;
}
