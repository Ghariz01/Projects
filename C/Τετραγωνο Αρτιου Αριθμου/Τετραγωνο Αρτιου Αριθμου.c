#include <stdio.h>

int main()
{
    int i;
    do{
        printf("Enter number");
        scanf("%d",&i);

        if(i%2==0)
            printf("Number = %d",i*i);
    }while(i<10||i>20);
}
