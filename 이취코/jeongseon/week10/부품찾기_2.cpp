//binary_search 사용해서 해결하기 (O(logn))

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int n, m;
vector<int> arr;
vector<int> test;

int main(){

    cin >> n;
    arr.resize(n);
    for(int i=0; i<n; i++){
        cin >> arr[i];
    }

    cin >> m;
    test.resize(m);
    for(int i=0; i<m; i++){
        cin >> test[i];
    }

    sort(arr.begin(), arr.end());

    for(int i=0; i<m; i++){
        bool ret = binary_search(arr.begin(), arr.end(), test[i]);       //해당 값 찾으면 true, 못찾으면 false

        if(ret) cout << "yes" << " ";
        else cout << "no" << " ";
    }


    return 0;
}