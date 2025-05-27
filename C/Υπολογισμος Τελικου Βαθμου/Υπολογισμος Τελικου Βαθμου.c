#include <stdio.h>
#include <math.h>
int main ()
{
    float b1 , b2 , b3 , Telikos;
    printf( "Dwse bathmo eksetasewn \n" );
    scanf( "%f" , &b1 );
    printf( "Dwse bnathmo proodou \n" );
    scanf( "%f" , &b2 );
    printf( "Dwse bathmo ergasias \n" );
    scanf( "%f" , &b3 );
    Telikos=(b1*0.6)+(b2*0.3)+(b3*0.1);
    printf( "O telikos bathmos sou einai: %.2f" , Telikos );
    return 0;
}
