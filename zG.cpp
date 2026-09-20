#include <iostream>
#include <vector>

using namespace std;

void CountSort(vector<int>& A) {
    vector<int> counts(101, 0); 

    for (int i = 0; i < A.size(); ++i) {
        int num = A[i];
        counts[num]++;
    }

    int index = 0;

    for (int value = 0; value <= 100; ++value) { 
        for (int i = 0; i < counts[value]; ++i) {
            A[index] = value;
            index++;
        }
    }
}

int main() {
    vector<int> A;
    int x;

    while (cin >> x) {
        A.push_back(x);
    }

    CountSort(A);

    for (int i = 0; i < A.size(); ++i) {
        cout << A[i] << " ";
    }
    cout << endl;

    return 0;
}

