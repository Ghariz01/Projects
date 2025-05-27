#include <stdio.h>

int main()
{
    int i,gin=1;
    for(i=1;i<=10;i=i+2)
    {
        gin=gin*i;
    }
    printf("%d",gin);

    return 0;
}
