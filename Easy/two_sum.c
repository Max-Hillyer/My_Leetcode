//Max Hillyer 6/27/25
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    int *result = (int*)malloc(2 * sizeof(int));

    for (int i = 0; i <numsSize; i++){
        for (int j = 0; j < numsSize; j++){
            if (nums[j] + nums[i] ==target && i != j
            ) {
                result[0] = j;
                result[1] = i;
                *returnSize = 2;
                return result;
            }
        }
    }
    *returnSize = 0;
    return NULL;
}
