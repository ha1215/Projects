/*
 * CSEC-201
 * Authors: CSEC-201 Instructors
 * Semester: 2221
 * Purpose: Header file for SHA_40
 */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define DIGEST_SIZE 5 //Size of SHA_40 hash in bytes
#define BLOCK_SIZE sizeof(struct Block) //Block size in bytes
#define BYTE unsigned char //Allows using BYTE in place of unsigned char

 //SHA_40 digest structure definition
struct Digest {
	BYTE hash0;
	BYTE hash1;
	BYTE hash2;
	BYTE hash3;
	BYTE hash4;
};

//Function Prototypes
unsigned char* SHA_40(const unsigned char* msg, size_t length); //SHA_40 hash function 
int digest_equal(struct Digest* digest1, struct Digest* digest2); //Returns 1 (true) or 0 (false)
void print_hash(struct Digest* digest); //Prints hash