#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define MAX_STRING_LENGTH 100
#define MAX_CYPHER_LENGTH 30
#define MAX_MAPPING_SIZE 10

int main() {
    char str[MAX_STRING_LENGTH];
    char arr1[MAX_MAPPING_SIZE];
    char arr2[MAX_MAPPING_SIZE];
    char file[MAX_CYPHER_LENGTH];
    int xx;

    printf("Hello, please enter a string: ");
    scanf("%99s", str);

    printf("\nPlease choose an option:\n");
    printf("1 = Encrypt the string.\n");
    printf("2 = Decrypt the string.\n");
    scanf("%d", &xx);

    printf("\nPlease Enter The File Name: ");
    scanf("%29s", file);

    FILE* thefile = fopen(file, "r");
    if (thefile == NULL) {
        perror("Error opening the file");
        exit(1);
    }

    // Initialize mapping arrays
    memset(arr1, 0, sizeof(arr1));
    memset(arr2, 0, sizeof(arr2));

    char line[MAX_MAPPING_SIZE];
    while (fgets(line, sizeof(line), thefile)) {
        char ch1 = line[0];
        char ch2 = line[2];

        // Check for duplicate letters
        for (int i = 0; i < MAX_MAPPING_SIZE; i++) {
            if (arr1[i] == ch1) {
                perror("\nDuplicate letter from the left side\n");
                exit(1);
            }

            if (arr2[i] == ch2) {
                perror("\nDuplicate letter from the right side\n");
                exit(1);
            }

            // Add mappings to arrays
            if (arr1[i] == 0) {
                arr1[i] = ch1;
                arr2[i] = ch2;
                break;
            }
        }
    }

    switch (xx) {
    case 1:
        for (int i = 0; i < strlen(str); i++) {
            int j = 0;
            while (arr1[j] != '\0') {
                if (str[i] == arr1[j] || str[i] == tolower(arr1[j])) {
                    str[i] = arr2[j];
                }
                j++;
            }
        }
        printf("\nEncrypted string: %s\n", str);
        break;

    case 2:
        for (int i = 0; i < strlen(str); i++) {
            int j = 0;
            while (arr1[j] != '\0') {
                if (str[i] == arr2[j] || str[i] == tolower(arr2[j])) {
                    str[i] = arr1[j];
                }
                j++;
            }
        }

        printf("\nDecrypted string: %s\n", str);
        break;

    default:
        printf("\nError: Invalid option\n");
    }

    fclose(thefile);  // Close the file after usage

    return 0;
}
