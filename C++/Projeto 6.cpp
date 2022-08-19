#include <iostream>

using namespace std;

int main(){
    float a, b, media = 0, base = 7;

    cout << "Digite a sua primeira nota: \n"; // input + leitura primeira nota
    cin >> a;
    cout << "Digite a sua segunda nota: \n"; // input + leitura segunda nota
    cin >> b;
    media = (media + a + b) / 2;       // calculo media final
    if(media >= base){
        cout << "Aprovado!\n";
        cout << "Media final: \n";
        cout << media;
    }else{
        cout << "Reprovado!\n";
        cout << "Media final: \n";
        cout << media;
    }
    return 0;
}
