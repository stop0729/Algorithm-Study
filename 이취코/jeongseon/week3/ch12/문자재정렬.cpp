#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

//모든 알파벳 오름차순 -> 모든 숫자 더한 값

string s;
vector<char> alpabet;

int sn;

int main(){

    cin >> s;

    for(int i=0; i<s.size(); i++){
        if(s[i] - 'A' < 0){
            sn += s[i]-'0';
        }else{
            alpabet.push_back(s[i]);
        }
    }

    sort(alpabet.begin(), alpabet.end());

    for(int i=0; i< alpabet.size(); i++){
        cout << alpabet[i];
    }
    cout << sn;



    return 0;
}