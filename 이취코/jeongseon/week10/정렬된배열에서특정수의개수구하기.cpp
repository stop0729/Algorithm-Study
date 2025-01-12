#include <iostream>
#include <tuple>
#include <map>
using namespace std;

//수열이 오름차순 정렬이 되어있을 때
//x가 등장한 횟수 구하기

//map으로 저장하고 이진탐색으로 탐색하기

int n, x;
map<int, int> mp;

int binarySearch(map<int,int> mp, int target){
	int left = 0;
	int right = mp.size()-1;
	
	while(left <= right){
		int mid = (left + right) / 2;
		
		if(mid == target) return mp[mid]; //갯수
		else if(target < mid){
			right= mid - 1;
		}else{
			left = mid + 1;
		}
	}
	
	return -1;
}

int main(){
	
	cin >> n >> x;
	
	for(int i=0; i<n; i++){
		int num;
		cin >> num;
		mp[num]++;  //map에 갯수 저장
	}
	
	//이미 정렬된게 입력으로 들어오므로 sort 필요x
	
	cout << binarySearch(mp, x);
	
	return 0;
}