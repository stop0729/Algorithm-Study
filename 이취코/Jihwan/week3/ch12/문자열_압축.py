def check(word, s, i):
    if word[s:s+i] == word[s+i:s+2*i]:
        return True
    else:
        return False
def solution(word):
    result = len(word)
    for i in range(1, len(word)//2 +1):
        switch = 0
        time = 0
        temp = len(word)
        for j in range(0,len(word)-2*i+1,i):
            if check(word, j, i) and switch == 0:
                time = 2
                temp -= i
                switch = 1
                # if j+2*i == len(word)-1:
                #     temp += 1
            elif check(word, j, i) and switch == 1:
                time += 1
                temp -= i
                # if j+2*i == len(word)-1:
                #     temp += len(str(time))
            elif check(word, j, i) != True and switch == 1:
                temp += len(str(time))
                time = 0
                switch = 0
        if switch == 1:
            temp += len(str(time))
        if result > temp:
            result = temp
    return result









# word = "aabbaccc"

# def check(word, s, i): # 
#     if word[s:s+i] == word[s+i:s+2*i]: # s=0 i=2
#         return True
#     else:
#         return False

# '''
# ababaccc -> '2abaccc'
# len(word) -> len(word) - 겹치는부분 + 숫자 ababcdcdababcdcd
# '''

# def solution(word):
#     result = 10000
    
#     for i in range(1, len(word)//2 +1): # abab cdcd [01 23] [23 45] [45 67]
#         switch = 0
#         time = 0
#         temp = len(word) # 처음 단어 길이 ababcdcd 첫번째 for문 ab ab 두번째 for문 ab cd 세번째 for문 cd cd
#         for j in range(0,len(word)-2*i+1,i):
#             if check(word, j, i) and switch == 0: # 처음 일치했을때
#                 time = 2 # check가 됐을때 생기는 앞 숫자 2
#                 temp -= i # 일치하면 그 일치한 단위 길이를 빼준다 ab
#                 switch = 1 # 이전까지 일치했는지 안 일치했는지 판단하는 기준 0-7 0 1 2 3 4 5 6 7
#                 if i ==1:
#                     if (j+1)+2*i >= len(word)-1:
#                         temp += len(str(time))
#                 else:
#                     if (j)+2*i >= len(word)-1:
#                         temp += len(str(time))

#             elif check(word, j, i) and switch == 1: # 이전부터 계속 일치해왔었는데 또 일치할때
#                 time += 1 # 
#                 temp -= i
#                 if i ==1:
#                     if (j+1)+2*i >= len(word)-1:
#                         temp += len(str(time))
#                 else:
#                     if (j)+2*i >= len(word)-1:
#                         temp += len(str(time))
#             elif check(word, j, i) != True and switch == 1: # 이전까지 일치했는데 이제는 일치하지 않을때
#                 temp += len(str(time))
#                 time = 0
#                 switch = 0
                
#         if result > temp:
#             result = temp


#     return result

# solution(word)




# #include <iostream>
# #include <vector>
# #include <string>
# using namespace std;

# string s;
# int start, cut=1, result=987654321;
# int main(){
#     cin >> s;
#     while(cut < s.size()){
#         start=0;
#         vector<string> tmp_v;
#         vector<pair<string, int>> cmp_v;
#         int isImpos=0;
#         while(s.size() / cut > 1 ){
#             string tmp_str;
#             cout << "1" << "\n";
#             for(int i = start; i < start+cut; i++){
#                 if(i + cut > s.size()){
#                     isImpos=1;
#                     cout << "2" << "\n";
#                     break;
#                 }
#                 tmp_str += s[i];
#             }
#             if(!isImpos){
#                 cout << "3" << "\n";
#                 tmp_v.push_back(tmp_str);
#                 start += cut;
#             }else{
#                 //이 부분 수정 필요
#                 int _div = s.size() % cut;
#                 //나눠 떨어지지 않았다면
#                 if(_div > 0){
#                     tmp_v.push_back(s.substr(s.size()-_div, _div));
#                 }
#                 break;
#                 cout << "3" << "\n";
#             }
#         }
#         cout << "-------------" << "\n";
#         for(string _s : tmp_v){
#             cout << _s << " " ;
#         }
#         cout << "\n-------------" << "\n";
#         cout << "after tmp size : " << tmp_v.size() <<"\n";
#         if(s.size() / cut <= 1){
#             //cut+=1;
#             //continue;
#             cout << "돌아가" <<"\n";
#             break;
#         }
#         string pre;
#         int pre_idx;
#         for(int i=0; i<tmp_v.size(); i++){
#             //0일 때 처리
#             if(cmp_v.empty()){
#                 pre = tmp_v[i];
#                 pre_idx =i;
#                 cmp_v.push_back({tmp_v[i], 1});
#                 continue;
#             }
#             if(tmp_v[i] != pre){
#                 pre = tmp_v[i];
#                 cmp_v.push_back({pre, 1});
#                 pre_idx++;
#             }else{
#                 cmp_v[pre_idx].second++;
#             }
#         }
#         int cnt =0;
#         for(auto _s : cmp_v){
#             if(_s.second > 1){
#                 cnt += to_string(_s.second).size();  //**
#             }
#             cnt += _s.first.size();
#         }
#         result = min(result, cnt);
#         cut += 1;
#     }
#     cout << result;
#     return 0;
# }
