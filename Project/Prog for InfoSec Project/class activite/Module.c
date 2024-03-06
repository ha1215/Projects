#include<stdio.h>

//create a struct that holds two integers. 
//Use typedef to create it with the name: "Data"
typedef struct {
    int x;
    int y;
} Data;



void scan1() {
    //Create a variable of type struct Data, on the stack. 
    //Read two integers into it using scanf, 
    //print them and their bitwise OR and AND value
    //Also print the scanf result code
    Data data;
    int a, b;
    printf("Enter two integers: ");
    int res = scanf("%d %d", &data.x, &data.y);
    printf("Integer 1: %d\n", data.x);
    printf("Integer 2: %d\n", data.y);

    printf("%c\n%c\n", a, b);

   

    printf("OR bitwise: %d\n", (data.x & data.y));
    printf("AND bitwise: %c\n", (data.x & data.y));

    printf("scanf returned: %i\n", res);

}




void scan2() {
    //Create a struct like in scan1(), but this time on the HEAP
    //Read two integers into it using scanf, 
    // print them as characters, and their bitwise OR  value
    // Add some value to each ( eg., mychar+2)   and print
    //Also print the scanf result code

    Data data = (Data*)malloc(sizeof(Data));
    int a, b;
    printf("Enter two integers: ");
    int res = scanf("%d %d", &data.x, &data.y);
    printf("Integer 1 (char): %c\n", data.x);
    printf("Integer 2 (char): %c\n", data.y);

    data.x += 2;
    data.y += 2;
    printf("Updated Integer 1 (char): %c\n", data.x);
    printf("Updated Integer 2 (char): %c\n", data.y);

    printf("Bitwise OR: %d\n", (data.x | data.y));
    printf("scanf returned: %d\n", res);
    free(data);

}

void scan3() {
    /**
    * Similar to above, get two strings s1 s2 (buffer size 20) using fgets
    * Perform  an AND operation on their first character, and store the result in
        first letter of s1
       print the string out using a for loop on characters
    */
    const int WORDSIZE = 20; //this does not work, it just means readonly in C, works in C++
    char s1[50] = "initial character array";
    char s2[50];



}

int main(int argc, char* argv[]) {


    // scan1();
    // scan2();
    //scan3();

     //fgets(p,50,stdin);
     //printf("%s\n", mystring);


    int nonsense = getchar();
    return 0;
}