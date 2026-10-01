#include <iostream>
#include <vector>

using namespace std;

bool check(long long len, const vector<long long>& a, long long k) {
    if (len == 0) return true; 
    
    long long count = 0;
    for (long long x : a) {
        count += x / len;
    }
    return count >= k;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    long long k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    long long left = 0;
    long long right = 10000001; 

    while (right - left > 1) {
        long long m = left + (right - left) / 2;

        if (check(m, a, k)) {
            left = m; 
        } else {
            right = m;
        }
    }

    cout << left << "\n";

    return 0;
}
