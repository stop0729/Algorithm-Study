#include <string>
#include <vector>

using namespace std;

//0인 곳만 이동할 수 있다.
//회전은 상좌->우하
//상, 우, 하, 좌, 회전
int dy[] = {-1, 0, 1, 0, 1};
int dx[] ={ 0, 1, 0, -1, 1};

int solution(vector<vector<int>> board) {
    int cnt = 0;
    
    pair<int, int> s = {0,0};
    pair<int, int> e = {0,1};
    
    for(int i=0; i<4; i++){
        pair<int, int> ns = s;
            
            
            
            
    }
    
    
    
    
    
    return cnt;
}

int main() {
    // 테스트용 보드 생성
    vector<vector<int>> board = {
        {0, 0, 0, 1, 1},
        {0, 0, 0, 1, 0},
        {0, 1, 0, 1, 1},
        {1, 1, 0, 0, 1},
        {0, 0, 0, 0, 0}
    };

    // solution 함수 호출
    int result = solution(board);
    
    // 결과 출력
    cout << "Result: " << result << "\n";

    return 0;
}