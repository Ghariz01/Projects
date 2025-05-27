#include <stdio.h>

int main()
{
    int i;
    for(i=10;i>0;i--)
    {
        printf("%d",i);
        if(i==3)
        {
            printf("H antistrofi metrisi stamatise");
            break;
        }
    }
    return 0;
}
