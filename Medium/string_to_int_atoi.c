// max hillyer 6/29/25

#include <ctype.h>
#include <limits.h>
int myAtoi(char* s) {
    long final = 0;
    int sign = 1;
    int i = 0;
    while (isspace(s[i])){
        i++;
    }
    if (s[i] == '-' || s[i] == '+'){
        if (s[i] == '-'){
            sign = -1;
        }
        i++;
    }
    while (s[i] == '0'){
        i++;
    }
    while (isdigit(s[i])) {
        final = final * 10 + (s[i] - '0');

        if (sign == 1 && final > INT_MAX) {
            return INT_MAX;
        }
        if (sign == -1 && -final < INT_MIN) {
            return INT_MIN;
        }

        i++;
    }
    return final * sign;
}
