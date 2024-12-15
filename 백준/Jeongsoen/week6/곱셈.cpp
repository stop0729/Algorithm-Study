#include <iostream>
typedef long long ll;
using namespace std;

long long a, b, c;

ll go(ll a, ll b){
    if(b==1) return a%c;

    long long ret = go(a, b/2);
    ret = (ret * ret) %c;

    //홀수일 때
    if(b%2) ret= (ret*a) %c;

    return ret;
}

int main(){

    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> a >> b >> c;
    cout << go(a, b) << "\n";


    return 0;
}