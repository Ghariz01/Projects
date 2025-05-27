#include <stdio.h>

int main()
{
    char ch='A';
    do{
        printf("%c",ch);
        ch=ch+1;
    }while (ch<='Z');
}
