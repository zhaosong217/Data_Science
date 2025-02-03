#include <iostream>
// d&c应用一:求和
int sum(int *arr, int n) 
{
    if (n == 0) 
        return 0;
    return arr[0] + sum(arr + 1, n - 1);
}
// d&c应用二:求GCD
int gcd(int a, int b)
{
    if (b==0)
        return a;
    return gcd(b, a%b);
}
// d&c应用三:求数组长度
int arr_len(int *arr)
{
    return sizeof(arr)/sizeof(arr[0]);
}

// d&c应用四:求数组最大值
int mx_num(int *arr)
{
    if (arr[0] > arr[1])
        return arr[0];
    return mx_num(arr + 1);
}
int main() 
{
    int a[] = {1, 2, 3, 4, 5};
    std::cout << "arr_len(a) = " << sizeof(a)/sizeof(int) << std::endl;
    //std::cout << "sum(arr, 5) = " << sum(arr, 5) << std::endl;
    //std::cout << "gcd(1680, 640) = " << gcd(1680,640) << std::endl;
    return 0;
}


