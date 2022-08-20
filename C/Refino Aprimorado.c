#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <windows.h>


void valorArma();
void raridadeAtk();
void porcentagemBonus();
void refinoUpgrade();
void menuInicial();

float atk;
float refino;
float raridade;
float porcentagem;

int main(){
    setlocale(LC_ALL, ""); // Forçar o compilador a aceitar acentuações no programa.

    menuInicial();

return 0;
}
// Receber o valor do item base
void valorArma(){
    printf("Digite o ataque do item: ");
    scanf("%f", &atk);
    printf("%.2f", atk);
return 0;
}

// Receber os valores base do item e do item com rare. Atk base ~ atk do item colorido
void raridadeAtk(){ // Será sempre a primeira função a ser chamada pois será imprescindível receber os 2 valores abaixo!!
    printf("Digite o valor de ataque base do item: ");
    scanf("%f", &atk);
    printf("Digite o valor de ataque do seu item: ");
    scanf("%f", &raridade);
return 0;
}
// Calcular o valor bonus de atk na arma (raridade)
void porcentagemBonus(){
    float a, b, resultado;
    a = atk;
    b = raridade;
    resultado = (b-a)/a;
    resultado = resultado*100;
    printf("\nPorcentagem: %.2f\n", resultado);
    if(resultado<1,5 && resultado<=4){
        printf("\nArma Rara!\n");
    }else if(resultado<4,5 && resultado<=7){
        printf("\nArma Épica!\n");
    }else if(resultado<7,5 && resultado<=11){
        printf("\nArma Mítica!\n");
    }else if(resultado==11,5 && resultado<=15){
        printf("\nArma Lendária!\n");
    }else{
        printf("\nValor não encontrado\n");
    }
return 0;
}

void refinoUpgrade(){
    float upgrade, arma, decimal, calculo;
    int i, cont = 0;
    arma = raridade;
    printf("\nDigite a quantidade de refinos que deseja adicionar no item: ");
    scanf("%f", &upgrade);
        for(i=0;i<upgrade;i++){
            calculo = (arma*5)/100;
            arma = arma + calculo;
            cont++;
            decimal = arma-(int)arma;
            if(decimal>=0.01){
                arma = arma - decimal;
                arma = arma + 1;
            }
        printf("Ataque +%d: %.2f\n", cont, arma);
    }
return 0;
}

void menuInicial(){
    int op1 = 1, op2 = 2, escolha, inicio;
    inicio:
    printf("\n\n\tVamos iniciar!!\n");
    printf("\tLoading...\n");
    printf("\t\nPreencha as próximas perguntas:\n\n");
    raridadeAtk();
    printf("\n\tOK!!\n");
    printf("Escolha uma das opções: \n");
    printf("\t==[1]== Para saber o dano do item refinado (+1 ~ +9).\n");
    printf("\t==[2]== Para saber a porcentagem do seu item.\n");
    scanf("%d", &escolha);
    if(escolha==1){
        printf("Você escolheu saber sobre o refino do seu item!");
        refinoUpgrade();
    }else if(escolha==2){
        printf("Você escolheu saber sobre a porcentagem do seu item!");
        porcentagemBonus();
    }else{
        printf("\nEscolha inválida!!\n\n");
    }
    system("pause");
    system("cls");
    goto inicio;
return 0;
}
