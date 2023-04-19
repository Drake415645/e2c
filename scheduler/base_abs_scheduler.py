"""
TODO: Add description
"""
from queue import Queue
from abs import ABC, abstractmethod

from task.task import Task
from machine.machine import Machine


class baseAbsScheduler(ABC):
    """
    TODO: Class description
    """

    def __init__(self, name: str) -> None:
        super().__init__()
        self._name = name
        # self._stats =
        self._queue = Queue()

    @property
    def name(self) -> str:
        return self._name    
    
    @name.setter
    def name(self, name: str):
        if not isinstance(name, str):
            raise TypeError('Name must be a string')
        self._name = str(name)

    @property
    def stats(self) -> dict:
        return self._stats

    @stats.setter
    def stats(self, stats: dict):
        if not isinstance(stats, dict):
            raise TypeError('Stats must be a dictionary')
        self._stats = stats

    @property
    def queue(self) -> Queue:
        return self._queue
    
    @queue.setter
    def queue(self, queue: Queue):
        if not isinstance(queue, Queue):
            raise TypeError('Queue must be a Queue Type')
        self._queue = queue



    def choose(self) -> Task:
        #assume fcfs
        task = self._queue.pop()
        return task
    
    def admit(self, task: Task) -> bool:
        pass

    def allocate(self, task: Task) -> Machine:
        machine.running = task
        
    def schedule(self, task: Task):  
        task = self.choose()

        if machine.is_empty():
            machine = self.allocate(task)
    
    def defer(self, task: Task):
        pass

    def prune(self) ->list[Task]:
        pass

    def is_empty(self) -> bool:
        if machine.running:   #how to see if machine is empty? i dont know how to access "machine", should it be defined in the init?
            return False
        return True

    def q_completion_time(self) -> float:
        pass
