#include <iostream>
#include <vector>

using namespace std;

bool check(int dist, const vector<int>& a, int k) {
    int count = 1;
    int last_pos = a[0];
    
    for (int i = 1; i < a.size(); ++i) {
        if (a[i] - last_pos >= dist) {
            count++;
            last_pos = a[i]; 
        }
    }
    
    return count >= k; 
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, k;
    cin >> n >> k;

    vector<int> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    int left = 1;
    int right = a[n - 1] - a[0] + 1;

    while (right - left > 1) {
        int m = left + (right - left) / 2;

        if (check(m, a, k)) {
            left = m;
        } else {
            right = m;
        }
    }

    cout << left << "\n";

    return 0;
}
