#include <stdio.h>

int main()
{
    int a;
    printf("Dwse bathmo apo 1 mexri 10");
    scanf("%d",&a);
    switch(a)
    {
        case 9:
        case 10:
        printf("Arista");
        break;

        case 7:
        case 8:
        printf("Lian Kalws");
        break;

        case 6:
        case 5:
        printf("Kala");
        break;

        case 4:
        case 3:
        case 2:
        case 1:
        printf("Den perases");
        break;

        default:printf("Lathos arithmos");

    }
}
