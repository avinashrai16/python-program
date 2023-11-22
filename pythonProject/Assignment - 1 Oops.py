# Problem 6: Shape Calculation Create a class representing a shape with attributes like length, width, and height.
# Implement methods to calculate the area and perimeter of the shape.
# class Shape:
#     def __init__(self, length=0, width=0, height=0):
#         self.length = length
#         self.width = width
#         self.height = height
#
#     def calculate_area(self):
#         raise NotImplementedError("Subclasses must implement the calculate_area method")
#
#     def calculate_perimeter(self):
#         raise NotImplementedError("Subclasses must implement the calculate_perimeter method")
#
#
# class Rectangle(Shape):
#     def __init__(self, length, width):
#         super().__init__(length, width)
#
#     def calculate_area(self):
#         return self.length * self.width
#
#     def calculate_perimeter(self):
#         return 2 * (self.length + self.width)
#
#
# class Square(Rectangle):
#     def __init__(self, side):
#         super().__init__(side, side)
#
#
# class Triangle(Shape):
#     def __init__(self, base, height):
#         super().__init__(base, height)
#
#     def calculate_area(self):
#         return 0.5 * self.length * self.height
#
#     def calculate_perimeter(self):
#         # Perimeter calculation for a triangle may depend on the specific type of triangle (e.g., equilateral, isosceles, scalene).
#         raise NotImplementedError("Perimeter calculation for a general triangle is not implemented")
#
#
# # usage:
# rectangle = Rectangle(5, 8)
# print("Rectangle Area:", rectangle.calculate_area())
# print("Rectangle Perimeter:", rectangle.calculate_perimeter())
#
# square = Square(4)
# print("Square Area:", square.calculate_area())
# print("Square Perimeter:", square.calculate_perimeter())
#
# triangle = Triangle(3, 6)
# print("Triangle Area:", triangle.calculate_area())


# Problem 7: Student Management Create a class representing a student with attributes like student ID, name, and grades.
# Implement methods to calculate the average grade and display student details.
# class Student:
#     def __init__(self, student_id, name):
#         self.student_id = student_id
#         self.name = name
#         self.grades = []
#
#     def add_grade(self, grade):
#         self.grades.append(grade)
#
#     def calculate_average_grade(self):
#         if not self.grades:
#             return 0  # Return 0 if there are no grades
#         return round((sum(self.grades) / len(self.grades)), 2)
#
#     def display_student_details(self):
#         print(f"Student ID: {self.student_id}")
#         print(f"Name: {self.name}")
#         if self.grades:
#             print(f"Grades:{self.grades}")
#             print(f"Average Grade: {self.calculate_average_grade()}")
#         else:
#             print("No grades available for this student.")
#
#
# # usage:
# student1 = Student(student_id="12345", name="Student1")
# student1.add_grade(85)
# student1.add_grade(90)
# student1.add_grade(78)
#
# student2 = Student(student_id="67890", name="Student2")
# student2.add_grade(92)
# student2.add_grade(88)
# student2.add_grade(95)
#
# student1.display_student_details()
# print("\n")
# student2.display_student_details()


# Problem 8: Email Management Create a class representing an email with attributes like sender, recipient, and subject.
# Implement methods to send an email and display email details.

# class Email:
#     def __init__(self, sender, recipient, subject, body):
#         self.sender = sender
#         self.recipient = recipient
#         self.subject = subject
#         self.body = body
#         self.sent = False
#
#     def send_email(self):
#         print(f"Email sent from {self.sender} to {self.recipient} with subject '{self.subject}'")
#         self.sent = True
#
#     def display_email_details(self):
#         print("Email Details:")
#         print(f"Sender: {self.sender}")
#         print(f"Recipient: {self.recipient}")
#         print(f"Subject: {self.subject}")
#         print("Body:")
#         print(self.body)
#         if self.sent:
#             print("Status: Sent")
#         else:
#             print("Status: Not Sent")
#
#
# # usage:
# email = Email(sender="sender@example.com", recipient="recipient@example.com",
#               subject="Meeting Details", body="Hello, let's meet at 2 PM.")
#
# # Display email details before sending
# email.display_email_details()
# print("\n")
# # Send the email
# email.send_email()
# print("\n")
# # Display email details after sending
# email.display_email_details()

# Social Media Profile Create a class representing a social media profile with attributes like username and posts.
# Implement methods to add posts, display posts, and search for posts by keyword
# class SocialMediaProfile:
#     def __init__(self, username):
#         self.username = username
#         self.posts = []
#
#     def add_post(self, content):
#         post = {"content": content, "author": self.username}
#         self.posts.append(post)
#
#     def display_posts(self):
#         if not self.posts:
#             print(f"{self.username} has no posts.")
#         else:
#             print(f"Posts by {self.username}:")
#             for i, post in enumerate(self.posts, 1):
#                 print(f"Post {i}:")
#                 print(f"Author: {post['author']}")
#                 print(f"Content: {post['content']}")
#                 print("----")
#
#     def search_posts(self, keyword):
#         matching_posts = [post for post in self.posts if keyword.lower() in post['content'].lower()]
#         if not matching_posts:
#             print(f"No posts containing '{keyword}' found.")
#         else:
#             print(f"Posts by {self.username} containing '{keyword}':")
#             for i, post in enumerate(matching_posts, 1):
#                 print(f"Post {i}:")
#                 print(f"Author: {post['author']}")
#                 print(f"Content: {post['content']}")
#                 print("----")
#
#
# # usage:
# profile = SocialMediaProfile(username="avinash_rai")
#
# # Add posts
# profile.add_post("Just had a great workout at the gym!")
# profile.add_post("Enjoying a relaxing evening with a good book.")
# profile.add_post("Excited about the upcoming vacation!")
#
# # Display all posts
# profile.display_posts()
#
# # Search for posts containing the keyword "vacation"
# profile.search_posts(keyword="vacation")

# Problem 10: toDoList Create a class representing a ToDlist with attributes like tasks and due dates.
# Implement methods to add tasks, mark tasks as completed, and display pending tasks.
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task, due_date=None):
        new_task = {"task": task, "due_date": due_date, "completed": False}
        self.tasks.append(new_task)

    def mark_task_as_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["completed"] = True
            print(f'Task "{self.tasks[task_index]["task"]}" marked as completed.')
        else:
            print("Invalid task index.")

    def display_pending_tasks(self):
        pending_tasks = [task for task in self.tasks if not task["completed"]]
        if not pending_tasks:
            print("No pending tasks.")
        else:
            print("Pending tasks:")
            for i, task in enumerate(pending_tasks, 1):
                print(f"Task {i}:")
                print(f"Task: {task['task']}")
                if task["due_date"]:
                    print(f"Due Date: {task['due_date']}")
                print("----")

#usage:
to_do_list = ToDoList()

# Add tasks
to_do_list.add_task("Complete project", due_date="2023-01-31")
to_do_list.add_task("Buy groceries")
to_do_list.add_task("Read a chapter of a book")

# Display pending tasks
to_do_list.display_pending_tasks()
print("\n")
# Mark a task as completed
to_do_list.mark_task_as_completed(1)
print("\n")
# Display pending tasks after marking a task as completed
to_do_list.display_pending_tasks()


