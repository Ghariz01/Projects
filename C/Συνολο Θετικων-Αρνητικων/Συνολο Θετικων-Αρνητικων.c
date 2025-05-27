#include <stdio.h>

int main()
{
    int i,thetikos,arnitikos;
    thetikos=0;
    arnitikos=0;
    printf("Dwse akaireo arithmo.Me mhden termatizei to programma");
    scanf("%d",&i);
    while(i!=0)
    {
        if(i>0)
            thetikos=thetikos+1;
        else if(i<0)
        arnitikos=arnitikos+1;
        printf("Dwse arithmo.Me mhden termatizei to programma");
        scanf("%d",&i);
    }

    printf("oi thetikoi arithmoi pou edwses einai %d",thetikos);
    printf("oi arnitikoi arithmoi pou edwses einai %d",arnitikos);
    return 0;
}
