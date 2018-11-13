"""Create a stack class."""
from typing import Any


class StackOverflowException(Exception):
    """Create a new exception."""
    pass


class StackUnderflowException(Exception):
    """Create a new exception."""
    pass


class Stack:
    """Simple stack implementation."""

    def __init__(self, capacity: int) -> None:
        """
        Initialise the stack.

        :param capacity: the maximum number of objects that stack can hold.
        """
        self.capacity = capacity
        self.stack_list = []

    def push(self, item: Any) -> None:
        """
        Add the element to the collection.

        If stack has no more room, raises StackOverflowException.
        """
        # print(f"Capacity: {self.capacity}")
        # print(f"Element to add: {item}")
        if len(self.stack_list) >= self.capacity:
            raise StackOverflowException()
        else:
            self.stack_list.insert(0, item)
            # print(f"New list: {self.stack_list}")

    def pop(self) -> Any:
        """
        Remove the most recently added element that was not yet removed.

        If stack is empty, raises StackUnderflowException.
        """
        if len(self.stack_list) == 0:
            raise StackUnderflowException()
        else:
            # print(f"Popped item: {self.stack_list[0]}")
            return self.stack_list.pop(0)

    def peek(self) -> Any:
        """
        Show the most recently added element without removing it from the stack.

        If stack is empty returns None.
        """
        if len(self.stack_list) == 0:
            # print(f"Stack is empty: {self.stack_list}")
            return None
        else:
            # print(f"Most recently added element: {self.stack_list[0]}")
            return self.stack_list[0]

    def is_empty(self) -> bool:
        """Return True/False depending on if stack is empty or not."""
        return True if len(self.stack_list) == 0 else False

    def is_full(self) -> bool:
        """Return True/False depending on if stack is full or not."""
        return True if self.capacity == len(self.stack_list) else False

    def __str__(self) -> str:
        """
        Get string representation of stack.

        If top element is present should return:
            "Stack(capacity={capacity}, top_element={top_element})"
        Else
            "Stack(capacity={capacity})"
        """
        if Stack.peek(self) is not None:
            # print(f"Stack(capacity={self.capacity}, top_element={Stack.peek(self)})")
            return f"Stack(capacity={self.capacity}, top_element={Stack.peek(self)})"
        else:
            # print(f"Stack(capacity={self.capacity})")
            return f"Stack(capacity={self.capacity})"


if __name__ == '__main__':
    # Define some items
    item_1 = "first item"
    item_2 = "second item"
    item_3 = "third item"
    stack_capacity = 5
    my_stack = Stack(stack_capacity)

    my_stack.push(item_1)
    my_stack.push(item_2)

    assert my_stack.pop() == item_2, "second item should be on the top of the stack"

    my_stack.push(item_3)

    assert my_stack.pop() == item_3, "third item should be on the top of the stack"
    assert my_stack.pop() == item_1, "first item should be on the top of the stack"

    # Now stack size should be zero, so after pop exception should be raised.
    try:
        my_stack.pop()
        assert False, "StackUnderflowException not raised"
    except StackUnderflowException:
        pass

    # Fill the stack
    for i in range(stack_capacity):
        my_stack.push(i)

    # Test that stack overflow exception is thrown
    try:
        my_stack.push("Too much items")
        assert False, "StackOverflowException not raised"
    except StackOverflowException:
        pass

    print()
    print("First part is done, should get 4 points for that.")

    # check peek function
    peek_stack = Stack(stack_capacity)
    peek_stack.push(item_1)
    assert peek_stack.peek() == item_1
    assert peek_stack.pop() == item_1, "item 1 should still be present in the stack"
    assert peek_stack.peek() is None, "empty_stack.peek() should return 0"

    # check is_empty function
    empty_stack = Stack(capacity=5)
    assert empty_stack.is_empty()

    stack_with_item_1 = Stack(5)
    stack_with_item_1.push(item_1)
    assert not stack_with_item_1.is_empty()

    # check is_full function
    full_stack = Stack(0)
    assert full_stack.is_full()

    not_full_stack = Stack(2)
    assert not not_full_stack.is_full()

    # check __str__ function
    assert str(empty_stack) == "Stack(capacity=5)"
    assert str(stack_with_item_1) == "Stack(capacity=5, top_element=first item)"

    print("Ready for submission!")
