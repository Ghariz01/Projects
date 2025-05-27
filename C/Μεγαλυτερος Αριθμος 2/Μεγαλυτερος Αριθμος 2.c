#include <stdio.h>

int main()
{
    int num,metritis,max,i;
    metritis=0;
    max=0;
    for (i=0;i<=10;i++)
    {
        printf("Dwse arithmo");
        scanf("%d",&num);
        if(num>max)
        {
            metritis=1;
            max=num;
        }

        else if(num==max)
        {
            metritis=metritis+1;
        }
    }
    printf("o megaliteros einai o %d kai emfanizetai %d fores",max,metritis);

    return 0;
}
