#include <bits/stdc++.h>

using namespace std;


void merge_func(vector <int>& v, int starting_indx, int mid, int last_index) {
    int len1 = mid - starting_indx + 1;
    int len2 = last_index - mid;
    vector <int> v1(len1);
    vector <int> v2(len2);
    int i, j, k;
    for(i = 0; i < len1; i++) {
        v1[i] = v[starting_indx + i];
    }
    for(i = 0; i < len2; i++) {
        v2[i] = v[mid + i + 1];
    }
    i = j = 0;
    k = starting_indx;
    while(i < len1 && j < len2) {
        if(v1[i] <= v2[j]) {
            v[k] = v1[i];
            i++;
        }
        else {
            v[k] = v2[j];
            j++;
        }
        k++;
    }
    while(i < len1) {
        v[k] = v1[i];
        i++;
        k++;
    }
    while(j < len2) {
        v[k] = v2[j];
        j++;
        k++;
    }
}

void merge_sort(vector <int>& v, int starting_indx, int last_indx) {
    if(starting_indx >= last_indx)
        return;
    int mid = (starting_indx + last_indx)/2;
    merge_sort(v, starting_indx, mid);
    merge_sort(v, mid+1, last_indx);
    merge_func(v, starting_indx, mid, last_indx);
}

int main()
{
    int n;
    cin >> n;
    vector <int> v(n);
    for(auto &x: v) cin >> x;
    merge_sort(v, 0, v.size()-1);
    for(auto x: v) cout << x << " ";
    cout << endl;
}
/*
5
1 3 6 8 2
*/
