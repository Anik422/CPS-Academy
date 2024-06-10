#include<bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin >> t;
    while(t--)
    {
        int n, m, i;
        cin >> n >> m;
        int xy[m][2];
        for(i = 0; i < m; i++)
        {
            cin >> xy[i][0] >> xy[i][1];
        }
        bool ok = true;
        for(i=0; i<m; i++){
            for(int j=i+1; j<m; j++){
                if(xy[i][0] + xy[j][0] == xy[i][1] + xy[j][1]){
                    ok = false;
                    break;
                }
            }
            if(!ok){
                break;
            }
        }
        if(ok){
            cout << "YES" << endl;
        }else{
            cout << "NO" << endl;
        }

    }

    return 0;
}
