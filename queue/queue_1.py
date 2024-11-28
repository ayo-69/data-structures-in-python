class _Queue:
    def __init__(self, size):
        self.queue = []

    def enqueue(self, data):
        self.queue.insert(0, data)

    def dequeue(self):
        self.queue.pop()

test = _Queue(3)
print(test.queue)

test.enqueue("Hello")
test.enqueue("world")
test.enqueue("booyah")
test.enqueue("")

print(test.queue)

test.dequeue()

print(test.queue)