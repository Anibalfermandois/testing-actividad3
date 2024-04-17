from src.todo_list import TodoList
from src.todo_list import Task

import unittest

class TestTodoList(unittest.TestCase):

    def setUp(self):
        self.list=TodoList()
        self.fulllist=TodoList()
        self.fulllist.add_task("T1")
        self.fulllist.add_task("T2")
        self.fulllist.add_task("T3")

    def test_A(self):
        list = self.list.list_tasks()
        self.assertEqual([],list)
    
    def test_A_empty1(self):
        self.assertEqual(self.list.remove_task(1),"Task 1 not found.")
    def test_A_empty2(self):
        self.assertEqual(self.list.complete_task(1),"Task 1 not found.")
    
    def test_add_list_return(self):
        new_task=self.list.add_task("T1")
        self.assertIsInstance(new_task,Task)

    def test_add_list_return_id(self):
        new_task=self.list.add_task("T1")
        self.assertEqual(new_task.task_id,1)
    def test_add_list_return_id2(self):
        new_task=self.fulllist.add_task("T4")
        self.assertEqual(new_task.task_id,4)
        
    def test_add_list_to_atribute(self):
        new_task=self.list.add_task("T1")
        expected_task=self.list.tasks[0]
        self.assertIs(new_task,expected_task)
    
    def test_add_list2(self):
        self.list.add_task("T1")
        self.list.add_task("T2")
        new_task=self.list.tasks[1]
        self.assertEqual(new_task.task_id,2)

    def test_remove_check(self):
        initial=self.fulllist.list_tasks()
        self.fulllist.remove_task(2)
        final=self.fulllist.list_tasks()
        self.assertNotEqual(len(initial),len(final))
    def test_remove_check_exact(self):
        initial=self.fulllist.list_tasks()
        initial.pop(1)
        self.fulllist.remove_task(2)
        final=self.fulllist.list_tasks()
        self.assertEqual(initial,final)

    def test_remove_text(self):
        out:str=self.fulllist.remove_task(1)
        self.assertEqual("Task 1 removed.",out)
    def test_remove_text2(self):
        out:str=self.list.remove_task(1)
        self.assertEqual("Task 1 not found.",out)

    def test_complete_task_return(self):
        out:str=self.fulllist.complete_task(1)
        self.assertEqual("Task 1 marked as done.",out)
    
    def test_complete_task_completed(self):
        inicial_value=self.fulllist.tasks[0].completed
        self.fulllist.complete_task(1)
        new_value=self.fulllist.tasks[0].completed
        self.assertNotEqual(inicial_value,new_value)

    def test_priority_list_empty(self):
        self.assertEqual(self.list.find_high_priority_tasks(0),[])
    
    def test_priority_list(self):
        self.fulllist.tasks[2].priority=3
        self.fulllist.tasks[1].priority=2
        self.assertEqual(self.fulllist.find_high_priority_tasks(2),[self.fulllist.tasks[2]])