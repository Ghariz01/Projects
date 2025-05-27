#include <stdio.h>
int main ()
{
    float Therm1 , Therm2 , Therm3 , mo;
    printf( "Dwse thermokrasia gia kentro \n" );
    scanf( "%f" , &Therm1 );
    printf( "Dwse thermokrasia gia wraiokastro \n" );
    scanf( "%f" , &Therm2 );
    printf( "Dwse thermokrasia gia to retsiki \n" );
    scanf( "%f" , &Therm3 );
    mo=( Therm1 + Therm2 + Therm3 )/3;
    printf( "O mesos oros einai: %.2f" , mo );
    return 0;
}
