#include<bits/stdc++.h>
using namespace std;

int main(){

    int t;
    cin >> t;
    while(t--){
        int n, f, l;
        cin >> n;
        f = n % 10;
        n /= 10;
        while(n > 9){
            n /= 10;

        }
        l = n;
        cout << l + f << endl;
    }


    return 0;
}
