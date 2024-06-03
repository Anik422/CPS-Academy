#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main() {
    ll t;
    cin >> t;
    while (t--) {
        ll n;
        cin >> n;
        if(n == 1){
            cout << 1 << endl;
            continue;
        } else if (n == 2){
            cout << 2 << endl;
            continue;
        }
        for(ll i = 1; i<=n; i++){
            if(n % i != 0){
                cout << i -1 << endl;
                break;
            }
        }
    }
    return 0;
}
