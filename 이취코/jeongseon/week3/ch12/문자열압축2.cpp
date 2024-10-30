#include <iostream>
#include <vector>
using namespace std;

string s;
int start, cut=1, result=987654321;

int main(){
    cin >> s;
    
    while(cut < s.size()){
        start=0;
        vector<string> tmp_v;
        vector<pair<string, int>> cmp_v;

        // 이 부분을 수정: while문 대신 for문 사용
        for(int i = 0; i < s.size(); i += cut) {
            string tmp_str = "";
            
            // 남은 문자열 길이가 자르려는 길이보다 작은 경우
            if(i + cut > s.size()) {
                tmp_str = s.substr(i); //문자열의 i번째 위치부터 문자열 끝까지 자름
            } else {
                tmp_str = s.substr(i, cut);
            }
            
            tmp_v.push_back(tmp_str);
        }

        string pre;
        int pre_idx = 0;  // pre_idx 초기화 추가

        for(int i=0; i<tmp_v.size(); i++){
            //0일 때 처리
            if(cmp_v.empty()){
                pre = tmp_v[i];
                pre_idx = i;
                cmp_v.push_back({tmp_v[i], 1});
                continue;
            }

            if(tmp_v[i] != pre){
                pre = tmp_v[i];
                cmp_v.push_back({pre, 1});
                pre_idx = cmp_v.size() - 1;  // pre_idx 수정
            }else{
                cmp_v[pre_idx].second++;
            }
        }

        int cnt = 0;
        for(auto _s : cmp_v){
            if(_s.second > 1) cnt += to_string(_s.second).length();  // 숫자의 길이도 포함
            cnt += _s.first.size();
        }

        result = min(result, cnt);
        cut += 1;
    }

    cout << result;
    return 0;
}