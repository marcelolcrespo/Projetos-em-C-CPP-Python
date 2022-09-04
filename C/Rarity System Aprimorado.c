#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <windows.h>

//Sistema feito para calcular quantidade de sucatas/p�'s necess�rios para poder aumentar a raridade de itens
// Primeira ideia do sistema. Ser� repensado com uma base mais limpa nos calculos de tiers.

void receberValores(); // Recebe os primeiros valores para calculo
void calculoSucatas(); // Calcula os valores recebidos
void reciclarItems();  // Calcular quantidade de sucatas e p� ao reciclar items
void boostRarity();    // Calcula o recurso necess�rio para avan�ar o pr�ximo n�vel
void menuInicial();    // Menu que puxa as duas fun��es quando acionadas

int tierGlobal[7];     // Guarda o valor de cada tier dentro de um vetor global para repassar para outra fun��o
int range;             // Guarda o valor de at� onde o player ir� calcular as sucatas

int main(){
    setlocale(LC_ALL, ""); // for�ar acentua��o PT-BR
    menuInicial(); // chamar menu
    calculoSucatas();
return 0;
}

void reciclarItems(){
    int branco, raro, epico, mitico, lendario, sucatas=0;
    printf("\nQuantos itens Brancos voc� possui: ");
    scanf("%d", &branco);
    printf("\nQuantos itens Raros voc� possui: ");
    scanf("%d", &raro);
    printf("\nQuantos itens �picos voc� possui: ");
    scanf("%d", &epico);
    printf("\nQuantos itens M�ticos voc� possui: ");
    scanf("%d", &mitico);
    printf("\nQuantos itens Lend�rios voc� possui: ");
    scanf("%d", &lendario);

    printf("Loading...\n");
    system("pause");
    printf("P� Raro: %d\n", raro * 9);
    printf("P� �pico: %d\n", epico * 6);
    printf("P� M�tico: %d\n", mitico * 4);
    printf("P� Lend�rio: %d\n", lendario * 2);
    sucatas = sucatas + raro + epico + mitico + lendario + branco; // Calculo de sucatas ao reciclar items
    printf("\n\n\tSucatas: %d\n", sucatas * 12);
    system("pause");
    system("cls");
return 0;
}

void boostRarity(){

return 0;
}

void receberValores(){
    int tier[7],i,valor=0; // vetor Tier armazenar� os valores dos tiers. a var Valor � apenas um subcontador para os n�veis.
    int tierRange; // receber� o tier a ser atingido.
    printf("\nQual tier voc� deseja atingir?\n");
    scanf("%d", &tierRange);

    if(tierRange>=8){
        printf("\nO limite de tier ingame � 7. Portanto, digite um valor igual ou menor que 7!\n");
    }
    else if(tierRange<=0){
        printf("Valor inv�lido!!\n\n");
    }
    else if(tierRange==1){
        printf("O valor precisa ser maior que 1 para ser calculado!!\n\n");
    }else{
        printf("\nDigite na sequ�ncia a quantidade de cada item de tier que voc� tem: ");
        for(i=0;i<tierRange;i++){
            valor++;
            printf("\nT-%d:", valor);
            scanf("%d", &tier[i]);
            tierGlobal[i]=tier[i];
        }
    valor=0;
        for(i=0;i<tierRange;i++){
            valor++;
            printf("\n");
            printf("Voc� possui: %d sucatas T-%d\n", tierGlobal[i], valor);
        }
    }
    range = tierRange;
    system("pause");
    system("cls");
return 0;
}

void calculoSucatas(){
    int tier[7],i,tierRange2;
    tierRange2 = range;
    for(i=0;i<tierRange2;i++){
        tier[i]=tierGlobal[i];
    }

    for(i=0;i<tierRange2;i++){
        printf("%d\n", tier[i]);
    }
return 0;
}

void menuInicial(){
    int escolha, inicio; // menu & goTo
    inicio:
    printf("Escolha uma das op��es: \n\n");
    printf("\t[1]-- Calcular a partir de um tier mais baixo\n\t[2]-- Reciclar items\n\t[3]-- Calcular items para boostar raridade items");
    printf("\n\n\tAguardando...\n");
    scanf("%d", &escolha);
    if(escolha==1){
        printf("Loading...");
        receberValores();
    }
    else if(escolha==2){
        printf("Loading...");
        reciclarItems();
    }
    else if(escolha==3){
        printf("Building...\n");
    }else{
        printf("Comando inv�lido!!");
    }
    goto inicio;
return 0;
}
