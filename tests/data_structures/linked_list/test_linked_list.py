from pyds.data_structures.linked_list import LinkedList


def test_linked_list_instantiate():
    linked_list = LinkedList()
    assert type(linked_list) is LinkedList
    assert linked_list.head is None
    assert len(linked_list) == 0


def test_append_new_item():
    linked_list = LinkedList()
    linked_list.append(10)
    assert len(linked_list) == 1
    assert linked_list.head.value == 10
    assert linked_list.tail.value == 10


def test_append_n_items():
    linked_list = LinkedList()
    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)
    linked_list.append(40)
    assert len(linked_list) == 4
    assert linked_list.head.value == 10
    assert linked_list.tail.value == 40


def test_append_n_items_with_duplicated_elements():
    linked_list = LinkedList()
    linked_list.append(5)
    linked_list.append(15)
    linked_list.append(25)
    linked_list.append(5)
    assert len(linked_list) == 4
    assert linked_list.head.value == 5
    assert linked_list.tail.value == 5


def test_iterator():
    linked_list = LinkedList()
    items_to_add = [1, 2, 3, 4, 5]

    for value in items_to_add:
        linked_list.append(value)

    for idx, item in enumerate(linked_list):
        assert item == items_to_add[idx]


def test_delete_value_on_head():
    linked_list = LinkedList()
    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)

    assert len(linked_list) == 3
    linked_list.delete(10)
    assert len(linked_list) == 2
    assert linked_list.head.value == 20


def test_delete_value_on_tail():
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    assert len(linked_list) == 3

    linked_list.delete(3)
    assert len(linked_list) == 2
    assert linked_list.tail.value == 2


def test_delete_on_tail():
    linked_list = LinkedList()
    linked_list.append(5)
    linked_list.append(55)
    linked_list.append(105)
    linked_list.append(155)
    assert len(linked_list) == 4

    linked_list.delete_tail()
    assert len(linked_list) == 3
    assert linked_list.tail.value == 105


def test_delete_on_tail_with_duplicated_elements():
    linked_list = LinkedList()
    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(35)
    linked_list.append(20)
    assert len(linked_list) == 4

    linked_list.delete_tail()
    assert len(linked_list) == 3
    assert linked_list.tail.value == 35


def test_delete_all_elements_on_tail():
    linked_list = LinkedList()
    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)
    assert len(linked_list) == 3

    linked_list.delete_tail()
    linked_list.delete_tail()
    linked_list.delete_tail()
    linked_list.delete_tail()
    assert len(linked_list) == 0
    assert linked_list.head is None
    assert linked_list.tail is None


def test_delete_value_between():
    linked_list = LinkedList()
    linked_list.append(50)
    linked_list.append(75)
    linked_list.append(100)
    assert len(linked_list) == 3

    linked_list.delete(75)
    assert len(linked_list) == 2
    assert linked_list.head.value == 50
    assert linked_list.tail.value == 100


def test_delete_value_with_duplicated_elements():
    linked_list = LinkedList()
    linked_list.append(99)
    linked_list.append(111)
    linked_list.append(222)
    linked_list.append(99)
    assert len(linked_list) == 4

    linked_list.delete(99)
    assert len(linked_list) == 3
    assert linked_list.head.value == 111
    assert linked_list.tail.value == 99


def test_delete_invalid_value():
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    assert len(linked_list) == 3

    linked_list.delete(75)
    assert len(linked_list) == 3


def test_with_different_value_object():
    linked_list = LinkedList()
    linked_list.append("Goku")
    linked_list.append("Vegetta")
    linked_list.append("Gohan")
    assert len(linked_list) == 3

    linked_list.delete("Vegetta")
    assert len(linked_list) == 2
    assert linked_list.head.value == "Goku"
    assert linked_list.tail.value == "Gohan"


def test_remove_all_objects():
    linked_list = LinkedList()
    linked_list.append("Sub-Zero")
    linked_list.append("Scorpion")
    assert len(linked_list) == 2

    linked_list.delete("Scorpion")
    linked_list.delete("Sub-Zero")
    assert len(linked_list) == 0
    assert linked_list.head is None
    assert linked_list.tail is None


def test_remove_first_element_from_list_size_2():
    linked_list = LinkedList()
    linked_list.append("Ken")
    linked_list.append("Ryu")
    assert len(linked_list) == 2

    linked_list.delete("Ken")
    assert len(linked_list) == 1
    assert linked_list.head.value == "Ryu"
    assert linked_list.tail == linked_list.head


def test_remove_last_element_from_list_size_2():
    linked_list = LinkedList()
    linked_list.append("Shiryu")
    linked_list.append("Seiya")
    assert len(linked_list) == 2

    linked_list.delete("Seiya")
    assert len(linked_list) == 1
    assert linked_list.head.value == "Shiryu"
    assert linked_list.tail.value == linked_list.head.value
