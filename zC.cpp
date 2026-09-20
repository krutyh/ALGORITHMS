#include <iostream>
#include <vector>
#include <utility> 
#include <string>  
#include <sstream> 
using namespace std;

void BubbleSort(vector<int>& A) {
    int n = A.size();
    
    for (int i = 0; i < n - 1; ++i) {
    	bool swapped = false;
    	for (int j = 0; j < n - 1 - i; ++j) {
    		if (A[j] < A[j+1]) {
    			swap(A[j], A[j+1]);
    			swapped = true;
			}
		}
		if (!swapped) {
			break;
		}
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

    BubbleSort(A);

    for (int i = 0; i < (int)A.size(); ++i) {
        cout << A[i] << " ";
    }
    cout << endl;
    
    return 0;
}
