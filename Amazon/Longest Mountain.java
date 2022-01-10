'''
	Amazon Question 2: Longest Mountain in Array

You may recall that an array arr is a mountain array if and only if:

arr.length >= 3
There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given an integer array arr, return the length of the longest subarray, which is 
a mountain. Return 0 if there is no mountain subarray.

'''


class Solution {
    public int longestMountain(int[] arr) {
        int maxLength = 0;
        int i = 0, j = 0;
        boolean increasing = false, decreasing = false;
        
        while(i < arr.length - 2) {
            while(i < arr.length - 1 && arr[i] >= arr[i + 1]) {
                i++;
            }
            increasing = false; 
            decreasing = false;
            
            // increasing slope
            j = i;
            while(j < arr.length - 1 && arr[j] < arr[j + 1]) {
                increasing = true;
                j++;
            }
            
            // decreasing slope
            while(j < arr.length - 1 && arr[j] > arr[j + 1]) {
                decreasing = true;
                j++;
            }
            
            if(increasing && decreasing) maxLength = Math.max(maxLength, j - i + 1);
            i = j;
        }
        if(increasing && decreasing) maxLength = Math.max(maxLength, j - i + 1);
        return maxLength >= 3 ? maxLength : 0;
    }
}