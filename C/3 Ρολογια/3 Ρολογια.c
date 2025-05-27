#include <stdio.h>

int main()
{
    int a=12,b=12,c=12,patimata=0;
    do
    {
        a=a+3;
        b=b+5;
        c=c+7;
        if(a>12)
        {
            a=a-12;
        }
        if(b>12)
        {
            b=b-12;
        }
        if(c>12)
        {
            c=c-12;
        }
        patimata++;
    }while(a!=12||b!=12||c!=12);

    printf("ola ta rologia tha dixnoun ksana 12:00 meta apo %d patimata",patimata);
    return 0;
}
