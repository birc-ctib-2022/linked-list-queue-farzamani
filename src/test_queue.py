"""Testing queues."""
from queuex import Queue

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
    