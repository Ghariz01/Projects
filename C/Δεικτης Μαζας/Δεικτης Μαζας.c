#include <stdio.h>
int main ()
{
    float y , b , bmi;
    printf( "Dwse ypsos" );
    scanf( "%f" , &y );
    printf( "Dwse varos" );
    scanf ( "%f" , &b );
    bmi=b/(y*y);
    printf( "O diktis mazas einai %f \n" , bmi );

    if(bmi<20)
    {
        printf( "Katw apo kanoniko" );
    }

    else if(bmi<=25)
    {
        printf( "Kanoniko" );
    }

    else if(bmi<=30)
    {
        printf( "Ypervaros" );
    }

    else if(bmi<=40)
    {
        printf( "Paxisarkos" );
    }

    else
    {
        printf( "Prosexe" );
    }
    return 0;
}
