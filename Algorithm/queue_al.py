# 队列先进先出原则
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        return self.items.insert(0, item)  # 只能使用insert这样才能保证先进先出

    def dequeue(self):
        return self.items.pop()   # 删除并返回最后一个值

    def size(self):
        return len(self.items)

    def items_values(self):
        return self.items

q1 = Queue()
print(q1.isEmpty())

q1.enqueue(89)
q1.enqueue(100)
q1.enqueue(110)
q1.enqueue(120)
print(q1.isEmpty())

q1.dequeue()

print(q1.items_values())