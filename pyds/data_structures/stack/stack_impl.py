from typing import Optional, List


class Stack:

    def __init__(self, from_list: Optional[List] = None):
        self.stack = from_list or []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop(-1) if len(self.stack) > 0 else None

    def __len__(self):
        return len(self.stack)

    def __repr__(self):
        return f"Stack(from_list={str(self.stack)})"

    def __str__(self):
        return f"{str(self.stack)}"

    def to_list(self):
        return self.stack

    def peek(self):
        try:
            top = self.stack[-1]
        except IndexError:
            top = None
        finally:
            return top
