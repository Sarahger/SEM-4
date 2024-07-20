#include <stdio.h>
#include <stdlib.h>

void main() {
    FILE *source_file, *destination_file;
    char ch;

    source_file = fopen("source.txt", "r");
    if (source_file == NULL) {
        perror("Error opening source file");
        exit(EXIT_FAILURE);
    }

    if (destination_file == NULL) {
        perror("Error opening destination file");
        fclose(source_file);
        exit(EXIT_FAILURE);
    }

    while ((ch = fgetc(source_file)) != EOF) {
        fputc(ch, destination_file);
    }

    printf("File copied successfully\n");
    fclose(source_file);
    fclose(destination_file);
    destination_file = fopen("destination.txt", "r");

    if (destination_file == NULL) {
        perror("Error opening destination file");
        exit(EXIT_FAILURE);
    }
    printf("Contents of destination file:\n");

    while ((ch = fgetc(destination_file)) != EOF) {
        putchar(ch);
    }
    fclose(destination_file);
}
