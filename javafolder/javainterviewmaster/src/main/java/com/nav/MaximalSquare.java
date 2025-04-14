package com.nav;

import java.util.Arrays;
import java.util.List;

public class MaximalSquare {

    @SuppressWarnings("unused")
    private int maximalSquare(char[][] matrix) {
        int rows = matrix.length;
        int cols = matrix[0].length;

        int[][] dp = new int[rows+1][cols+1];
        int max_side = 0;

        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; j++) {
                if (matrix[r][c] == '1') {
                    dp[r+1][c+1] = Math.min(dp[r][c], Math.min(dp[r+1][c],dp[r][c+1])) + 1;
                    max_side = Math.max(max_side, dp[r+1][c+1]);
                }
            }
        }

        return max_side * max_side;

    }





}