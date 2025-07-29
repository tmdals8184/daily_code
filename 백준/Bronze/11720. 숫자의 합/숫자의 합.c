#include <stdio.h>

int main(void)
{
    int n, sum = 0;
    char num[101];
    scanf("%d", &n);
    scanf("%s", num);
    for (int i = 0; i < n; i++) 
        sum += (int)(num[i]) - (int)'0';
    printf("%d\n", sum);
    return 0;
}