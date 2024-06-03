#include<bits/stdc++.h>
using namespace std;

int main(){

    int a, b;
    char ch;
    while(1){
        cin >> a >> ch >> b;
        if(ch == '+'){
            cout << a + b << endl;
        }else if (ch == '-'){
            cout << a - b << endl;
        }else if (ch == '*'){
            cout << a * b << endl;
        }else if (ch == '/'){
            cout << a / b << endl;
        }else{
            break;
        }
    }

    return 0;
}
