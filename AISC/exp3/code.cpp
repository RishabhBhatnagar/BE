#include<bits/stdc++.h>

using namespace::std;
int get_int_seq(int m, int n, int d, int seq[]){
    int k=0, s=0;
    while(k != d){
        for(;k != d && k <= n; (seq[s++] = m), k += m);
        if(((k > n) && ((k -= n)) && (seq[s++] = -n)));
    }
    return s;
}


vector<pair<int, int>> get_pouring_seq(int seq[], int n, int l1, int l2){
    // n is the jug from which reduction is being done.
    int c1=0, c2=0;
    vector<pair<int, int>> res;
    for(int i=0; i < n; i++){
        int d = seq[i], f = d < 0 ? 1 : 0;
        if((f * (c2 < -d)) || ((f ^ 1) * ((c1 + d) > l1))){
            int t1 = d + c1 - l1;
            c1 = f * (c1 + d + c2) + (f ^ 1) * (c1 - t1);
            c2 = f * (c2 - d - c2) + (f ^ 1) * (c2 + t1);
            res.push_back(make_pair(c1, c2));
        }
        c1 += (f ^ 1) * (d);
        c2 += (f) * (d);
        res.push_back(make_pair(c1, c2));
    }
    return res;
}


vector<pair<int, int>> algo(int m, int n, int d){
    int int_seq1[1000],int_seq2[1000];
    int n1 = get_int_seq(m, n, d, int_seq1);
    int n2 = get_int_seq(n, m, d, int_seq2);
    vector<pair<int, int>> seq1 = get_pouring_seq(int_seq1, n1, m, n);
    vector<pair<int, int>> seq2 = get_pouring_seq(int_seq2, n2, n, m);
    return seq1.size() > seq2.size() ? seq2 : seq1;
}


int main(void){
    int a, b, d;
    cout << "Enter capacity of the First Jug: ";
    cin >> a;
    cout << "Enter capacity of the Second Jug: ";
    cin >> b;
    cout << "Enter the required capacity: ";
    cin >> d;

    if(d % (__gcd(a, b)) == 0){
        cout << "Transfer sequence is as follows: " << endl;
        for(auto p: algo(a, b, d))
            cout << "(" << p.first << ", " << p.second << ")" << endl;
    }
    else
        cout << "No such sequence possible.";
    return 0;
}

