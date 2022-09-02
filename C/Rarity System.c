#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <windows.h>

//Sistema feito para calcular quantidade de sucatas/pó's necessários para poder aumentar a raridade de itens
// Primeira ideia do sistema. Será repensado com uma base mais limpa nos calculos de tiers.

void calculoValores(); // Calcular recursos de items
void reciclarItems();  // Calcular quantidade de sucatas e pó ao reciclar items
void menuInicial();    // Menu que puxa as duas funções quando acionadas

int main(){
    setlocale(LC_ALL, ""); // forçar acentuação PT-BR
    menuInicial(); // chamar menu
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

void calculoValores(){
    int t1, t2, t3, t4, t5, t6, t7, t8, item; // Var T para receber os valores das sucatas.
    int tier; // receberá o tier a ser atingido.
    printf("\nQual tier você deseja atingir?\n");
    scanf("%d", &tier);
    if(tier==1){
        printf("Tier I\n");
    }
    else if(tier==2){
        printf("Tier II\n");
        printf("Quantos materias de tiers anteriores você possui para evoluir?\n\n");
        printf("T1: ");
        scanf("%d", &t1);
        item = t1/3;
        printf("Quantidade de sucatas feitas T-II: %d\n", item);
    }
    else if(tier==3){
        printf("Tier III\n");
        printf("Quantos materias de tiers anteriores você possui para evoluir?\n\n");
        printf("T-I: ");
        scanf("%d", &t1);
        printf("T-II: ");
        scanf("%d", &t2);
        item = ((t1/3)/3)+(t2/3);
        printf("Quantidade de sucatas feitas T-III: %d\n", item);
    }
    else if(tier==4){
        printf("Tier IV\n");
        printf("Quantos materias de tiers anteriores você possui para evoluir?\n\n");
        printf("T-I: ");
        scanf("%d", &t1);
        printf("T-II: ");
        scanf("%d", &t2);
        printf("T-III: ");
        scanf("%d", &t3);
        item = (((t1/3)/3)/3)+((t2/3)/3)+(t3/3);
        printf("Quantidade de sucatas feitas T-IV: %d\n", item);
    }
    else if(tier==5){
        printf("Tier V\n");
        printf("Quantos materias de tiers anteriores você possui para evoluir?\n\n");
        printf("T-I: ");
        scanf("%d", &t1);
        printf("T-II: ");
        scanf("%d", &t2);
        printf("T-III: ");
        scanf("%d", &t3);
        printf("T-IV: ");
        scanf("%d", &t4);
        item = ((((t1/3)/3)/3)/3)+(((t2/3)/3)/3)+((t3/3)/3)+(t4/3);
        printf("Quantidade de sucatas feitas T-V: %d\n", item);
    }
    else if(tier==6){
        printf("Tier VI\n");
        printf("Quantos materias de tiers anteriores você possui para evoluir?\n\n");
        printf("T-I: ");
        scanf("%d", &t1);
        printf("T-II: ");
        scanf("%d", &t2);
        printf("T-III: ");
        scanf("%d", &t3);
        printf("T-IV: ");
        scanf("%d", &t4);
        printf("T-V: ");
        scanf("%d", &t5);
        item = (((((t1/3)/3)/3)/3)/3)+((((t2/3)/3)/3)/3)+(((t3/3)/3)/3)+((t4/3)/3)+(t5/3);
        printf("Quantidade de sucatas feitas T-VI: %d\n", item);
    }
    else if(tier==7){
        printf("Tier VII\n");
        printf("Quantos materias de tiers anteriores você possui para evoluir?\n\n");
        printf("T-I: ");
        scanf("%d", &t1);
        printf("T-II: ");
        scanf("%d", &t2);
        printf("T-III: ");
        scanf("%d", &t3);
        printf("T-IV: ");
        scanf("%d", &t4);
        printf("T-V: ");
        scanf("%d", &t5);
        printf("T-VI: ");
        scanf("%d", &t6);
        item = ((((((t1/3)/3)/3)/3)/3)/3)+(((((t2/3)/3)/3)/3)/3)+((((t3/3)/3)/3)/3)+(((t4/3)/3)/3)+((t5/3)/3)+(t6/3);
        printf("Quantidade de sucatas feitas T-VII: %d\n", item);
    }
    else{
        printf("Valor não encontrado!");
    }
    system("pause");
    system("cls");
return 0;
}

void menuInicial(){
    int escolha, inicio; // menu & goTo
    inicio:
    printf("Escolha uma das opções: \n\n");
    printf("\t[1]-- Calcular a partir de um tier mais baixo\n\t[2]-- Reciclar items");
    printf("\n\n\tAguardando...\n");
    scanf("%d", &escolha);
    if(escolha==1){
        printf("Loading...");
        calculoValores();
    }
    else if(escolha==2){
        printf("Loading...");
        reciclarItems();
    }else{
        printf("Comando inválido!!");
    }
    goto inicio;
return 0;
}
