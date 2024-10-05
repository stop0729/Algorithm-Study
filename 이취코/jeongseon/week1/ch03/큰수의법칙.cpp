#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

//M : 더하는 횟수
//k : 같은 인덱스 숫자 연속해서 더하는 한계
//인덱스가 다른데 같은 숫자는 서로 다른 것으로 간주

//1억 = 1초

int n, m, k, sum;
vector<int> v;

int main(){

    cin >> n >> m >> k;

    for(int i=0; i<n; i++){
        int num;
        cin >> num;
        v.push_back(num);
    }

    //정렬하기
    sort(v.begin(), v.end(), greater<>());

    int tmpCnt=0, totalCnt=0;
    while(true){
        if(totalCnt == m ) break;
        if(tmpCnt == k){
            tmpCnt=0;   //초기화
            totalCnt++;
            sum += v[1];
        }else{
            sum += v[0];
            tmpCnt++;
            totalCnt++;
        }
    }

    cout << sum << "\n";

    return 0;
}