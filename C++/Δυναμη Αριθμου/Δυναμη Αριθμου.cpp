#include <iostream>
using namespace std;

int CalculatePower(int Vasi , int Dinami) {
int res = 1;
for (int i = 0;i<Dinami;++i){
    res *= Vasi;
    }
    return res;
}

int main (){

    int num, pow;

    cout << "Vale Arithmo";
    cin >> num;

    cout << "Vale Ektheti";
    cin >> pow;

    int result = CalculatePower(num , pow);
    cout << "To apotelesma einai" << result << endl;

    return 0;
}
