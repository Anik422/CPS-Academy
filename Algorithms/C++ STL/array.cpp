#include<iostream>
#include<array>
#include<algorithm>

using namespace std;

void print(const array<int, 6> arr){
    int n = arr.size();
    for(int i = 0; i < n; i++){
        cout << arr[i] << ",";
    }
    cout << endl;
}


void arrayUpdateDuplicate(array<int, 6> arr, int i, int val){
    arr[i] = val;
    print(arr);
    cout << "Duplicate update before print .." << endl;
}

void arrayUpdateMain(array<int, 6> &arr, int i, int val){
    arr[i] = val;
    print(arr);
    cout << "Main update before print .." << endl;
}




int main(){

    array<int, 6> arr = {1, 2, 3,  16, 70, 8};
    print(arr);
    arrayUpdateDuplicate(arr, 0, 30);
    print(arr);
    arrayUpdateMain(arr, 0, 100);
    print(arr);
    sort(arr.begin(), arr.end());
    print(arr);

    array <int, 6> nullArra;
    nullArra.fill(0);
    print(nullArra);
    for(const int x : nullArra){
        cout << x << " ,";
    }
    cout << endl;



    return 0;
}
