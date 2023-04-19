"""

TODO: add description

"""
from queue import Queue

from task.task import Task
from machine.machine import Machine

class Scheduler:
    """
    
    TODO: add description

    """

    def choose(self) -> Task:
        #for fcfs
        task = Queue.pop()
    
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
        if machine.running:        #how to see if machine is empty? i dont know how to access "machine", should it be defined in the init?
            return False
        return True

    def q_completion_time(self) -> float:
        pass
