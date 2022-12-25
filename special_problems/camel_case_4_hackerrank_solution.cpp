//https://www.hackerrank.com/challenges/three-month-preparation-kit-camel-case/problem


#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
	
    string s;
    int n, i;

    while(getline(cin, s)) {
		
		// important
        s.erase(remove(s.begin(), s.end(), '\r'), s.end());
		/*
		https://programs.programmingoneonone.com/2022/05/hackerrank-camel-case-4-problem-solution.html
		https://stackoverflow.com/questions/15433188/what-is-the-difference-between-r-n-r-and-n
		https://www.geeksforgeeks.org/remove-all-occurrences-of-a-character-from-a-string-using-stl/
		*/
		
        vector <string> ans;
        n = s.size();
        string tmp;

        if(s[0] == 'S') {
            if(s[2] == 'M') {
                n = n-2;
            }
            tmp+= tolower(s[4]);
            for(i = 5; i < n; ++i) {
                if(s[i] >= 'A' && s[i] <= 'Z') {
                    ans.push_back(tmp);
                    tmp.clear();
                    tmp+= tolower(s[i]);
                }
                else if(i == n-1) {
                    tmp+= s[i];
                    ans.push_back(tmp);
                    tmp.clear();
                }
                else {
                    tmp+= tolower(s[i]);
                }
            }
            int nn = ans.size();
            for(i = 0; i < nn; ++i) {
                cout << ans[i];
                if(i != nn-1) {
                    cout << " ";
                }
            }
        }

        else {
            string outputString;
            for(i = 4; i < n; ++i) {
                if(s[i]!= ' ' && s[i] != '\n') {
                    if(i-1 >= 0 && s[i-1] == ' ') {
                        outputString+= toupper(s[i]);
                    }
                    else
                        outputString+= s[i];
                }
            }
            if(s[2] == 'C')
                outputString[0] = toupper(outputString[0]);
            if(s[2] == 'M')
                outputString+= "()";
            cout << outputString;
        }

        cout << "\n";

    } 
    return 0;
}
