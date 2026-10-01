#include <iostream>
#include <algorithm>

using namespace std;

bool good(long long cnt, long long q, long long s, long long t) {
    return (t / q + t / s) >= cnt;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    long long n, quick, slow;
    if (!(cin >> n >> quick >> slow)) return 0;

    if (quick > slow) {
        swap(quick, slow);
    }

    long long l = 0;
    long long r = (n - 1) * slow;

    while (r - l > 1) {
        long long m = (l + r) / 2;

        if (!good(n - 1, quick, slow, m)) {
            l = m;
        } else {
            r = m;
        }
    }

    cout << r + quick << "\n";

    return 0;
}
