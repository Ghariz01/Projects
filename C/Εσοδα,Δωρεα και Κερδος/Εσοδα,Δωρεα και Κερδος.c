#include <stdio.h>
#define kostos 0.0762
int main ()
{
    int sms;
    float esoda , dwrea , kerdos;
    printf( "Posa munhmata stalthikan?" );
    scanf( "%d" , &sms );
    esoda=sms*kostos;
    dwrea=esoda*0.60;
    kerdos=esoda-dwrea;
    printf( "Ta esoda tis etaireias apo ta sms einai %.2f \n" , esoda );
    printf( "H dwrea sta idrumata einai %.2f \n" , dwrea );
    printf ( "To kerdos tis etaireias einai %.2f \n" , kerdos );
    return 0;

}
