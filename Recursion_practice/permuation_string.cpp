#include <bits/stdc++.h>

typedef long long ll;
#define endl "\n"

using namespace std;

string s = "abc";

void perm(int take, string per) {
    if (take == s.size()) {
        cout << per << endl;
        return;
    }
    for (int i = 0; i <= per.size(); i++) {
        string str = per;
        str.insert(i, 1, s[take]);
        perm(take + 1, str);
    }
}

int main() {
	perm(0, "");
	return 0;
}
