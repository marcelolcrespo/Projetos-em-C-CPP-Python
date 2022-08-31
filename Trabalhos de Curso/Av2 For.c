#include <stdio.h>
#include <stdlib.h>

int main(){
    int num = 0, contador = 0, par = 0, impar = 0;
    //printf(" -- \tO valor inicial precisa ser maior que 0 -- \n");
    printf("\nDigite um valor inicial\n");
    scanf("%d", &contador);
    printf("Digite um valor final\n");
    scanf("%d", &num);
    //if(contador <= 0 || num <= 0){
        //printf("Um dos valores digitados e um numero invalido\n");
    //}else{
        for (contador = contador; contador <= num; contador = contador + 1){
            if(contador%2 == 0){
                par = par + 1;
                printf("Valor do contador e: \t%d e ele e Par\n", contador);
            }else{
                impar = impar + 1;
                printf("Valor do contador e: \t%d e ele e Impar\n", contador);
            }
        }
    //}
    printf("\nQuantidade de numeros Pares: \t%d\n", par);
    //printf("Quantidade de numeros Impares: \t%d\n", impar);
return 0;
}
