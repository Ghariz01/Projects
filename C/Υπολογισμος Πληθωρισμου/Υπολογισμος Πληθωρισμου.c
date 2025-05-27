#include <stdio.h>

int main()
{
    int xronia;
    float pli8ismos=100000;
    for(xronia=0;xronia<5;xronia++)
    {
        pli8ismos=pli8ismos+pli8ismos*0.033;
    }
    printf("o pli8ismos einai %.2f",pli8ismos);
}
