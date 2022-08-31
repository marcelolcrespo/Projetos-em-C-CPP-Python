#include <stdio.h>
#include <stdlib.h>

int main(){
    int contador = 1, idade = 0, quant = 0, total = 0;
    printf("Quantos membros tem na sua familia? \n");
    scanf("%d", &quant);
    printf("Ok!\n");
    for(contador = contador; contador <= quant; contador = contador +1){
        printf("Digite a idade do %dº\n", contador);
        scanf("%d", &idade);
        total = total + idade;
    }
        printf("Valor total das idades da sua familia = %d\n", total);
        printf("Valor medio de idades da sua familia e = %d\n", total / quant);
return 0;
}
