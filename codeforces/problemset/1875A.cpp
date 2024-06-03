#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main()
{
    ll t, n, a, b, i, j, mn;
    cin >> t;
    while (t--)
    {
        cin >> a >> b >> n;
        ll ans = b;
        for (i = 0; i < n; i++)
        {
            cin >> j;
            ans += min(a-1, j);
        }
        cout << ans << endl;
    }

    return 0;
}
