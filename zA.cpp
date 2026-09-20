#include <iostream>
#include <vector>
#include <utility> 
#include <string>  
#include <sstream> 
using namespace std;

void SelectionSort(vector<int>& A) {
    int n = A.size();

    for (int i = 0; i < n - 1; ++i) {
        int max_index = i;

        for (int j = i + 1; j < n; ++j) {
            if (A[j] > A[max_index]) {
                max_index = j;
            }
        }

        if (max_index != i) {
            swap(A[i], A[max_index]);
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

    SelectionSort(A);

    for (int i = 0; i < (int)A.size(); ++i) {
        cout << A[i] << " ";
    }
    cout << endl;
    
    return 0;
}

