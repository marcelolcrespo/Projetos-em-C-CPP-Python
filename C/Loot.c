#include <stdio.h>
#include <stdlib.h>

int main(){
    int waste = 0, loot = 0, players = 0, cont = 1, total = 0, valor = 1, div;

    printf("Digite o numero de jogadores presentes no grupo: \n");
    scanf("%d", &players);
    if(players <= 0){
        printf("Nao existe waste a ser calculado!\n");
    }else{
    for(cont = cont; cont <= players; cont = cont + 1){
        printf("Valor da %d waste: \n", valor);
        valor = valor + 1;
        scanf("%d", &waste);
        total = total + waste;
    }
    printf("Agora digite o valor do loot da hunt completa: \n");
    scanf("%d", &loot);
    if(loot < total){
            //div = total - loot;
        printf("\t\nWaste\n");
        printf("O loot da hunt foi %d, dividido por %d players = %d", loot, players, loot / players);
    }else if(loot > total){
            div = loot - total;
        printf("\t\nProfit\n");
        printf("\nTotal da waste do grupo: %d\n", total);
        printf("\nO numero de players na PT foi de %d\nValor total de Gold foi de %d\n", players, loot);
        printf("\nO loot total - a waste somada = %d\n", div);
        printf("\nCada player recebera %d Golds\n", div / players);
    }else if(loot == total){
            div = loot - total;
        printf("\t\nProfit - Loot igual ao waste\n");
        printf("\nTotal da waste do grupo: %d\n", total);
        printf("\nO numero de players na PT foi de %d\nValor total de Gold foi de %d\n", players, loot);
        printf("\nO loot total - a waste somada = %d\n", div);
        printf("\nCada player recebera %d Golds\n", div / players);
    }
}
return 0;
}
