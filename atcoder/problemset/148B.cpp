#include<bits/stdc++.h>
#define ll long long


using namespace std;

int main()
{

    ll a, b, k, tem1, tem2;
    cin >> a >> b >> k;
    tem1 = k - a;
    tem2 = k - tem1;
    if (k >= a){
        if (tem2 <= 0){
            tem2 = 0;
        }
        cout << 0 << " " << tem2 << endl;
    }else{
        tem1 = a-k;
        cout << tem1 << " " << b << endl;
    }



    return 0;
}
