#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int n;
vector<int> v;
int main(){

    cin >> n;

    for(int i=0; i<n; i++){
        int a;
        cin >> a;
        v.push_back(a);
    }

    sort(v.begin(), v.end(), greater());   //less는 오름차순

    for(int i: v){
        cout << i << "\n";
    }


    return 0;
}