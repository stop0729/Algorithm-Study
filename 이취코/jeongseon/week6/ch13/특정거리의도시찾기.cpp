#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

//dfs로 풀기

int n, m, k, x;  //도시갯수, 도로갯수, 거리정보, 출발도시번호
int s, e;
vector<vector<int>> v;
bool isPos=0;
int visited[300003];

void dfs(int x, int num){    //num은 방문 횟수임
    
    if(visited[x]!= -1 && visited[x] <= num){
        return;
    }
    visited[x]= num;      //이건 bfs에서 많이 쓰는거긴함..

    for(int i : v[x]){
        if(visited[i]== -1 || visited[i]> num+1){
            dfs(i, num+1);
        }
        //dfs(i, num+1);
    }
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> n >> m >> k >> x;

    v.resize(n+1);

    //도로 입력 받기
    for(int i=0; i<m; i++){
        cin >> s >> e;
        v[s].push_back(e);   //단방향
    }

    fill(visited, visited+n+1, -1); //-1로 초기화
    
    dfs(x, 0);

    for(int i=1; i<=n; i++){
        if(visited[i]== k){
            cout << i << "\n";
            isPos=true;
        }
    }
    
    if(!isPos){
        cout << -1;
    }

    return 0;
}