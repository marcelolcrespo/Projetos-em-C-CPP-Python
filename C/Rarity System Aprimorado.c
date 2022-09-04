#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <windows.h>

//Sistema feito para calcular quantidade de sucatas/pó's necessários para poder aumentar a raridade de itens
// Primeira ideia do sistema. Será repensado com uma base mais limpa nos calculos de tiers.

void receberValores(); // Recebe os primeiros valores para calculo
void calculoSucatas(); // Calcula os valores recebidos
void reciclarItems();  // Calcular quantidade de sucatas e pó ao reciclar items
void boostRarity();    // Calcula o recurso necessário para avançar o próximo nível
void menuInicial();    // Menu que puxa as duas funções quando acionadas

int tierGlobal[7];     // Guarda o valor de cada tier dentro de um vetor global para repassar para outra função
int range;             // Guarda o valor de até onde o player irá calcular as sucatas

int main(){
    setlocale(LC_ALL, ""); // forçar acentuação PT-BR
    menuInicial(); // chamar menu
    calculoSucatas();
return 0;
}

void reciclarItems(){
    int branco, raro, epico, mitico, lendario, sucatas=0;
    printf("\nQuantos itens Brancos você possui: ");
    scanf("%d", &branco);
    printf("\nQuantos itens Raros você possui: ");
    scanf("%d", &raro);
    printf("\nQuantos itens Épicos você possui: ");
    scanf("%d", &epico);
    printf("\nQuantos itens Míticos você possui: ");
    scanf("%d", &mitico);
    printf("\nQuantos itens Lendários você possui: ");
    scanf("%d", &lendario);

    printf("Loading...\n");
    system("pause");
    printf("Pó Raro: %d\n", raro * 9);
    printf("Pó Épico: %d\n", epico * 6);
    printf("Pó Mítico: %d\n", mitico * 4);
    printf("Pó Lendário: %d\n", lendario * 2);
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
    int tier[7],i,valor=0; // vetor Tier armazenará os valores dos tiers. a var Valor é apenas um subcontador para os níveis.
    int tierRange; // receberá o tier a ser atingido.
    printf("\nQual tier você deseja atingir?\n");
    scanf("%d", &tierRange);

    if(tierRange>=8){
        printf("\nO limite de tier ingame é 7. Portanto, digite um valor igual ou menor que 7!\n");
    }
    else if(tierRange<=0){
        printf("Valor inválido!!\n\n");
    }
    else if(tierRange==1){
        printf("O valor precisa ser maior que 1 para ser calculado!!\n\n");
    }else{
        printf("\nDigite na sequência a quantidade de cada item de tier que você tem: ");
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
            printf("Você possui: %d sucatas T-%d\n", tierGlobal[i], valor);
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
    printf("Escolha uma das opções: \n\n");
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
        printf("Comando inválido!!");
    }
    goto inicio;
return 0;
}
