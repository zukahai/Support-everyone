#include <iostream>

using namespace std;

char binToString(string s){
    int ans = 0;
    for (int i = 0; i < s.length(); i++)
        ans = 2 * ans + (s[i] - '0');
    return ans;
}

string deCode(string s){
    string ans = "";
    for (int i = 0; i < s.length(); i += 9)
        ans = ans + binToString(s.substr(i, 8));
    return ans;
}

string intToBin(int n){
    string ans = "";
    while (n > 0){
        ans = char(n % 2 + '0') + ans;
        n /= 2;
    }
    while (ans.length() < 8)
        ans = "0" + ans;
    return ans;
}

string enCode(string s){
    string ans = "";
    for (int i = 0; i < s.length(); i++){
        ans = ans + intToBin(s[i]) + " ";
    }
    return ans;
}

int main(){
    string s;
    getline(cin, s);
    cout << enCode(s);
}
