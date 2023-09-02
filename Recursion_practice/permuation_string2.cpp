#include <bits/stdc++.h>

typedef long long ll;
#define endl "\n"

using namespace std;

string s = "aab";
int c = 0;

void perm(int take, string per) {
    if (take == s.size()) {
        cout << per << endl;
        c++;
        return;
    }
    for (int i = 0; i <= per.size(); i++) {
        string str = per;
        str.insert(i, 1, s[take]);
        perm(take + 1, str);
        if (i + 1 < str.size() && str[i + 1] == s[take]) {
            break;
        }
    }
}

int main() {
	perm(0, "");
	cout << "permutations count: " << c << endl;
	return 0;
}
