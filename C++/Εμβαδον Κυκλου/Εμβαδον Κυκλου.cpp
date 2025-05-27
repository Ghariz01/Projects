#include <iostream>
using namespace std;

float PI = 3.14159;

float CalculateCircleArea(float Aktina) {
return PI * Aktina * Aktina;
}

int main()
{
    float r;

    cout << "Vale Aktina Kyklou";
    cin >> r;

    float area = CalculateCircleArea (r);
    cout << "To embadon einai" << area << endl;

    return 0;
}
