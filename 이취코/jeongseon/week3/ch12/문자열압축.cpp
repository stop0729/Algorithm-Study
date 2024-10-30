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
        int isImpos=0;

        while(s.size() / cut > 1 ){
            string tmp_str;

            for(int i = start; i < start+cut; i++){
                if(start + cut > s.size()){         //i는 변하는 숫자이기 때문에 i+cut이 아니라 start+cut으로 해야함.
                    isImpos=1;
                    break;
                }
                tmp_str += s[i];
         
            }

            if(!isImpos){
                tmp_v.push_back(tmp_str);
                start += cut;
            }else{
                //이 부분 수정 필요
                int _div = s.size() % cut;
                //나눠 떨어지지 않았다면 
                if(_div > 0){
                    tmp_v.push_back(s.substr(s.size()-_div, _div));
                }
                break;
            }

        }    

        if(s.size() / cut <= 1){
            break;
        }

        string pre;
        int pre_idx;

        for(int i=0; i<tmp_v.size(); i++){

            //0일 때 처리
            if(cmp_v.empty()){
                pre = tmp_v[i];
                pre_idx =i;
                cmp_v.push_back({tmp_v[i], 1});
                continue;
            }

            if(tmp_v[i] != pre){
                pre = tmp_v[i];
                cmp_v.push_back({pre, 1});
                pre_idx++;
            }else{
                cmp_v[pre_idx].second++;
            }

        }


        int cnt =0;
        for(auto _s : cmp_v){
            if(_s.second > 1){
                cnt += to_string(_s.second).size();  //**
            }
            cnt += _s.first.size();
        }

        result = min(result, cnt);

        cut += 1;
    }

    cout << result;

    return 0;
}