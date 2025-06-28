//max hillyer 6/28/25

bool isPalindrome(int x) {
    if (x<0){
        return false; }
    int new = x;
    long k = 0;
    while (new>0){
        int n = new%10;
        k = k*10;
        k += n;
        new /= 10;
    }
    return (k == x);
    
}
