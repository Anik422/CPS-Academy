#include<bits/stdc++.h>
using namespace std;

int main(){

    int n, i;
    cin >> n;
    int num[n];
    for(i=0; i<n; i++) cin >> num[i];

    int nums2[n];
    for(i=0; i<n; i++){
        num2[num[i]-1] = i+1;
    }
    for(i=0; i<n; i++){
        cout <<num[i] << " ";
    }
    cout << endl;



    return 0;
}
