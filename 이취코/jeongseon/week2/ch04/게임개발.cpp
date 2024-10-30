#include <iostream>
using namespace std;

int arr[53][53], n, m, y, x, dir, ny, nx, leftrotate, ret=1;
int visited[53][53];

int dy[] = {-1, 0, 1, 0};  //북동남서로 변경
int dx[] = {0, -1, 0, 1};

int main(){

    cin >> n >> m;
    cin >> y >> x >> dir;

    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++){
            cin >> arr[i][j];
        }
    }

    while(true){

        dir-=1;
        if(dir<0){
            dir+=4;
        }

        //바라보고 있는 방향으로 이동
        ny = y + dy[dir];
        nx = x + dx[dir];

        if(arr[ny][nx] == 0 && !visited[ny][nx]){
            y = ny; x = nx;
            visited[y][x]=1;  //dir 방향은 유지
            leftrotate=0;     //방향 횟수 초기화
            ret++;
            
        }else{
            leftrotate++; //회전횟수
        }

        //한바퀴 돔-> 갈 수 있는데 없음
        if(leftrotate == 4){

            int tmp_dir = dir+2;
            if(tmp_dir > 4) tmp_dir-=4;

            if(arr[y + dy[tmp_dir]][x + dx[tmp_dir]]=='0'){
                y += dy[tmp_dir];
                x += dx[tmp_dir];
                leftrotate=0;
            }else{
                break;
            }
        }
    }

    cout << ret << "\n";

    return 0;
}