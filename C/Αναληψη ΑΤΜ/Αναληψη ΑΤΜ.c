#include <stdio.h>
#define poso 30000
int main()
{
    float a , y;
    printf( "Dwse poso analipsis" );
    scanf( "%f" , &a );
    y=poso-a;

    if(y>0)
    {
        printf( "To upoloipo einai %.2f" , y );
    }

    else
    {
        printf( "Einai adunaton" );
    }
    return 0;
}
