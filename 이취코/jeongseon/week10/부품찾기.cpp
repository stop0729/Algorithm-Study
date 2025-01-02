//직접 구현

#include <iostream>
#include <vector>
using namespace std;

int n, m;
vector<int> v;
vector<int> test;

string binarySearch(const vector<int>& arr, int target){

    int left = 0;
    int right = arr.size()-1;

    while(left <= right){
        int mid = (left + right) / 2;

        if(target == arr[mid]) return "yes";
        else if(target < arr[mid]){
            right = mid-1;
        }else{
            left = mid +1;
        }
    }

    return "no";
}

int main(){

    cin >> n;

    v.resize(n);

    for(int i=0; i<n; i++){
        cin >> v[i];
    }

    cin >> m;

    test.resize(m);

    for(int i=0; i<m; i++){
        cin >> test[i];
    }

    sort(v.begin(), v.end());  //정렬하기

    for(int i=0; i<m; i++){
        cout << binarySearch(v, test[i]) << " ";
    }


    return 0;
}