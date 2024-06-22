# 约瑟夫斯问题（Josephus Problem）是一个著名的数学问题，具体描述如下：
# n 个人（编号为 0 到 n-1）围成一个圈，从编号为 0 的人开始报数。每次报到第 m 个人时，将其杀掉，
# 直到最后一个人留下为止。求最后留下的那个人的编号。

# 递归解法

def josephus_recursive(n, m):
    if n == 1:
        return 0
    else:
        return (josephus_recursive(n - 1, m) + m) % n

# 示例测试
n = 7
m = 3
print(josephus_recursive(n, m))  # 输出：3

# 迭代解法

def josephus_iterative(n, m):
    result = 0  # 初始时，只有一个人，编号为0
    for i in range(2, n + 1):
        result = (result + m) % i
    return result

# 示例测试
n = 7
m = 3
print(josephus_iterative(n, m))  # 输出：3
