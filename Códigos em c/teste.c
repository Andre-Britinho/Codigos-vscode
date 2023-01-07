#include <stdio.h>
#include <stdlib.h>

void main(){
    int matriz[2][2];
    int maior_numero = 0;

    for(int i = 0; i < 2; i++){
        for(int j = 0; j < 2; j++){
            printf("Digite um número: ");
            scanf("%d", &matriz[i][j]);
            if(matriz[i][j] > maior_numero){
                maior_numero = matriz[i][j];
            }
        }
    }

    printf("Matriz: \n");
    for(int i = 0; i < 2; i++){
        for(int j = 0; j < 2; j++){
            printf("%4d", matriz[i][j]);            
        }
        printf("\n");
    }
    printf("Maior número = %d",maior_numero);


}//main