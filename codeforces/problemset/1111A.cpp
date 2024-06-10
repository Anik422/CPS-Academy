#include<bits/stdc++.h>
using namespace std;

bool checkVowel(char ch){
	if(ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u') return true;
	else return false;
}

int main(){
	#ifndef ONLINE_JUDGE
		freopen("input.txt", "r", stdin);
		freopen("output.txt", "w", stdout);
	#endif

	string s, t;
	cin >> s;
	cin >> t;
	if(s.length() != t.length()){
		cout << "NO" << endl;
	}else{
		bool temp = true;
		for(int i = 0; i < s.length(); i++){
			if(checkVowel(s[i]) != checkVowel(t[i])){
				temp = false;
				break;
			}
		}
		if(temp) cout << "YES" << endl;
		else cout << "NO" << endl;
	}

	return 0;
}