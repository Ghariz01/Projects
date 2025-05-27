#include <stdio.h>
int main()
{
    float a , b , c , mo;
    printf( "Dwse 3 epidoseis" );
    scanf( "%f%f%f" , &a , &b , &c );
    mo=(a+b+c)/3;

    printf( "mesos oros %.2f \n" , mo );
    if(mo>=8)
    {
        printf( "Perase" );
    }
    else
    {
        printf( "Den perase" );
    }
    return 0;
}
