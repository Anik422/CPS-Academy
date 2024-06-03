#include<iostream>
#include <algorithm>
using namespace std;


void updateArray(int arr[], int i, int val)
{
    arr[i] = val;
}



void print(int arr[], int n)
{
    for(int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }
    cout << endl;
}


void arraySize(int arr[])
{
    cout << "Array Size in function : " << sizeof(arr) << endl;
    cout << endl;
}

int main()
{
    int arr[] = {1, 5, 4, 3, 2}; // init list
    int n = sizeof(arr) / sizeof(int);
    cout << "Array Size in main : " << sizeof(arr) << endl;
    cout << endl;
    cout << arr << endl;
    arraySize(arr);

    updateArray(arr, 1, 13);
    print(arr, n);
    sort(arr, arr + n);
    print(arr, n);



}
