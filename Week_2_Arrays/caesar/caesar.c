#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

int main(int argc, string argv[]) 
{
    if (argc != 2)
    {
        printf("Usage: ./caesar key");
        return 1;
    }

    for (int i = 0; i < strlen (argv[1]); i++)
    {
        if (!isdigit(argv[1][i]))
        printf("usage: ./caesar key");
    }

    int k = atoi(argv[1]);       
    string plaintext = get_string("Plaintext: ");
    printf("Ciphertext ");

    for (int j = 0; j < strlen(plaintext); j++)
    {
        if (isupper(plaintext[j]))
        {
            printf("%c", (plaintext[j] - 'A' + k ) % 26 + 'A');
        }
        else if (islower(plaintext[j]))
        {
            printf("%c", (plaintext[j] - 'a' + k ) % 26 + 'a');
        }
        else
        {
            printf("%c", plaintext[j]);
        }
    }
    printf("\n");
 }
