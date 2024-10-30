#include <iostream>
using namespace std;

int n, mid, lsum, rsum;
string sn;

int main(){

    cin >> n;

    sn = to_string(n);

    mid = sn.size() / 2;

    //cout << mid;

    for(int i=0; i<mid; i++){
        lsum += sn[i]-'0';
    }
    for(int i=mid; i<sn.size(); i++){
        rsum += sn[i]-'0';                    //for문 하나로 해결 가능
    }

    if(lsum == rsum) cout << "LUCKY";
    else cout << "READY";


}