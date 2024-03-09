class Task:
    _id_counter = 0  # Class variable to keep track of the last used ID

    def __init__(self, description, programmer, workload):
        Task._id_counter += 1  # Increment the class-wide ID counter for each new instance
        self.id = Task._id_counter  # Assign the current ID value to this instance
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.is_finished_flag = False  # Initially, the task is not finished

    def is_finished(self):
        return self.is_finished_flag

    def mark_finished(self):
        self.is_finished_flag = True

    def __str__(self):
        # Create a string representation of the Task instance
        status = "FINISHED" if self.is_finished_flag else "NOT FINISHED"
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {status}"

# Using the Task class
t1 = Task("program hello world", "Eric", 3)
print(t1.id, t1.description, t1.programmer, t1.workload)
print(t1)
print(t1.is_finished())
t1.mark_finished()
print(t1)
print(t1.is_finished())

t2 = Task("program webstore", "Adele", 10)
t3 = Task("program mobile app for workload accounting", "Eric", 25)
print(t2)
print(t3)
