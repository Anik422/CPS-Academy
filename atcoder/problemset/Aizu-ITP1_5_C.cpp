#include<bits/stdc++.h>
using namespace std;

int main()
{

    int h, w, i, j;
    while(true)
    {
        cin >> h >> w;
        if(h==0 && w == 0) break;
        for(i = 1; i<=h; i++)
        {
            for(j=1; j<=w; j++)
            {
                if(i % 2 != 0)
                {
                    if(j % 2 != 0) cout << "#";
                    else cout << ".";
                }
                else
                {
                    if(j % 2 != 0) cout << ".";
                    else cout << "#";
                }

            }
            cout << endl;
        }
        cout << endl;
    }


    return 0;
}



