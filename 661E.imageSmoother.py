# coding:utf-8
# 第1种解法
def imageSmoother(self, M):
    R, C = len(M), len(M[0])
    ans = [[0] * C for _ in M]
    for r in range(R):
        for c in range(C):
            count = 0
            # 再用两个for求元素和，加上该元素最多有3×3个元素
            for nr in (r-1, r, r+1):
                for nc in (c-1, c, c+1):
                    # 根据下标去除不存在的元素，如边界元素
                    if 0 <= nr < R and 0 <= nc < C:
                        ans[r][c] += M[nr][nc]
                        count += 1
            ans[r][c] //= count
    return ans


