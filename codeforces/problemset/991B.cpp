#include<bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;
    int m[n], i, sum = 0, ans = 0;
    for(i=0; i<n; i++)
    {
        cin >> m[i];
        sum += m[i];
    }
    if(sum / (1.0 * n) >= 4.5)
    {
        cout << ans << endl;
    }
    else
    {
        sort(m, m + n);
        for(i=0; i<n; i++)
        {
            sum += (5 - m[i]);
            ans += 1;
            if(sum / (1.0 * n) >= 4.5)
            {
                cout << ans << endl;
                break;
            }

        }
    }


    return 0;
}
