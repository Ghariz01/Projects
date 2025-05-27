#include <stdio.h>
#include <math.h>

int main()

{

    int Gwnia;
    printf( "Dwse megethos gwnias" );
    scanf( "%d" , &Gwnia );

    if( Gwnia>90 )
      printf( "Amvleia" );
    else if( Gwnia<90 )
      printf( "Okseia" );
    else
      printf( "Orthi" );

   return 0;
}
