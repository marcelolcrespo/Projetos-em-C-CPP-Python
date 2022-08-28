#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <windows.h>


//void valorArma();
void raridadeAtk();
void porcentagemBonus();
void refinoUpgrade();
void menuInicial();

float atk;          // var que guarda o dano do item
float raridade;     // var que guarda o valor do item com atk bonus (item com raridade)

int main(){
    setlocale(LC_ALL, ""); // Forçar o compilador a aceitar acentuações no programa.

    menuInicial();

return 0;
}
// Receber o valor do item base
/*void valorArma(){
    printf("Digite o ataque do item: ");
    scanf("%f", &atk);
    printf("%.2f", atk);
return 0;
}*/

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
    a = atk;        // var A recebe o valor da var global Atk
    b = raridade;   // var B recebe o valor da var global Raridade
    resultado = (b-a)/a; // calculo para saber a porcentagem do item (bonus da raridade)
    resultado = resultado*100;
    printf("\nPorcentagem: %.2f\n", resultado);
    if(resultado<1,5 && resultado<=4){          // Condicional para identificar o nivel de raridade do item
        printf("\nArma Rara!\n\n");
    }else if(resultado<4,5 && resultado<=7){
        printf("\nArma Épica!\n\n");
    }else if(resultado<7,5 && resultado<=11){
        printf("\nArma Mítica!\n\n");
    }else if(resultado==11,5 && resultado<=15){
        printf("\nArma Lendária!\n\n");
    }else{
        printf("\nValor não encontrado\n");
    }
return 0;
}
// Função que calcula o refino do item.
void refinoUpgrade(){
    float upgrade, arma, decimal, calculo;
    int i, cont = 0; // Contadores
    arma = raridade; // var Arma recebe o valor da var global Raridade.
    printf("\nDigite a quantidade de refinos que deseja adicionar no item: ");
    scanf("%f", &upgrade);              // input de nivel de refino
        for(i=0;i<upgrade;i++){         // loop para calular refino
            calculo = (arma*5)/100;     // calculo adicionando +5% a cada refino
            arma = arma + calculo;
            cont++;
            decimal = arma-(int)arma;   // remove o valor inteiro da arma, deixando o valor real guardado na var Decimal
            if(decimal>=0.01){          // condicional para checar os valores reais. Se tiver, o programa deve remove-los
                arma = arma - decimal;
                arma = arma + 1;        // Apos a remoção, arredondar a var Arma pra cima somando +1 no valor final
            }
        printf("Ataque +%d: %.2f\n", cont, arma); // Atualizar o valor do Dano do item dentro do for + contador
    }
return 0;
}
// Menu principal - Esse menu contém as funções presentes no programa. Será utilizada na medida que o usuario solicitar
void menuInicial(){
    int escolha, inicio;
    inicio:
    printf("\n\n\tVamos iniciar!!\n");
    printf("\tLoading...\n");
    printf("\t\nPreencha as próximas perguntas:\n\n");
    raridadeAtk();                          // chamando a função que recebe os valores
    printf("\n\tOK!!\n");
    printf("Escolha uma das opções: \n"); // Menu de opções
    printf("\t==[1]== Para saber o dano do item refinado (+1 ~ +9).\n"); // Menu de opções
    printf("\t==[2]== Para saber a porcentagem do seu item.\n");         // Menu de opções
    scanf("%d", &escolha);
    if(escolha==1){
        printf("Você escolheu saber sobre o refino do seu item!");
        refinoUpgrade(); // Chama a função que calcula o refino
    }else if(escolha==2){
        printf("Você escolheu saber sobre a porcentagem do seu item!");
        porcentagemBonus(); // Chama a função que calcula o bonus de raridade do item
    }else{
        printf("\nEscolha inválida!!\n\n");
    }
    system("pause");
    system("cls");
    goto inicio;
return 0;
}
