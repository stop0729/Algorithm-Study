#include <iostream>
using namespace std;

string s;
int curX, curY;
int dy[] = {-2, -2, 2, 2, -1, 1, -1, 1};
int dx[] = {-1, 1, -1, 1, -2, -2, 2, 2}; // 나이트의 이동 방향
int cnt = 0;

int main(){

    cin >> s;
    curY = s[0] - 'a';
    curX = s[1] - '1';
    
    // 8개의 방향에 대해 이동 가능 여부 확인
    for(int i = 0; i < 8; i++){
        int ny = curY + dy[i];
        int nx = curX + dx[i];
        
        // 체스판 내에 있는지 확인
        if(ny >= 0 && nx >= 0 && ny < 8 && nx < 8) {
            cnt++;
        }
    }

    cout << cnt << "\n";

    return 0;
}
