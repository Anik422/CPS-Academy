#include<bits/stdc++.h>
#include <cmath>
#define ll long long
using namespace std;

int main()
{
    ll t;
    cin >> t;
    while(t--)
    {
        ll n;
        ll ans;
        cin >> n;
        ans = n / 2;
        if (n % 2 == 0)
        {
            cout << ans << endl;
        }
        else
        {
            ans++;
            cout << ans << endl;
        }
    }
    return 0;
}
