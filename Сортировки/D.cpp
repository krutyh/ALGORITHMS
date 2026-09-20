#include <iostream>
#include <vector>
#include <utility> 

using namespace std;

int BubbleSort(vector<int>& A) {
    int n = A.size();
    int swap_count = 0;
    
    for (int i = 0; i < n - 1; ++i) {
    	bool swapped = false;
    	for (int j = 0; j < n - 1 - i; ++j) {
    		if (A[j] > A[j+1]) {
    			swap(A[j], A[j+1]);
    			swapped = true;
    			swap_count++;
			}
		}
		if (!swapped) {
			break;
		}
	}
	return swap_count;
}

int main() {
    int n;
    cin >> n;

    vector<int> A(n);
    for (int i = 0; i < n; ++i) {
        cin >> A[i];
    }

    int count = BubbleSort(A);

    cout << count << endl;
    
    return 0;
}
