#include <iostream>
#include <tuple>
#include <string>
#include <vector>
using namespace std;

int n;
vector<pair<string, int>> student_info;

bool sort_operator(pair<string, int> a, pair<string, int> b){

    //if(a.second == b.second){
    //    
    //}
    return a.second < b.second;

}

int main(){

    cin >> n;

    for(int i=0; i<n; i++){
        string name; int score;
        cin >> name >> score;
        student_info.push_back({name, score});
    }

    //sort(student_info.begin(), student_info.end(), sort_operator);
    sort(student_info.begin(), student_info.end());

    for(auto it : student_info){
        cout << it.first << " ";
    }


    return 0;
}