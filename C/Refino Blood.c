#include <stdio.h>
#include <stdlib.h>

int main(){
    float atk, soma, upgrade, porcentagem, rare, decimal,decimalbase;
        int i, cont = 0; // Contadores
    printf("Digite o valor da arma a ser calculada: "); // Recebe o valor de dano da arma
        scanf("%f", &atk);
    printf("Quantos upgrades voce quer fazer nesse item? "); // Recebe o numero de refinos
        scanf("%f", &upgrade);
    printf("Qual a porcentagem da arma [Raridade]: "); // Recebe o bonus de dano da arma [Raridade]
        scanf("%f", &rare);
    porcentagem=rare; // Passa o valor da var rare para a var porcentagem para fazer a condicional
    rare=(atk*rare)/100;
    atk=atk+rare; // calculo do atk base + bonus de raridade
    decimalbase= atk-(int)atk; // função para remover o valor decimal do valor da raridade
    atk=atk-decimalbase;       // remove o valor decimal da var atk, tornando-o inteiro
    //printf("%f\n", decimalbase);
        if(porcentagem>=2 && porcentagem<=4){ // condicional com range dos valores de cada raridade
            printf("Arma Rara!\n");
            printf("Ataque base: %.2f\n\n", atk);
        }else if(porcentagem>=5 && porcentagem<=7){ // {rara 2~4 -- epica 5~7 -- mitica 8~11 -- lendaria 12~15}
            printf("Arma Epica!\n");
            printf("Ataque base: %.2f\n\n", atk);
        }else if(porcentagem>=8 && porcentagem<=11){
            printf("Arma Mitica!\n");
            printf("Ataque base: %.2f\n\n", atk);
        }else if(porcentagem>=12 && porcentagem<=15){
            printf("Arma Lendaria!\n");
            printf("Ataque base: %.2f\n\n", atk);
        }else{
            printf("Raridade nao encontrada.\n\n");
        }
        for(i=0;i<upgrade;i++){ // for para fazer o calculo do refino do item. Será atribuido +5% do refino a cada volta do loop
            soma=(atk*5)/100;       // soma o ataque + 5% do bonus de refino
            atk=atk+soma;           // repassa o valor de atk + bonus para var Atk
            cont++;                 // Contador de refinos
            decimal = atk-(int)atk; // função que checa os numeros reais
                if(decimal>=0.01){ // Se tiver numero decimal, remove-lo e somar +1 ao ataque (Arredondar pra cima)
                    atk=atk-decimal; // remover o valor decimal da var atk
                    atk=atk+1; // adicionar +1 (Arredondar pra cima)
                }
            printf("Ataque +%d: %.2f\n", cont, atk); // imprimir o calculo final do refino
        }
    return 0;
}
