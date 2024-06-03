#include<bits/stdc++.h>
using namespace std;

int main(){

    int n, mx, mn, sum, i, m;
    cin >> n;
    mx = INT_MIN;
    mn = INT_MAX;
    sum = 0;
    for(i = 0; i < n; i++){
            cin >> m;
        if(mx < m){
            mx = m;
        }
        if(mn > m){
            mn = m;
        }
        sum += m;
    }
    cout << mn << " " << mx << " " << sum << endl;


    return 0;
}
