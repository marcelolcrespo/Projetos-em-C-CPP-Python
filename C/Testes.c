#include <stdio.h>
#include <stdlib.h>

// Algoritmo que entrega um bonus ao colaborador se ele tiver x horas
// extras somadas no mes. Valor da bonificação será de +20%
// do salário desse funcionário.


int main(){
    int salario;
    int horaX;
    int bonus = 20;
    int bonus1 = 100;

    printf("'Primeiro' - DIGITE O SEU SALARIO\n'Segundo' - QUANTIDADE DE HORAS EXTRAS.\n");
    scanf("%d", &salario);
    scanf("%d", &horaX);
    //printf("Seu salario e de %d reais e seu saldo de horas mensais extras e de %d horas.\n", salario, horaX);

    if(horaX >= 20){
        printf("\nBonus adicionado. Valor total: %d", salario + salario * bonus / bonus1);
    }else if(horaX < 20){
        printf("\nBonus negado. Seu banco de horas e menor que 20horas extras mensais.");
    }

return 0;
}
