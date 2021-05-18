temp = Node(x)
        if head is None:
            head = temp
        else:
            while head is not None:
                head = head.next
            head.next = temp
            temp.next = None 