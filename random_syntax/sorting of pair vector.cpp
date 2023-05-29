#include <bits/stdc++.h>

using namespace std;

bool sortParamFn(const pair <int,int> &a, const pair <int,int> &b) {
    return a.second < b.second;
}

int main()
{
    int arr[] = {10, 20, 5, 40 };
    int arr1[] = {30, 60, 20, 50};
    int n = sizeof(arr)/sizeof(arr[0]);

    vector <pair<int,int>> v;

//    for(int i = 0; i < n; i++) {
//        v.push_back( make_pair(arr[i], arr1[i]) );
//    }

    for(int i = 0; i < n; i++) {
        v.push_back( {arr[i], arr1[i]} );
    }

    for(auto x: v) {
        cout << x.first << " " << x.second << endl;
    }
    cout << endl;

    sort(v.begin(), v.end(), sortParamFn);


    vector <pair <int, int>>::iterator it;
    for(it = v.begin(); it!=v.end(); it++)
        cout << it->first << " " << it->second << endl;
}
