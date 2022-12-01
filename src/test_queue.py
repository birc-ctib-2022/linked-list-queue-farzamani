"""Testing queues."""
from queuex import Queue, Dequeue

def test_me() -> None:
    """Remember to write tests."""
    assert 2 + 2 == 4

    my_queue = Queue()
    assert my_queue.is_empty() == True

    my_queue.enqueue(10)
    assert my_queue.is_empty() == False
    assert my_queue.front() == 10

    my_queue.enqueue(20)
    assert my_queue.front() == 10

    my_queue.enqueue(30)
    assert my_queue.front() == 10

    assert 10 == my_queue.dequeue()
    assert 20 == my_queue.dequeue()
    assert 30 == my_queue.dequeue()

    assert my_queue.is_empty() == True

def test_dequeue():
    my_dequeue = Dequeue()
    assert my_dequeue.is_empty() == True
    assert my_dequeue.front() == None
    assert my_dequeue.back() == None

    my_dequeue.enqueue(10)
    my_dequeue.enqueue(20)
    my_dequeue.enqueue(30)
    my_dequeue.enqueue(40)
    my_dequeue.enqueue(50)
    my_dequeue.enqueue(60)
    my_dequeue.enqueue(70)

    assert my_dequeue.is_empty() == False
    assert my_dequeue.front() == 10
    assert my_dequeue.back() == 70

    front, back = my_dequeue.dequeue()
    assert front == 10
    assert back == 70
    assert my_dequeue.front() == 20
    assert my_dequeue.back() == 60
    
    front, back = my_dequeue.dequeue()
    assert front == 20
    assert back == 60
    assert my_dequeue.front() == 30
    assert my_dequeue.back() == 50

    my_dequeue.enqueue(60)

    front, back = my_dequeue.dequeue()
    assert front == 30
    assert back == 60
    assert my_dequeue.front() == 40
    assert my_dequeue.back() == 50

    front, back = my_dequeue.dequeue()
    assert front == 40
    assert back == 50
    assert my_dequeue.is_empty() == True
    assert my_dequeue.front() == None
    assert my_dequeue.back() == None


