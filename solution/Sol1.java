package solution;

import java.util.Arrays;

public class Sol1 {
    public static void main(String[] args) {
        Solution solution = new Solution();

        int[] nums = new int[]{2, 7, 11, 13};
        int target = 9;
        System.out.println("Input: nums:" + Arrays.toString(nums));
        System.out.println("Input: target:" + String.valueOf(target));

        int[] answers =  solution.twoSum(nums, target);
        System.out.println("Output: answers:" + Arrays.toString(answers));
    }
}

class Solution {
    public int[] twoSum(int[] nums, int target) {
        int answer_list[] = new int[2];
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                int x = nums[i];
                int y = nums[j];
                if (x + y == target) {
                    answer_list[0] = i;
                    answer_list[1] = j;
                    break;
                }
            }
        }
        return answer_list;
    }
}