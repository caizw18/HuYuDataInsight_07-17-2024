import sys


def matrix_chain_order(dimensions):
    n = len(dimensions) - 1  # Number of matrices
    dp = [[0] * n for _ in range(n)]

    # Solve for chains of increasing length
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = sys.maxsize
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + dimensions[i] * dimensions[k + 1] * dimensions[j + 1]
                if cost < dp[i][j]:
                    dp[i][j] = cost

    # Minimum number of scalar multiplications for full chain is dp[0][n-1]
    return dp[0][n - 1]


# Example usage:
dimensions = [10, 30, 5, 60]
print(f"The minimum number of scalar multiplications needed is: {matrix_chain_order(dimensions)}")