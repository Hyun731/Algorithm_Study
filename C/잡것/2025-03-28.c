#include <stdio.h>

int main(){
    char room[21];
    scanf("%s",room);
    for(int i = 0; room[i] != '\0'; i++){
        printf("'%c'",room[i]);
        printf("\n");

    }
}