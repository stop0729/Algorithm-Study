#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

//행 선택
//같은 행에서 가장 작은 수 택
//그 가장 작은 수가 다른 행 중에 가장 큰 수여야 함

int n, m;
vector<int> v[103];

int main(){

    cin >> n >> m;

    //입력받기
    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++){
            int num;
            cin >> num;
            v[i].push_back(num);
        }
    }

    //내림차순 정렬
    for(int i=0; i<n; i++){
        sort(v[i].begin(), v[i].end());
    }

    int ret= 0;
    for(int i=0; i<n; i++){
        ret = max(ret, v[i][0]);
    }

    cout << ret;

    return 0;
}