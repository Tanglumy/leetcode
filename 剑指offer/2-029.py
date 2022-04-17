class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':

        if not head:
            head = Node(insertVal, head)
            head.next = head
            return head

        OriHead = head
        while True:
            # 合适位置，插入
            if head.val <= insertVal <= head.next.val:
                head.next = Node(insertVal, head.next)
                return OriHead

            # 走到了循环点
            elif head.next.val < head.val:
                # 需要插入的点比最小值还小/比最大值还大
                if insertVal >= head.val or insertVal <= head.next.val:
                    head.next = Node(insertVal, head.next)
                    return OriHead

            else:
                # 走回原点了，还是没找到插入位置，只有一种可能：整个链表只有一种val
                # 此时原地插入返回即可
                if head.next == OriHead:
                    head.next = Node(insertVal, head.next)
                    return OriHead
            head = head.next
