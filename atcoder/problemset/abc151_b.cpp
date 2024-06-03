#include<bits/stdc++.h>
using namespace std;

int main()
{

    int n, k, m, sum = 0;
    cin >> n >> k >> m;
    int nums[n];
    for(int i = 0; i<n-1; i++)
    {
        cin >> nums[i];
        sum += nums[i];
    }
    if(sum / n >= m) cout << 0 << endl;
    else{
        int p = (n * m) - sum;
        if(p <= k) cout << p <<endl;
        else cout << -1 << endl;

    }


    return 0;
}




