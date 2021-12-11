"""
Stack Class
"""


class Stack:
    """
    Stack Class
    """
    def __init__(self):
        """
        Constructor
        """
        self._list = []

    def push(self, x):
        """
        Push
        """
        self._list.append(x)

    def pop(self):
        """
        Pop
        """
        return self._list.pop()


def test_stack():
    """
    test_stack
    """
    stack = Stack()
    stack.push("Hello")
    stack.push("How are you?")
    stack.push("Goodbye")

    assert stack.pop() == "Goodbye"
    assert stack.pop() == "How are you?"
    assert stack.pop() == "Hello"