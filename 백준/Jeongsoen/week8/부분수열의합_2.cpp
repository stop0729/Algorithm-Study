#include <iostream>
using namespace std;

int n, s, arr[23], cnt;

int main(){

    cin >> n >> s;

    //입력 받기
    for(int i=0; i<n; i++){
        cin >> arr[i];
    }

    for(int i=1; i < (1<<n); i++){   //모든 경우의 수 
        //i=1부터 2의 n승-1까지
        int sum =0;
        for(int j=0; j<n; j++){//숫자들
            if(i & (1 << j)){
                //선택된 숫자들 더한다
                //cout << "arr[j] : " << arr[j] << "\n";
                sum += arr[j];
            }
        }

        //다 더한 숫자들 s랑 같으면 cnt++
        if(sum == s){
            cnt++;
        }
    }

    cout << cnt;


    return 0;
}