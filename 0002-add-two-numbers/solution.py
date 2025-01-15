class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        This function adds two numbers represented by linked lists, and returns a new linked list with the sum.

        The two input linked lists represent two numbers, with each node in the linked list representing a digit in the number.
        The number is represented with the least significant digit first, and the most significant digit last.

        The output linked list represents the sum of the two input numbers, with each node in the linked list representing a digit in the sum.
        The sum is also represented with the least significant digit first, and the most significant digit last.
        """
        # Create a dummy node that will be used as the head of the result linked list
        dummyHead = ListNode(0)

        # Keep track of the tail of the result linked list
        tail = dummyHead

        # Keep track of any carry from the previous addition
        carry = 0

        # Loop until we have processed all the nodes in both linked lists, and there is no carry left over
        while l1 is not None or l2 is not None or carry != 0:
            # Get the current digit from the first linked list, or 0 if we have reached the end of the list
            digit1 = l1.val if l1 is not None else 0

            # Get the current digit from the second linked list, or 0 if we have reached the end of the list
            digit2 = l2.val if l2 is not None else 0

            # Calculate the sum of the two digits, and add the carry from the previous addition
            sum = digit1 + digit2 + carry

            # Calculate the new digit for the current node in the result linked list
            digit = sum % 10

            # Calculate the carry for the next addition
            carry = sum // 10

            # Create a new node with the calculated digit
            newNode = ListNode(digit)

            # Add the new node to the result linked list
            tail.next = newNode

            # Move the tail to the newly added node
            tail = tail.next

            # Move to the next node in the first linked list, if there is one
            l1 = l1.next if l1 is not None else None

            # Move to the next node in the second linked list, if there is one
            l2 = l2.next if l2 is not None else None

        # Create the result linked list by returning the next node of the dummy head
        result = dummyHead.next

        # Clear the next pointer of the dummy head to prevent a cycle
        dummyHead.next = None

        # Return the result linked list
        return result
