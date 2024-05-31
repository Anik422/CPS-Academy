
#include <bits/stdc++.h>
#define int long long
using namespace std;

void main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        int a[n + 1], b[n + 1], ans = 0, mx = 0;
        for (int i = 0; i < n; i++)
        {
            cin >> a[i];
            mx = max(a[i], mx);
        }
        for (int i = 0; i <= n; i++)
        {
            cin >> b[i];
        }
        a[n + 1] = -1;
        int lest = b[n + 1];
        bool ok = true;
        for (int i = 0; i < n; i++)
        {
            if (ok == true && lest >= b[i] && lest <= a[i])
            {
                ans++;
                ok = false;
            }
            else
            {
                ans += abs(b[i] - a[i]);
            }
        }
        if (ok == true)
        {
            ans += abs(b[n + 1] - mx) + 1;
        }
        cout << ans << endl;
    }
}
