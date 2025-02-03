//用分治写一个求数组长度的程序
#include <iostream>
using namespace std;

int count(int *arr, int n) {
    if (n == 0) {
        return 0;
    }
    return 1 + count(arr + 1, n - 1);
}
