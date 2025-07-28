#include <stdio.h>

void swap(int *a, int *b);
int main(void)
{
    int n, m, a, b;
    int arr[100];
    scanf("%d %d", &n, &m);
    for (int i = 0; i < n; i++) arr[i] = i + 1;    
    for (int i = 0; i < m; i++)
    {
        scanf("%d %d", &a, &b);
        for (int j = 0; j < (b - a + 1) / 2; j++)
        {
            swap(&arr[a - 1 + j], &arr[b - 1 - j]);
            // 1 1 -> 0 -> 0 (1)
            // 1 2 -> 1 -> 1 
            // 1 3 -> 2 -> 1 (1)
            // 1 4 -> 3 -> 2
            // 1 5 -> 4 -> 2 (1)
        }       
    }
    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);
    return 0;
}

void swap(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}
