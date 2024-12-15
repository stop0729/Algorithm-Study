#include <iostream>
using namespace std;

//입력 : 첫번째 장대에 쌓인 원판 개수
//출력 : 옮긴 횟수 출력
//출력 : 수행과정 출력

void func(int a, int b, int n){
    if(n==1){
        cout << a << " " << b << "\n";
        return;
    }

    func(a, 6-a-b, n-1);
    cout << a << " " << b << "\n";
    func(6-a-b, b, n-1);
}

int main(){

    int m;
    cin >> m;
    cout << (1 << m) -1 << "\n"; //최소 경우의 수 : 2의 m승 -1
    func(1, 3, m);

    return 0;
}