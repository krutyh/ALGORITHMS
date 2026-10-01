#include <iostream>
#include <algorithm>

using namespace std;

bool check(long long w, long long h, long long n, long long side) {
    long long cols = side / w;
    long long rows = side / h;

    if (cols == 0 || rows == 0) return false;

    return cols >= (n + rows - 1) / rows;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    long long w, h, n;
    if (!(cin >> w >> h >> n)) return 0;

    long long l = 0;
    long long r = max(w, h) * n;

    while (r - l > 1) {
        long long m = l + (r - l) / 2;

        if (!check(w, h, n, m)) {
            l = m; 
        } else {
            r = m;
        }
    }

    cout << r << "\n";

    return 0;
}
