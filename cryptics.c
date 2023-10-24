#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define INITIAL_MAX_MESSAGE 5000
#define MAX_KEY 50
#define MAX_ASCII 126
#define MIN_ASCII 1
#define ASCII_OFSET 125

FILE *infile ;
FILE *outfile ;

void encrypt(char* message, char* key) {
    int key_position = 0 ;
    for (char c = *message; c != '\0'; c = *++message) {
        int msg_ascii = c ;
        int key_ascii = *key ;
        int result_ascii = msg_ascii + key_ascii + key_position;
        while ( result_ascii > MAX_ASCII ) {
            result_ascii -= ASCII_OFSET ;
        }

        putc(result_ascii, outfile) ;
        key_position++ ;
        if(*++key == '\0') {
            key -= key_position ;
            key_position = 0 ;
        }
    }
}

void decrypt(char* message, char* key) {
    int key_position = 0;
    key += key_position ;
    for (char c = *message; c != '\0'; c = *++message) {
        int msg_ascii = c ;
        int key_ascii = *key ;
        int result_ascii = msg_ascii - key_ascii - key_position;
        while ( result_ascii < MIN_ASCII ) {
            result_ascii += ASCII_OFSET ;
        }

        putc(result_ascii, outfile) ;
        key_position++ ;
        if(*++key == '\0') {
            key -= key_position ;
            key_position = 0 ;
        }
    }
}

int main(int argc, char *argv[]) {
    if (argc != 3) {
        return 1;
    }

    char message[INITIAL_MAX_MESSAGE + 1] ;
    char* message_inc = message ;
    char key[MAX_KEY + 1] ;
    char* key_inc = key ;
    
    infile = fopen(argv[2], "r") ;

    for(int i=getc(infile); i != EOF; i=getc(infile)) {
        char c = i ;
        *message_inc = c ;
        message_inc++ ;
    }
    *message_inc = '\0' ; 
    fclose(infile) ;

    printf("Enter encryption key: ") ;
    for(int i=getchar(); i != 10; i=getchar()) {
        char c = i ;
        *key_inc = c ;
        key_inc++ ;
    }
    *key_inc = '\0' ;

    outfile = fopen(argv[2], "w") ;
    if ( *(argv[1]) == 'e') {
        encrypt(message, key) ;
    } else {
        decrypt(message, key) ;
    }
    fclose(outfile) ;

    return 0 ;
}
