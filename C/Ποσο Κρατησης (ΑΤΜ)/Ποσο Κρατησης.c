#include <stdio.h>
#include <math.h>

int main()

{
    float poso , kratisi;
    printf( "Posa thes na bgaleis" );
    scanf( "%f" , &poso );
    kratisi=poso*0.01;

    if( kratisi<1 )
        printf( "1 euro kratisi" );

    else if( kratisi>3 )
        printf( "3 euro kratisi" );

    else
        printf( "H kratisi einai %.2f" , kratisi );

    return 0;
}
