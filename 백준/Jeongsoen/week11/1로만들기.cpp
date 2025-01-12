#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

//(x%3==0) x/=3
//(x2==0) x/=2
//x-=1

//기저 : 1 나오면 종료

//초기화
int dp[1000003], n;
const int INF = 987654321;


int main(){
    //초기화
    memset(dp, INF, sizeof(dp));
    cin >> n;

    dp[1] = 0;

    //bottom-up
    for(int i=2; i<=n; i++){
        dp[i] = dp[i-1] + 1;
        if(i%3 == 0) dp[i] = min(dp[i], dp[i/3]+1);
        if(i%2 == 0) dp[i] = min(dp[i], dp[i/2]+1);
        
    }

    cout << dp[n];

    return 0;
}