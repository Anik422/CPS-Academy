#include<bits/stdc++.h>
#define ll long long
using namespace std;

int main(){

    ll t, l, r, d;
    cin >> t;
    while(t--){
        cin >> l >> r >> d;
        if(d < l || r < d){
            cout << d << endl;
        }else{
               cout << (((r / d) + 1) * d) << endl;
        }

    }

    return 0;
}
