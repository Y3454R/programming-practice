#include <bits/stdc++.h>

using namespace std;


int main()
{
    map <int, int> mp;
    int n, x;
    cout << "Enter number of inputs: ";
    cin >> n;
    for(int i = 0; i < n; i++) {
        cin >> x;
        mp[x]++;
    }
    map <int,int>::iterator it;
    for(it = mp.begin(); it!=mp.end(); it++) {
        cout << it->first << " " << it->second <<endl;
    }
    cout << "\nEnter a number to find: ";
    cin >> x;
    cout << endl;
    if(mp.count(x)) {
        cout << "ache\n";
    }
    else
        cout << "nai\n";
    cout << "\nEnter a number to see its count: ";
    cin>> x;
    cout << mp[x] << endl;
    cout << endl;
    for(auto ax: mp) {
        cout << ax.first << " " << ax.second << endl;
    }
}
/*
5
1 3 6 8 2
*/
