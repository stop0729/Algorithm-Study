#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

//안테나는 집이 위치한 곳에만 설치할 수 있다.

int n;
vector<int> v; 


int main(){

    cin >> n;

    v.resize(n); 

    for(int i=0; i<n; i++){
        cin >> v[i];
    }

    sort(v.begin(), v.end());

    int result = n % 2 ==0 ? n / 2 -1 : n / 2;

    cout << v[result];

    return 0;
}