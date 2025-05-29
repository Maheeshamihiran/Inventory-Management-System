#include <iostream>
#include <chrono>
#include <vector>
#include <string>

using namespace std;
using namespace std::chrono;

int fib_rec(int n) {
    if (n == 0) return 0;
    if (n == 1) return 1;
    return fib_rec(n - 1) + fib_rec(n - 2);
}

int fib_mem(int n, vector<long>& mem) {
    if (n == 0) return 0;
    if (n == 1) return 1;
    if (mem[n] != -1) return mem[n];
    mem[n] = fib_mem(n - 1, mem) + fib_mem(n - 2, mem);
    return mem[n];
}

int fib_tab(int n) {
    if (n == 0) return 0;
    if (n == 1) return 1;
    vector<long> mem(n + 1);
    mem[0] = 0;
    mem[1] = 1;
    for (int i = 2; i <= n; i++) {
        mem[i] = mem[i - 1] + mem[i - 2];
    }
    return mem[n];
}

int main(int args, char* argv[]) {
    if (args < 2) {
        cout << "Usage: " << argv[0] << " <n>" << endl;
        return 0;
    }

    int n = stoi(argv[1]);

    auto start = high_resolution_clock::now();
    cout << "fib_rec(" << n << ") = " << fib_rec(n) << endl;
    auto stop = high_resolution_clock::now();
    auto duration = duration_cast<microseconds>(stop - start);
    cout << "Time taken by fib_rec: " << duration.count() << " microseconds" << endl;

    vector<long> mem(n + 1, -1);
    start = high_resolution_clock::now();
    cout << "fib_mem(" << n << ") = " << fib_mem(n, mem) << endl;
    stop = high_resolution_clock::now();
    duration = duration_cast<microseconds>(stop - start);
    cout << "Time taken by fib_mem: " << duration.count() << " microseconds" << endl;

    start = high_resolution_clock::now();
    cout << "fib_tab(" << n << ") = " << fib_tab(n) << endl;
    stop = high_resolution_clock::now();
    duration = duration_cast<microseconds>(stop - start);
    cout << "Time taken by fib_tab: " << duration.count() << " microseconds" << endl;

    return 0;
}
