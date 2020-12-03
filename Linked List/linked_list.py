class Node:
    def __init__(self, data, point=None):

        """
        Create Node that alows to store two data in head and pointer.
        Example : \n
        >>> node = Node(5)
        >>> node.point = Node(3)
        >>> node
        5-->3-->

        :param data: Values to be stored in head
        :param point: Values to be pointed
        :return: None
        """

        self.head = data
        self.point = point

    def __str__(self):
        if self.head is None:
            return 'Node is empty'
        else:
            itr = self
            string_itr = ''
            while itr:
                string_itr += f'{itr.head}-->'
                itr = itr.point
            return string_itr


class LinkedList:
    def __init__(self):

        """
        Initialize linked list class to used in instance
        Example : \n
        >>> linked_list = LinkedList()
        >>>  linked_list.to_linked([1, 2, 3])
        >>> linked_list
        1-->2-->3-->
        """

        self.node = None

    def __str__(self):
        if self.node is None:
            return 'Linked list is empty'
        else:
            itr = self.node
            string_itr = ''
            while itr:
                string_itr += f'{itr.head}-->'
                itr = itr.point
            return string_itr

    def __len__(self):
        if self.node is None:
            return 0
        else:
            counter = 0
            itr = self.node
            while itr:
                counter += 1
                itr = itr.point
            return counter

    def __iter__(self):
        itr = self.node
        while itr:
            yield itr
            itr = itr.point

    def to_linked(self, array):

        """
        Convert normal python iterable into linked list
        Example : \n
        >>> linked_list = LinkedList()
        >>> linked_list.to_linked([1,2,3])
        >>> linked_list
        1-->2-->3-->

        :param array: Iterable, ex : list, tuple, set
        :return: None
        """

        for i in array:
            self.append(i)

    def append(self, data):

        """
        Append data values from any type into linked list.\n
        Example:\n
        >>> linked_list = LinkedList()
        >>> linked_list.to_linked([1,2,3])
        >>> linked_list.append('Can be anything')
        >>> linked_list
        1-->2-->3-->Can be anything-->

        :param data: Values to be appended in any type.
        :return: None
        """

        if self.node is None:
            self.node = Node(data)
        else:
            itr = self.node
            while itr:
                if itr.point is None:
                    itr.point = Node(data)
                    break
                itr = itr.point

    def insert_start(self, data):

        """
        Insert values to linked list at the start (index zero)
        Example : \n
        >>> linked_list = LinkedList()
        >>> linked_list.to_linked([1, 2, 3])
        >>> linked_list.insert_start(7)
        >>> linked_list
        7-->1-->2-->3-->

        :param data: Values to be appended
        :return: None
        """

        if self.node is None:
            self.node = Node(data, None)
        else:
            self.node = Node(data, self.node)

    def insert_at(self, index, data):

        """
        Insert values into specific index of linked list
        Example : \n
        >>> linked_list = LinkedList()
        >>> linked_list.to_linked([1, 2, 3])
        >>> linked_list.insert_at(2,12)
        >>> linked_list
        1-->2-->12-->3-->

        :param index: Index / position of the linked list
        :param data: Values to be appended
        :return: None
        """

        if self.node is None:
            self.node = Node(data, None)
        else:
            counter = 0
            itr = self.node
            while itr:
                counter += 1
                if counter == index:
                    itr.point = Node(data, itr.point)
                    break
                itr = itr.point

    def remove_at(self, index):

        """
        Remove values from linked list by the index
        Example : \n
        >>> linked_list = LinkedList()
        >>> linked_list.to_linked([1, 2, 3])
        >>> linked_list.remove_at(2)
        >>> linked_list
        1-->2-->

        :param index: Index of linked list
        :return: None
        """

        if self.node is None:
            pass
        else:
            counter = 0
            itr = self.node
            while itr:
                counter += 1
                if counter == index:
                    itr.point = itr.point.point
                    break
                itr = itr.point


if __name__ == '__main__':
    li = LinkedList()
    li.to_linked([1, 2, 3])
    li.remove_at(2)

    print(f'Linked list : {li}')
    print(f'Len of linked list : {len(li)}')
