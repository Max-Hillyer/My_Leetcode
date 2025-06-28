//max hillyer 6/28/25

#include <limits.h>
int reverse(int x){
    int new = x;
    long k = 0;
    while (new != 0){
        int n = new%10;
        k *= 10;
        k += n;
        new /= 10;
    }
    if (k > INT_MAX || k < INT_MIN){
        return 0;
    }
    return k;
}

