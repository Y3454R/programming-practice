#include <bits/stdc++.h>

using namespace std;


int main()
{
    set <int> st;
    for(int i = 0; i < 7; ++i)
        st.insert(i+1);

    for(auto x:st)
        cout << x << " ";
    cout <<endl;

    if(st.count(2)) {
        st.erase(2);
    }

    set<int>::iterator it;
    for(it = st.begin(); it!=st.end(); it++)
        cout << *it << " ";
    cout <<endl;

}
