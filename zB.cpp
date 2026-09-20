#include <iostream>
#include <vector>
#include <utility> 
#include <string>  
#include <sstream> 

using namespace std;

void InsertionSort(vector<int>& A) {
    int n = A.size();
    
    for (int i = 1; i < n; ++i) {
    	int key = A[i];
    	int j = i;
    	
    	while (j >= 1 and A[j - 1] > key) {
    		A[j] = A[j - 1];
    		--j;
		}
		A[j] = key;
	}
}

int main() {
    string line;
    getline(cin, line);
    
    stringstream ss(line);
    vector<int> A;
    int x;
    while (ss >> x) {
        A.push_back(x);
    }

    InsertionSort(A);

    for (int i = 0; i < (int)A.size(); ++i) {
        cout << A[i] << " ";
    }
    cout << endl;
    
    return 0;
}
