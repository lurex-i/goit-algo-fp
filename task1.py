# Для реалізації однозв'язного списку (приклад реалізації можна взяти з конспекту) необхідно:
# написати функцію, яка реалізує реверсування однозв'язного списку, змінюючи посилання між вузлами;
# розробити алгоритм сортування для однозв'язного списку, наприклад, сортування вставками або 
# злиттям; написати функцію, що об'єднує два відсортовані однозв'язні списки в один 
# відсортований список.

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(f"{current.data} ->", end=' ')
            current = current.next
        print("end")

    # head -> 0 -> 1 -> 2 -> none
    # none <- 0 <- 1 <- 2 <- head
    def reverse(self):
        def reverse_item(prev, curr):
            if curr == None:
                return curr
            tmp = curr.next
            curr.next = prev
            return (curr, tmp)

        if self.head == None or self.head.next == None:
            return
        prev = self.head
        curr = prev.next
        while curr:
            prev, curr = reverse_item(prev, curr)
            if curr == None:
                break

        self.head.next = None
        self.head = prev


    def sort(self):
        if self.head == None or self.head.next == None:
            return
        prev = self.head
        nxt = prev.next
        while nxt:
            if nxt.data < prev.data:
                # remove nxt node and paste it into appropriate place of sorted part of the linked list
                prev.next = nxt.next
                curr = self.head
                if nxt.data < curr.data:
                    nxt.next = self.head
                    self.head = nxt
                else:
                    while curr.next:
                        if nxt.data < curr.next.data:
                            nxt.next = curr.next
                            curr.next = nxt
                            break
                        curr = curr.next
            else:
                prev = nxt
            nxt = prev.next    

    def extend(self, other):
        if other.head == None:
            return
        if self.head == None:
            self.head = other.head
            return

        a = self.head
        b = other.head
        # first case to define a new head
        if a.data < b.data:
            self.head = a
            a = a.next
        else:
            self.head = b
            b = b.next
        curr = self.head

        while a and b:
            if a.data < b.data:
                curr.next = a
                curr = a
                a = a.next
            else:
                curr.next = b
                curr = b
                b = b.next
        # Now connetct curr to the remain linked list
        curr.next = a if a else b


if __name__ == '__main__':
    llist = LinkedList()

    # Вставляємо вузли в початок
    llist.insert_at_beginning(5)
    llist.insert_at_beginning(10)
    llist.insert_at_beginning(15)

    # Вставляємо вузли в кінець
    llist.insert_at_end(20)
    llist.insert_at_end(25)

    # Друк зв'язного списку
    print("Зв'язний список:")
    llist.print_list()

    llist.reverse()
    print("\nЗв'язний список після реверсу:")
    llist.print_list()

    llist.sort()
    print("\nЗв'язний список після сортування:")
    llist.print_list()

    llist2 = LinkedList()
    llist2.insert_at_end(5)
    llist2.insert_at_end(14)
    llist2.insert_at_end(7)
    llist2.insert_at_end(23)
    llist2.sort()
    print("\nДругий відсортований зв'язний список до додавання до першого:")
    llist2.print_list()

    llist.extend(llist2)
    print("\nЗв'язний список після додавання іншого зв'язаного списку:")
    llist.print_list()
