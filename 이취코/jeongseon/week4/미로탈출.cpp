#include <iostream>
#include <queue>
#include <tuple>

using namespace std;


//0: 괴물 O
//1: 괴물 X
//동빈이가 탈출하기 위해 움직여야 하는 최소 칸 수 
//시작 : (1,1)
//탈출 : (n, m)

int n, m, visited[203][203];
char map[203][203];
int dy[]={-1, 0, 1, 0};
int dx[]={0, 1, 0, -1};

void bfs(int y, int x){
    visited[y][x]=1;
    queue<pair<int, int>> q;
    q.push({y, x});

    while(!q.empty()){
        tie(y, x) = q.front(); q.pop();

        for(int i=0; i<4; i++){
            int ny = y + dy[i];
            int nx = x + dx[i];

            if(ny < 1 || ny > n || nx< 1 || nx >m || map[ny][nx]=='0') continue;
            if(!visited[ny][nx]){
                visited[ny][nx]= visited[y][x] + 1;
                q.push({ny, nx});
            } 
        }
    }
}

int main(){

    cin >> n >> m;

    for(int i=1; i<=n; i++){
        for(int j=1; j<=m; j++){
            cin >> map[i][j];
        }
    }

    bfs(1,1);

    cout << visited[n][m];

    return 0;
}