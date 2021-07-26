#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define N 20000000000L

int main() {
    void *p = malloc(N); // I cannot request to much memory
    printf("got %p\n", p);
    if (p != NULL) {
        memset(p, 0, N);
        getchar();
        free(p);
    }
    return 0;
}