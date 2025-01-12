#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
using namespace std;

int n, k;
vector<int> A, B;

int main(){

    cin >> n >> k;

    //A 넣기
    for(int i=0; i<n; i++){              //시간복잡도 n
        int a;
        cin >> a;
        A.push_back(a);
    }

    //B 넣기
    for(int j=0; j<n; j++){             //시간복잡도 n
        int b;
        cin >> b;
        B.push_back(b);
    }

    //A는 오름차순
    sort(A.begin(), A.end(), less());      //시간복잡도 nologn
    //B는 내림차순
    sort(B.begin(), B.end(), greater());   //시간복잡도 nlogn

    //k만큼 자리바꾸기
    for(int i=0; i<k; i++){                //시간복잡도 k
        A[i] = B[i];
    }

    //배열 A 누적합
    int sum = accumulate(A.begin(), A.end(), 0);  //시간복잡도 n

    cout << sum;

    return 0;
}