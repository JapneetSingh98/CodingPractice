#include <stdio.h> 
#include <stdlib.h>
#include <string.h>

const char FORM_FINGERPRINT[] = "FORM";
const char SCDH_FINGERPRINT[] = "SCDH";

int main(int argc, char *argv[])  {
    FILE *fp = fopen(argv[1], "r");
    char form[5];
    char scdh[5];
    char garb[5];
    
    int lenForm = fread(&form, sizeof(char), 4, fp);
    int lengarb = fread(&garb, sizeof(char), 4, fp);
    int lenScdh = fread(&scdh, sizeof(char), 4, fp);

    form[4] = '\0';
    garb[4] = '\0';
    scdh[4] = '\0';
    printf("%s\n", form);
    printf("%s\n", garb);
    printf("%s\n", scdh);

    
    if (strcmp(form, FORM_FINGERPRINT) == 0 && strcmp(scdh, SCDH_FINGERPRINT) == 0) {
        printf("0\n");
        return 0;
    } else {
        printf("1\n");
        return 1;
    }
    
}