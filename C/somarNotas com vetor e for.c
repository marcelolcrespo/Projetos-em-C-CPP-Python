#include <stdio.h>
#include <stdlib.h>

int main(){ // Sistema de somatório de notas através de um vetor
    float nota[3], media; // vetor que recebe as notas

    for(int i=0;i<3;i++){ // Loop para rodar 3x ( tamanho do vetor nota)
        printf("Digite uma nota: ");
        scanf("%f", &nota[i]);
        media += nota[i]; // somatorio das notas
    }
    media = media / 3; // tirar o valor medio
    printf("%.2f\n", media); // mostrar o valor final
return 0;
}

    //printf("\t%f\n\n", media);  - print para conferir se está somando
