#include <bits/stdc++.h>

using namespace std;

int main()
{
    vector <int> v;
    for(int i = 0; i < 5; i++) {
        v.push_back(i+1);
    }
    sort(v.begin(), v.end(), greater<int>());
    for(auto x : v) {
        cout << x << " ";
    }
    return 0;
}
