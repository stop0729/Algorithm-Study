#include <iostream>
using namespace std;

//0 : 구멍이 뚫려있는 부분
//1: 칸막이가 존재하는 부분

int n, m, cnt, visited[1003][1003];
char arr[1003][1003];
int dy[]={-1, 0, 1, 0};
int dx[]={0, 1, 0, -1};

void dfs(int y, int x){
    visited[y][x]=1;

    for(int i=0; i<4; i++){
        int ny = y + dy[i];
        int nx = x + dx[i];

        if(ny <0 || ny>=n || nx<0 || nx>=m || arr[ny][nx]=='1') continue;
        if(!visited[ny][nx]){
            dfs(ny, nx);
        }

    }

}

int main(){

    cin >> n >> m;

    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++){
            cin >> arr[i][j];
        }
    }

    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++){
            if(arr[i][j]=='0' && !visited[i][j]){
                dfs(i, j);
                cnt++;
            }
        }
    }

    cout << cnt;



    return 0;
}


/**
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111*/