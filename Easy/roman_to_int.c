//Max hillyer 6/28/25

int value(char c) {
    switch(c) {
        case 'I': return 1;
        case 'V': return 5;
        case 'X': return 10;
        case 'L': return 50;
        case 'C': return 100;
        case 'D': return 500;
        case 'M': return 1000;
        default: return 0;
    }
}

int romanToInt(char* s) {
    int total = 0;
    int i = 0;

    while (s[i]) {
        int s1 = value(s[i]);
        int s2 = value(s[i+1]);

        if (s2 > s1) {
            total += s2 - s1;
            i += 2;
        } else {
            total += s1;
            i += 1;
        }
    }

    return total;
}

