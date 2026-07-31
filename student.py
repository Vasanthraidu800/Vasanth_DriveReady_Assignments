class Student:
    college_name = "Aditya Institute of Technology"
    total_students = 0
    PASS_MARK = 35
    MAX_SUBJECTS = 5

    def __init__(self, roll_number, name, branch):
        """Initialize a Student object."""
        self._roll_number = roll_number
        self.name = name
        self._branch = branch
        self.__marks = {}

        Student.total_students += 1

    @property
    def roll_number(self):
        """Return the student's roll number."""
        return self._roll_number

# average and grade are not stored as separate variables.
# They are calculated every time the properties are accessed using the
# current contents of __marks.
# Therefore, when new marks are added, the next time average or grade is
# accessed, the calculation uses the updated marks automatically.
# This makes a stale-grade bug impossible because there is no old grade
# value stored that could become out of date.
    @property
    def average(self):
        """Calculate and return the average of the marks."""
        if len(self.__marks) == 0:
            return 0.0

        return sum(self.__marks.values()) / len(self.__marks)

    @property
    def grade(self):
        """Calculate and return the grade from the current average."""
        avg = self.average

        if avg >= 90:
            return "A+"
        elif avg >= 75:
            return "A"
        elif avg >= 60:
            return "B"
        elif avg >= Student.PASS_MARK:
            return "C"
        else:
            return "F"

    def add_marks(self, subject, mark):
        """Validate and add marks for a subject."""
        if not isinstance(mark, (int, float)):
            raise TypeError("Mark must be a number")

        if mark < 0 or mark > 100:
            raise ValueError(
                f"Mark must be between 0 and 100, got {mark}"
            )

        if subject not in self.__marks and len(self.__marks) >= Student.MAX_SUBJECTS:
            raise ValueError(
                f"Cannot have more than {Student.MAX_SUBJECTS} subjects"
            )

        self.__marks[subject] = mark

    def get_marks(self):
        """Return a copy of the student's marks."""
        return dict(self.__marks)

    def has_passed(self):
        """Return True only if every subject has passing marks."""
        if len(self.__marks) == 0:
            return False

        for mark in self.__marks.values():
            if mark <= Student.PASS_MARK:
                return False

        return True

    def change_branch(self, new_branch):
        """Change the student's branch."""
        old_branch = self._branch
        self._branch = new_branch

        return f"{self.name} moved from {old_branch} to {new_branch}"

    @classmethod
    def get_total_students(cls):
        """Return the total number of students."""
        return cls.total_students

    @staticmethod
    def is_valid_mark(mark):
        """Check whether a mark is between 0 and 100."""
        return isinstance(mark, (int, float)) and 0 <= mark <= 100

    def __str__(self):
        """Return a readable student summary."""
        return (
            f"Student[{self.roll_number}] {self.name} | "
            f"{self._branch} | Avg: {self.average:.2f} | "
            f"Grade: {self.grade}"
        )


def main():
    """Demonstrate all Student class requirements."""

    print("College:", Student.college_name)

    s1 = Student(101, "Ravi Kumar", "CSE")
    s2 = Student(102, "Anita Sharma", "ECE")

    s1.add_marks("Maths", 92)
    s1.add_marks("Physics", 88)
    s1.add_marks("Chemistry", 76)

    s2.add_marks("Maths", 40)
    s2.add_marks("Physics", 35)

    print("Total students:", Student.get_total_students())

    print(s1)
    print(s2)

    print("s1 marks :", s1.get_marks())
    print("s1 passed :", s1.has_passed())
    print("s2 passed :", s2.has_passed())

    print(s1.change_branch("IT"))

    print("is_valid_mark(105):", Student.is_valid_mark(105))

    try:
        s1.add_marks("Biology", 150)
    except ValueError as e:
        print("Blocked (mark 150):", e)

    try:
        s1.average = 99
    except AttributeError as e:
        print("Blocked (write average):", e)

    try:
        s1.roll_number = 999
    except AttributeError as e:
        print("Blocked (write roll):", e)

    marks = s1.get_marks()
    marks["Maths"] = 0

    # print("s1 marks after modifying copy :", s1.get_marks())

    print("protected :", s1._branch)
    print("private :", s1._Student__marks)


if __name__ == "__main__":
    main()