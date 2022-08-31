#include <stdio.h>
#include <stdlib.h>
        //Uma empresa necessita de um programa que simule uma calculadora
        // para poder ajudar o setor financeiro a realizar as operações triviais (soma, subtração, multiplicação e divisão).
        //É importante que a calculadora calcule de forma simultânea todas as quatro operações e exiba os seus respectivos valores.

int main(){
        //variaveis
    float a, b;
        //titulo & inicio do programa
    printf("Esse programa realiza operacoes simultaneas.\n");
    printf("Vamos comecar! \nDigite o primeiro valor: \n");
        //input ao usuario 01
    scanf("%f", &a);
        //input ao usuario 02
    printf("Digite o segundo valor: \n");
    scanf("%f", &b);
        //Resultado de para cada operacao
    printf("A soma dos valores e: %.2f\n", a + b);
    printf("A subtracao dos valores e: %.2f\n", a - b);
    printf("A divisao dos valores e: %.2f\n", a / b);
    printf("A multiplicacao dos valores e: %.2f\n", a * b);
    return 0;
}
