#include <stdio.h>
#include <math.h>

int main()

{
    float a;
    printf( "Dwse bathmo" );
    scanf( "%f" , &a );

    if( a>18&&a<=20 )
       printf( "Arista" );

    else if( a>16&&a<=18 )
        printf( "Poly kala" );

    else if( a>14&&a<=16 )
        printf( "Kala" );

    else if( a>12&&a<=14 )
        printf( "Metria" );

    else if( a>10&&a<=12 )
        printf( "Sxedon bash" );

    else if( a==10 )
        printf( "Bash" );

    else if( a<10 )
        printf( "Katw bashs" );

    else
        printf( "Akyros bathmos" );

    return 0;
}
