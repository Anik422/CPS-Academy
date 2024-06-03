#include <bits/stdc++.h>
#define ll long long
using namespace std;


ll find_luck(ll m, ll n)
{
    ll ans = 0, mx_val = 0;
    for(ll i = m; i >= n; i--)
    {
        int mx = 0, mn = 9;
        ll num = i;
        while(num > 0)
        {
            int mod = num % 10;
            mx = max(mx, mod);
            mn = min(mn, mod);
            num /= 10;
        }
        if (mx_val == 9) break;
        if(mx_val < (mx - mn))
        {
            mx_val = (mx - mn);
            ans = i;
        }

    }
    return ans;

}


int main()
{
    ll t;
    cin >> t;
    while(t--)
    {
        ll n, m;
        cin >> n >> m;
        if(n <= 9 && m <= 9){
            cout << max(n, m) << endl;
        }
        else if(m-n >= 10)
        {
            cout << find_luck(m, n) << endl;
        }
        else
        {
            cout << find_luck(m, n) << endl;
        }
    }
    return 0;
}
