#include <iostream>
#include <vector>
#include <string>

using namespace std;

class MinHeap {
private:
    vector<int> heap;

    void siftUp(int idx) {
        while (idx > 0) {
            int parent = (idx - 1) / 2;
            if (heap[idx] < heap[parent]) {
                swap(heap[idx], heap[parent]);
                idx = parent;
            } else {
                break;
            }
        }
    }

    void siftDown(int idx) {
        int size = heap.size();
        while (2 * idx + 1 < size) {
            int left = 2 * idx + 1;
            int right = 2 * idx + 2;
            int smallest = left;
            if (right < size && heap[right] < heap[left]) {
                smallest = right;
            }

            if (heap[idx] <= heap[smallest]) {
                break;
            }

            swap(heap[idx], heap[smallest]);
            idx = smallest;
        }
    }

public:
    void add(int val) {
        heap.push_back(val);
        siftUp(heap.size() - 1);
    }

    void extract() {
        if (heap.empty()) {
            cout << "CANNOT\n";
            return;
        }
        if (heap.size() == 1) {
            cout << heap[0] << "\n";
            heap.pop_back();
            return;
        }

        cout << heap[0] << "\n";
        heap[0] = heap.back();
        heap.pop_back();
        siftDown(0);
    }

    void clear() {
        heap.clear();
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    MinHeap hp;
    string command;

    while (cin >> command) {
        if (command == "ADD") {
            int n;
            cin >> n;
            hp.add(n);
        } else if (command == "EXTRACT") {
            hp.extract();
        } else if (command == "CLEAR") {
            hp.clear();
        }
    }

    return 0;
}

