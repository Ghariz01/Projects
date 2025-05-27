#include <stdio.h>
int main()
{
    int b;
    printf( "Dwse ilikia" );
    scanf( "%d" , &b );

    if(b<18)
    {
        printf( "Den psifizeis" );
    }

    else if(b>=18&&b<=70)
    {
        printf( "Psifizeis upoxreotika" );
    }

    else
    {
        printf( "Kane oti thes" );
    }
    return 0;
}
