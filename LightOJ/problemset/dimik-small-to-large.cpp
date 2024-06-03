#include<bits/stdc++.h>
using namespace std;

int main(){

    int t, n1,n2, n3;
    cin >> t;
    while(t--){
        cin >> n1 >> n2 >> n3;
        int mx = max(n1, n2, n3);
        int mn = min(n1, n2, n3);
        if(mn == n1 && mx == n3) cout << n1 << " " << n2 << " " << n3 << endl;
        else if(mn == n1 && mx == n2) cout << n1 << " " << n3 << " " << n2 << endl;
        else if(mn == n2 && mx == n1) cout << n2 << " " << n3 << " " << n1 << endl;
        else if(mn == n2 && mx == n3) cout << n2 << " " << n1 << " " << n3 << endl;
        else if(mn == n3 && mx == n1) cout << n3 << " " << n2 << " " << n1 << endl;
        else if(mn == n3 && mx == n2) cout << n3 << " " << n1 << " " << n2 << endl;

    }



    return 0;
}




