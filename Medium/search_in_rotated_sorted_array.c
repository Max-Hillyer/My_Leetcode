//max hillyer 6/29/25

int search(int* nums, int numsSize, int target) {
    for (int i =0; i < numsSize; i++){
        if (nums[i] == target){
            return i;
        }
    }
    return -1;
}
