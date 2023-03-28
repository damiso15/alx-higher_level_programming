#!/usr/bin/python3
"""
A class Node that defines a node of a singly linked list
"""


class Node:
    """
    A Singly Linked List Node with the following attributes:
    Private instance attribute: data
    Private instance attribute: next_node
    Instantiation with data and next_node
    """

    def __init__(self, data, next_node=None):
        """ Instantiation with data and next_node """

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ The property for the data method to retrieve it """

        return self.__data

    @data.setter
    def data(self, value):
        """ The property for the data method to set it """

        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ The property for the next_node method to retrieve it """

        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ The property for the data method to set it """

        if value is None or type(value) is Node:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


"""
a class SinglyLinkedList that defines a singly linked list
"""


class SinglyLinkedList:
    """
    A Singly Linked List with the following attributes:
    Private instance attribute: head (no getter, no setter)
    Public instance method: sorted_insert
    Simple instantiation
    """

    def __init__(self):
        """ Simple instantiation of the private instance attribute head """

        self.head = None

    def sorted_insert(self, value):
        """
        The sorted_insert method takes a value parameter and inserts
        a new node with that value into the correct sorted position
        in the linked list. If the list is empty, it sets the new
        node as the head. If the value is less than the head's value,
        it sets the new node as the head. Otherwise, it traverses the
        list until it finds the correct position to insert the new node
        """

        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return

        if self.head.data > value:
            new_node.next_node = self.head
            self.head = new_node
            return

        current = self.head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node
        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """
        __str__ method that prints the entire linked list by traversing
        the nodes from the head to the end and concatenating their
        values with newline characters
        """

        result = ""
        current = self.head
        while current:
            result += str(current.data) + "\n"
            current = current.next_node

        return result[:-1]
