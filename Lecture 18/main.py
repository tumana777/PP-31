# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# class Stack:
#     def __init__(self):
#         self.top = None
#         self.size = 0
#
#     def empty(self):
#         return self.size == 0
#
#     def peek(self):
#         if self.empty():
#             return "Stack is empty"
#         return self.top.data
#
#     def push(self, data):
#         new_node = Node(data)
#
#         new_node.next = self.top
#         self.top = new_node
#         self.size += 1
#
#     def pop(self):
#
#         if self.empty():
#             return "Stack is empty"
#
#         popped_element = self.top.data
#
#         self.top = self.top.next
#         self.size -= 1
#         return popped_element
#
# stack = Stack()
# # print(stack.empty())
# # print(stack.peek())
# stack.push(10)
# stack.push(9)
# # print(stack.peek())
# stack.push(12)
# stack.push(15)
# # print(stack.peek())
#
# stack.pop()
# print(stack.pop())
# print(stack.pop())
# print(stack.peek())


#  10 -> 9 -> 12 -> 15


# from collections import deque
#
# q = deque(maxlen=3)

# q.append(10)
# q.append(9)
# q.append(12)
# q.append(15)
# q.appendleft(25)
# q.appendleft(16)

# print(q.pop())
# print(q.popleft())

# print(list(q))


# from queue import Queue
#
# q = Queue()
#
# q.put(10)
# q.put(9)
# q.put(12)
# q.put_nowait(15)
#
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.get_nowait())
#
# print(list(q.queue))


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

                    # 10    11
    def _insert(self, node, key):
        if node is None:
            return Node(key)

        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)

        return node

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _print_parents(self, node, parent):
        if node:
            if parent is None:
                print(node.key, "-> Root")
            else:
                print(node.key, "-> ", parent.key)

            self._print_parents(node.left, node)
            self._print_parents(node.right, node)

    def print_parents(self):
        print("Parents are: ")
        self._print_parents(self.root, None)


                                              # 10
                                          # 9          12

                                                    # 11    13

bst = BST()
bst.insert(10)
bst.insert(12)
bst.insert(11)
bst.insert(9)
bst.insert(13)
bst.print_parents()













