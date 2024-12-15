#include <iostream>
using namespace std;

int n, r, c;

int func(int n, int r, int c){
    if(n==0) return 0;
    int half = (1<< n-1);    //2의 n-1승
    if(r<half && c< half) return func(n-1, r, c);
    else if(r<half && c >= half) return half*half + func(n-1, r, c-half);    //c-half: 1사각형으로 평행이동이라고 생각하면 됨
    else if(r>=half && c < half) return 2*half*half + func(n-1, r-half, c);
    return 3*half*half + func(n-1, r-half, c-half);
}

int main(){

    cin >> n >> r >> c;
    cout << func(n, r, c);
    return 0;
}