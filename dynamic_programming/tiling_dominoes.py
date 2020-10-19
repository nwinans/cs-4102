dp = []

def tile_options(length: int) -> int:
    if length % 2 == 1 or length < 0:
        return 0
    if length == 0:
        return 1
    global dp 
    dp = [-1] * (length + 1)
    dp[0] = 1
    dp[1] = 1
    return tile_dp(length)

def tile_dp(n: int) -> int:
    if dp[n] != -1:
        return dp[n]
    if n % 2 == 0:
        result = tile_dp(n-2) + 2*tile_dp(n-1)
    else:
        result = tile_dp(n-2) + tile_dp(n-1)
    dp[n] = result
    return result

print(tile_options(12))