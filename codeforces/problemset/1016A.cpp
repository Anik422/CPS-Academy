#include<bits/stdc++.h>
#define ll long long
using namespace std;

int main(){

    ll n, m;
    cin >> n >> m;
    ll d[n], res = 0;
    for(ll i = 0; i < n; i++) cin >> d[i];
    for(ll i = 0; i < n; i ++){
        cout << (res + d[i]) / m << " ";
        res = (res + d[i]) % m;
    }


    return 0;
}
