#include <stdio.h>

int main()
{
    int i,num,sum;
    float mo;
    printf("Dwse arithmo apo 5 mexri 10");
    scanf("%d",&num);
    sum=0;
    if (num>=5&&num<=10)
    {
        for(i=1;i<=num;i++)
            sum=sum+i;
        mo=sum/num;
        printf("o mesos oros einai %.2f",mo);
    }
    else
        printf("Lathos arithmos");

    return 0;
}
