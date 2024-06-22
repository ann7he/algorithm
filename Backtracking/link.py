# 如何判断一个字符串是否是回文字符串的问题，我想你应该听过，我们今天的题目就是基于这个问题的改造版本。
# 如果字符串是通过单链表来存储的，那该如何来判断是一个回文串呢？你有什么好的解决思路呢？相应的时间空间复杂度又是多少呢？


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def isPalindrome(head: ListNode) -> bool:
    if not head or not head.next:
        return True

    # 使用快慢指针找到链表的中间节点
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # 反转链表的后半部分
    prev, curr = None, slow
    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp

    # 比较前半部分和反转后的后半部分
    first_half, second_half = head, prev
    while second_half:
        if first_half.val != second_half.val:
            return False
        first_half = first_half.next
        second_half = second_half.next

    return True


# 辅助函数：创建链表
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


# 示例测试
values = [1, 2, 3, 2, 1]
head = create_linked_list(values)
print(isPalindrome(head))  # 输出：True



# 单链表反转
# 链表中环的检测
# 两个有序的链表合并
# 删除链表倒数第 n 个结点
# 求链表的中间结点

