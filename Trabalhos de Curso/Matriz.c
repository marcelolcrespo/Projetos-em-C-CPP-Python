#include <stdlib.h>
#include <stdio.h>

int main(){
    int matriz[3][3];
    int l,c,w,n,valor;

    w = 0;
    n = 0;
    valor = 0;
    printf("\n|| Guia || ==== L  C"); // GUIA
    for(l=0;l<3;l++){
        for(c=0;c<3;c++){
            printf("\nDigite o valor [%d][%d]: ", n,w); //
            scanf("%d", &matriz[l][c]);
            valor++; // indicador dos valores / posições
            //printf("valor %d", valor); // pegar o resultado de valor - usado para construir a logica.
            matriz[l][c] = matriz[l][c] * 5; // multiplicar todos os valores por 5
            if(valor >= 1){
                w++;
                if(valor >= 3){
                    n++;
                    w = 0;
                    valor = 0;
                }
            }
        }
    }
    for(l=0;l<3;l++){ // loop para printar a matriz
        printf("\n");
            for(c=0;c<3;c++){
                printf("\t%d ", matriz[l][c]);
            }
        printf("\n");
    }
    return 0;
}
