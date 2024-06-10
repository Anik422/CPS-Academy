#include<bits/stdc++.h>
#define ll long long
using namespace std;

int main(){
    int n, mx, x, y;
    cin >> n;
    mx = 0;
    while(n--){
        cin >> x >> y;
        mx = max(x+y, mx);
    }
    cout << mx << endl;
    return 0;
}
