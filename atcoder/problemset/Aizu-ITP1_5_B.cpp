#include<bits/stdc++.h>
using namespace std;

int main()
{

    int h, w, i, j;
    while(true)
    {
        cin >> h >> w;
        if(h==0 && w == 0) break;
        for(i = 0; i<h; i++)
        {
            for(j=0; j<w; j++)
            {
                if(i == 0 or i ==h-1 or j == 0 or j == w-1)cout << "#";
                else cout << ".";
            }
            cout << endl;
        }
        cout << endl;
    }


    return 0;
}


