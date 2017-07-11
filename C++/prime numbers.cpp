#include <iostream>
using namespace std;

int main(){
	int num;
	int n;
	for(num = 2; num < 100; num += 1){
		for(n = 2; n < num; n += 1){
			if(num%n==0){
			break;
			}
			else if(num%n!=0){
				cout << num << endl;
			}
		}
	}
	
}
