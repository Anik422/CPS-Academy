#include<bits/stdc++.h>
using namespace std;

bool compare(const pair<int, int> & a, const pair<int, int> & b)
{
    return a.second < b.second;
}

int main()
{
    int n, k,w;
    cin >> n >> k;
    map<int, int> m;
    for(int i = 0; i<n; i++)
    {
        cin >> w;
        if(m[w])
        {
            m[w]++;
        }
        else
        {
            m[w] = 1;
        }
    }
    int maxn = max_element(m.begin(), m.end(), compare)->second;
    if(maxn % k != 0)
    {
        maxn += k- (maxn % k);
    }
    int ans = 0;
    for (const auto& x : m)
    {
        ans += maxn - x.second;
    }
    cout << ans << endl;

    return 0;
}
