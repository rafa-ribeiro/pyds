from pyds.data_structures.stack import Stack
from collections import namedtuple
import pytest


def test_stack_instantiate():
    stack = Stack()
    assert type(stack) == Stack
    assert len(stack) == 0


def test_stack_instantiate_with_params():
    items = [1, 2, 3]
    stack = Stack(from_list=items)
    assert type(stack) == Stack
    assert len(stack) == len(items)
    top_item = stack.peek()
    assert top_item == 3


def test_stack_push():
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    assert len(stack) == 3
    item_on_top = stack.peek()
    assert item_on_top == 30


def test_stack_pop():
    stack = Stack(from_list=[10, 20])
    _ = stack.pop()
    stack.push(30)
    _ = stack.pop()
    top_item = stack.pop()
    assert top_item == 10
    top_item = stack.pop()
    assert top_item is None


StackBehaviorParam = namedtuple('StackBehaviorParam', 'items pops_amount expected_stack')

testdata = [
    StackBehaviorParam(items=[5, 6, 7], pops_amount=1, expected_stack=[5, 6]),
    StackBehaviorParam(items=[10, 20, 30], pops_amount=2, expected_stack=[10]),
    StackBehaviorParam(items=[100, 200, 300], pops_amount=0, expected_stack=[100, 200, 300]),
    StackBehaviorParam(items=[3, 5, 7], pops_amount=3, expected_stack=[]),
    StackBehaviorParam(items=None, pops_amount=1, expected_stack=[]),
]


@pytest.mark.parametrize("items, pops_amount, expected_stack", testdata)
def test_stack_behavior(items, pops_amount, expected_stack):
    stack = Stack(from_list=items)
    for _ in range(pops_amount):
        stack.pop()

    assert stack.to_list() == expected_stack


def test_stack_repr():
    items = [1, 4, 6]
    stack = Stack(from_list=items)
    assert repr(stack) == f"Stack(from_list={str(items)})"


def test_stack_str():
    items = [1, 4, 6]
    stack = Stack(from_list=items)
    assert str(stack) == f"{str(items)}"
