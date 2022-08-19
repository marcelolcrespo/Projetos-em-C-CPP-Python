#include <iostream>
#include <windows.h>
#include <stdlib.h>
#include <stdio.h>

using namespace std;

int main(){
    int claim = 0, resp, c = 0; // [Claim] Variavel que vai ser lida no switch // [Resp] Vai receber o valor de claim (V - 1/ F - 0)
    int s = 0, m = 0, h = 0, timer = 0;
    char alt;

        inicio: // Goto - Reset no claimed. [START]

    cout << "Escolha primeiro a hunt: \n";
    cout << "\n\t[1]Earth Elemental \n\t[2]Fire Elemental \n\t[3]Water Elemental \n\t[4]Wind Elemental\n\n";
    cin >> claim;
    if(claim == resp){ // Multiplayer Check - Se alguem estiver usando o respaw, vai retornar erro:
        cout << "Alguem esta utilizando o respaw no momento\n";
        cout << "Faltam " << 2 - timer << " horas para acabar a hunt!\n";
    }else{
    switch(claim){
    case 1:
        cout << "\nVoce pegou o respaw [1]Earth Elemental. O tempo de hunt comecara a correr em 1 minuto\n\n";
        Sleep(3000); // 60s Sleep - Timer para startar a contagem no claimed
        system("cls"); // refresh no terminal
        resp = claim; // atribuir o valor do claimd para o respaw
        claim = 0; // liberar var claimed
        break;
    case 2:
        cout << "\nVoce pegou o respaw [2]Fire Elemental. O tempo de hunt comecara a correr em 1 minuto\n\n";
        Sleep(3000); // 60s Sleep - Timer para startar a contagem no claimed
        system("cls"); // refresh no terminal
        resp = claim; // atribuir o valor do claimd para o respaw
        claim = 0; // liberar var claimed
        break;
    case 3:
        cout << "\nVoce pegou o respaw [1]Water Elemental. O tempo de hunt comecara a correr em 1 minuto\n\n";
        Sleep(3000); // 60s Sleep - Timer para startar a contagem no claimed
        system("cls"); // refresh no terminal
        resp = claim; // atribuir o valor do claimd para o respaw
        claim = 0; // liberar var claimed
        break;
    case 4:
        cout << "\nVoce pegou o respaw [1]Wind Elemental. O tempo de hunt comecara a correr em 1 minuto\n\n";
        Sleep(3000); // 60s Sleep - Timer para startar a contagem no claimed
        system("cls"); // refresh no terminal
        resp = claim; // atribuir o valor do claimd para o respaw
        claim = 0; // liberar var claimed
        break;
    default:
        cout << "Opcao invalida!\n"; // Digitar valor que nao consta no menu - break;
    }
    if(claim > 4){
        cout << "\nParece que voce digitou um valor invalido. \nRetorne ao menu\n";
        goto inicio;
    }else{
    while(c < 10){
        Sleep(1000);
        system("cls");
        s++;
        cout << "Horas rodando: " << timer << "\n";
        cout << "Respaw cod: " << resp << "\n";
        cout << "Para alterar o respaw digite [s]\n";
        cout << "\n\t" << h << " : " << m << " : " << s << "\n";
            if(s == 60){
                s = 0;
                m++;
            }
            if(m == 60){
                m = 0;
                h++;
            }
            if(h == 60){
                h = 0;
                timer++;
            }
            if(h == 2){
                    cout << "Voce cacou por " << timer << " horas.\n";
                    cout << "Seu tempo no respaw acabou!\n";
                    resp = 0;
                    claim = 0;
                    goto inicio;
                break;
                    }
                }
        if(alt == 's' || alt == 'S'){
        claim = 0;
        resp = 0;
        goto inicio;
            }
        }
    }
    return 0;
}
