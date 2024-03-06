#include <stdio.h>

#include <stdlib.h>

typedef unsigned char BYTE;

int main(){

char x[] = { 'a', 'a', 'a' };
*x += 1;

*(x + 1) += 1;

x[2] += 1;
    return 0;

}

