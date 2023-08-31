#!/usr/bin/python3
"""Define classes for a singly linked list"""


class Node:
    """Represent a node in a singly-linked list"""


    def __init__(self, data, next_node=None):
        """Initialize a new Node
        
        Args:
            data (int): Data of Node
            next_node (Node): Node of the next new Node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get data of a Node"""
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get the next node of the Node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represent a singly-linked list"""


    def __str__(self):
        """Define print() representation of singly linked list"""
        rtn = ""
        ptr = self.__head

        while ptr is not None:
            rtn += str(ptr.data)
            if ptr.next_node is not None:
                rtn += "\n"
            ptr = ptr.next_node

        return rtn

    def __init__(self):
        """Initialize a new singly linked list"""
        self.__head = None

    def sorted_insert(self, value):
        """Insert new Node into singly linked list
        New Node is in an ordered manner

        Args:
            value (Node): New Node to insert
        """
        ptr = self.__head

        while ptr is not None:
            if ptr.data > value:
                break
            ptr_prev = ptr
            ptr = ptr.next_node

        newNode = Node(value, ptr)
        if ptr == self.__head:
            self.__head = newNode
        else:
            ptr_prev.next_node = newNode
