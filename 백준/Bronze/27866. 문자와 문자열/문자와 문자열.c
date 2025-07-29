#include <stdio.h>

int main(void)
{
    char word[1001];
    int n;
    scanf("%s", word);
    scanf("%d", &n);
    printf("%c\n", word[n - 1]);
    return 0;
}