from src.todo_list import TodoList
from src.task import Task

import unittest

class TestTodoList(unittest.TestCase):

    def test_A(self):
        t1 = Task(1,"t1",False)
        
        self.assertEqual(t1.__str__(),"Task 1: t1 (Priority: False, Not Done)")
    

    def test_C(self):
        t1 = Task(1,"t1",completed=False)
        self.assertEqual(t1.is_completed(),False)

    def test_C_completed_true(self):
        t1 = Task(1,"t1")
        t1.complete_task()
        self.assertEqual(t1.is_completed(),True)
    
    # def test_C_init_true(self):
    #     t1 = Task(1,"t1",completed=True)
    #     self.assertEqual(t1.is_completed(),True)
    # def test_C_init_false(self):
    #     t1 = Task(1,"t1")
    #     self.assertEqual(t1.completed,False)
    
    # def test_C_check_complete_task(self):
    #     t1 = Task(1,"t1")
    #     t1.complete_task()
    #     self.assertEqual(t1.completed,True)
    # def test_C_check_not_complete_task(self):
    #     t1 = Task(1,"t1")
    #     self.assertEqual(t1.completed,False)
    
    
    def test_B(self):
        t1 = Task(2,"t2")
        self.assertEqual(t1.__str__(),"Task 2: t2 (Priority: 1, Not Done)")
    
    def test_B_completed(self):
        t1 = Task(2,"t2")
        t1.complete_task()
        self.assertEqual(t1.__str__(),"Task 2: t2 (Priority: 1, Done)")

    # def test_B_diferent_id(self):
    #     t1 = Task(9,"t2")
    #     t1.complete_task()
    #     self.assertEqual(t1.__str__(),"Task 9: t2 (Priority: 1, Done)")
    
    # def test_B_diferent_descript(self):
    #     t1 = Task(2,"roar and fight")
    #     t1.complete_task()
    #     self.assertEqual(t1.__str__(),"Task 2: roar and fight (Priority: 1, Done)")
    
    # def test_B_diferent_prio(self):
    #     t1 = Task(2,"t2",priority=3)
    #     self.assertEqual(t1.__str__(),"Task 2: t2 (Priority: 3, Not Done)")