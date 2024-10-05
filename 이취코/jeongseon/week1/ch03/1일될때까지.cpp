#include <iostream>
using namespace std;

//n이 1이 될 때까지 1번 or 2번 과정 수행
//2번 과정 즉 나눴을 때가 1에 훨씬 더 가까워질 확률이 높이지므로 나눌 수 있으면 최대한 나누자


int n,k, cnt;

int main(){

    cin >> n >> k;

    while(true){
        if(n==1) break;
        if(n % k ==0){
            n /= k;
        }else{
            n -= 1;
        }
        cnt++;
    }

    cout << cnt;
    
    return 0;
}