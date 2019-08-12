#include<bits/stdc++.h>
#define X INT_MAX 
#define G 100

using namespace::std;


vector<int> get_adjs(vector<int> graph, int node, int m, int n){
    vector<int> ans;
    if((node >= n) && (graph[node - n] != X)) 
        ans.push_back(node-n);          // up
    if((node + n < m * n) && (graph[node + n] != X)) 
        ans.push_back(node + n); // down
    if(((node % n) != 0)  && (graph[node - 1] != X)) 
        ans.push_back(node - 1);        // left
    if(((node + 1) % m != 0) && (graph[node + 1] != X)) 
        ans.push_back(node + 1); // right
    return ans;
}


void print_queue(queue<int> q){
    for(queue<int> tq = q; !tq.empty();){
        cout << tq.front() << ", ";
        tq.pop();
    }
}


void BFS(vector<int> graph, int s, int m, int n){
    // s: start node.
    // n: number of nodes in the graph.
    queue<int> q;
    vector<int> res;
    q.push(s);
    res.push_back(s);
    for(int i=0; !q.empty(); i++){
        
        /*cout << "queue: ";
        print_queue(q);
        cout << endl;*/
        
        int node = q.front();
        q.pop();
        

        for(int adj: get_adjs(graph, node, m, n)){
            if(find(res.begin(), res.end(), adj) == res.end()){
                q.push(adj);
                cout << adj << endl;
                if(graph[adj] == G){
                    cout << "Found a path";
                }
                res.push_back(adj);
            }
        }
    }
}

int main(void){
    vector<int> graph = {
                    1, 1, X, X, X,
                    X, 1, X, G, X,
                    X, 1, X, 1, X,
                    X, 1, 1, 1, X
                };
    BFS(graph, 0, 4, 5);
    return 0;
}
