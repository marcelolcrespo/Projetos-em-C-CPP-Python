#include <iostream>
#include <cstdlib>

using namespace std;

int main(){
    int valor;
    char opc;

    inicio:
    cout << "Digite o numero de jogadores a ser sorteado: ";
    cin >> valor;

    valor = rand()%valor;
    if(valor == 0){
        cout << "Valor encontrado foi igual a 0 ou invalido. Resetando o programa.\n";
        goto inicio;
    }else{
    cout << valor << "\n";

    cout << "Deseja rodar outra vez? [s/n] ";
    cin >> opc;
    }

    if(opc == 's' || opc == 'S'){
        goto inicio;
    }
    return 0;
}
