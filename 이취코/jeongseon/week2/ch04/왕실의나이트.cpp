#include <iostream>
using namespace std;

string s;
int curX, curY;
int dy[] = {-1, 0, 1, 0};
int dx[] = {0, 1, 0, -1};
int cnt;


int main(){

    cin >>s;  //a1
    //curX = s[0] - 'a'; //char
    //curY = s[1] - '1';

    for(int i = 0; i< 4; i++){ //상하좌우
        bool isPossible=true;

        curX = s[0] - 'a'; //char
        curY = s[1] - '1';

        if(i==0 || i==2){
            //수직으로 2번 이동
            for(int j = 0; j<2; j++){
                int ny = curY + dy[i];
                int nx = curX + dx[i];   //차피 0
                if(ny < 0 || nx < 0 || ny >7 || nx >7) {
                    isPossible = false;
                    break;
                }
                curY = ny;
                curX = nx;
            }
            if(isPossible){
                //수평으로 1번 이동
                if(curX + dx[1] >= 0 && curX + dx[1] <= 7) cnt++;
                if(curX + dx[3] >=0 && curX + dx[3] <= 7) cnt++;
            }
            
        }else{
            //수평으로 2번 이동
            for(int j = 0; j<2; j++){
                int ny = curY + dy[i];  //차피 0
                int nx = curX + dx[i];   
                if(ny < 0 || nx < 0 || ny >7 || nx >7){
                    isPossible = false;
                    break;
                }
                curY = ny;
                curX = nx;
            }
            if(isPossible){
                //수직으로 1번 이동
                if(curY + dy[0] >= 0 && curY + dy[0] <= 7) cnt++;
                if(curY + dy[2] >=0 && curY + dy[2] <= 7) cnt++;
            }
        }
    }

    cout << cnt;

    return 0;
}