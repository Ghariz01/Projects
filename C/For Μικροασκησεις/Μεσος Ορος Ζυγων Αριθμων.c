#include <stdio.h>

int main()
{
    int i,num,sum,metritis;
    sum=metritis=0;
    for (i=0;i<=10;i++)
    {
        printf("Dwse arithmo");
        scanf("%d",&num);

        if(num==-1)
            break;
        if(num%2==0)
        {
            sum=sum+num;
            metritis++;
        }
    } if(metritis!=0)
        printf("o mesos oros einai %.2f",(float)sum/metritis);
      else
        printf("den edwses zygous arithmous");

      return 0;
}
