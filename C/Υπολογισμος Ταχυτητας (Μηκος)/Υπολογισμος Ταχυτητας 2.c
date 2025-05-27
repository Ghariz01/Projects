#include <stdio.h>
#include <math.h>
int main()
{
    float M , Taxythta;
    printf( "Dwse mhkos \n" );
    scanf( "%f" , &M );
    Taxythta=2*3.14*sqrt( M/9.81 );
    printf( "H Taxythta einai: %.2f", Taxythta );
    return 0;
}
