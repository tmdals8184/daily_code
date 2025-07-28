#include <stdio.h>

int main(void)
{
    int n, count = 0;
    int arr[42] = {0,};
    for (int i = 0; i < 10; i++)
    {
        scanf("%d", &n);
        arr[n % 42] = 1;
    }
    for (int i = 0; i < 42; i++)
        if (arr[i] > 0) count++;
    printf("%d\n", count);
    return 0;
}