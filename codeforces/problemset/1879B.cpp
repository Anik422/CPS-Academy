#include <bits/stdc++.h>
#define ll long long
using namespace std;

int main()
{
    ll t;
    cin >> t;

    while(t--)
    {
        ll n;
        cin >> n;
        ll arr1[n], arr2[n];
        ll arr1min = LLONG_MAX;
        ll arr2min = LLONG_MAX;
        ll sum1 = 0, sum2 = 0;

        for(ll i = 0; i < n; i++)
        {
            cin >> arr1[i];
            sum1 += arr1[i];
            if(arr1[i] < arr1min)
            {
                arr1min = arr1[i];
            }
        }
        for(ll i = 0; i < n; i++)
        {
            cin >> arr2[i];
            sum2 += arr2[i];
            if(arr2[i] < arr2min)
            {
                arr2min = arr2[i];
            }
        }
        sum1 += (n * arr2min);
        sum2 += (n * arr1min);
        cout << min(sum1, sum2) << endl;
    }

    return 0;
}
