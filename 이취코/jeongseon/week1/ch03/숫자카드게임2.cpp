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

    int ret=-1;
    for(int i=0; i<n; i++){
        //각 행의 최소 찾기
        int tmp=987654321;
        for(int j=0; j<m; j++){
            tmp = min(tmp, v[i][j]);
        }

        ret = max(ret, tmp);

    }

    cout << ret;


    return 0;
}