#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int n,m;
vector<int> arr;
int ret;

int binarySearch(const vector<int>& arr, int target){
	int left =0;
	int right = arr.size()-1;
    cout << "right : " << right << "\n";
	
	while(left <= right){
		int sum=0; //떡 합
		int mid = (right + left) / 2; 
		//mid는 절단기 높이임
		
		//손님이 가져갈 수 있는 떡 길이
		for(int i : arr){
			if(i <= arr[mid]) continue;
			else sum += i - arr[mid];
		}
		
		if(sum == target){ //target:요청한 떡길이
			return arr[mid];
		}else if(sum > target){
			left = mid +1;
		}else{
			right = mid -1;
		}			
		
	}
}

int main(){
	
	cin >> n >> m;
	
	arr.resize(n);
	
	for(int i=0; i<n; i++){
		cin >> arr[i];
	}
	
	sort(arr.begin(), arr.end());
	
	
	cout << binarySearch(arr, m);
	
	
	return 0;
}

//최대라고 하지만 만족 시키는 결과 나오면 바로 종료하면 된다. 절단기 높이가 다른데 손님이 원하는 떡길이가 나오는 여러 종류는 있을 수 없다.
//처음에 순차 탐색을 떠올렸다. 탐색해야하는 수의 범위가 크면 이분 탐색을 먼저 떠올리자.
// https://breakcoding.tistory.com/188