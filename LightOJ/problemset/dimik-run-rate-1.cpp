#include<bits/stdc++.h>
#include <iomanip>
using namespace std;


int main()
{
    int t;
    cin >> t;
    while(t--)
    {
        int r1, r2, b; cin >>r1>>r2>>b; float cr, rr; cr = r2/((300-b)/6.0);
        if(r1<r2) rr=0.00;
        else rr =((r1-r2+1.0)/(b/6.0));
        std::cout << std::fixed << std::setprecision(2) << cr << " " << rr << std::endl;

    }
}
