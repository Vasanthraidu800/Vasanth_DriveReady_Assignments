class Employee:
    company_name = "TechCorp Solutions"
    total_employees = 0
    pf_percentage = 12.0
    MIN_SALARY = 15000
    MAX_SALARY = 500000

    def __init__(self, emp_id, name, department, salary):
        """Initialize an Employee object."""
        self._emp_id = emp_id
        self.name = name
        self._department = department
        self.__pan_number = "ABCDE1234F"

        self.salary = salary

        Employee.total_employees += 1

    @property
    def emp_id(self):
        """Return the employee ID."""
        return self._emp_id

    @property
    def salary(self):
        """Return the employee salary."""
        return self._salary

    @salary.setter
    def salary(self, value):
        """Validate and set the employee salary."""
        if not isinstance(value, (int, float)):
            raise TypeError("Salary must be a number")

        if value < Employee.MIN_SALARY or value > Employee.MAX_SALARY:
            raise ValueError(
                f"Salary must be between {Employee.MIN_SALARY} "
                f"and {Employee.MAX_SALARY}, got {value}"
            )

        self._salary = value

    def apply_hike(self, percent):
        """Increase salary by the given percentage."""
        if percent < 0 or percent > 50:
            raise ValueError("Hike percentage must be between 0 and 50")

        self.salary = self.salary + (self.salary * percent / 100)

        return self.salary

    def calculate_pf(self):
        """Calculate provident fund using the company PF percentage."""
        return self.salary * Employee.pf_percentage / 100

    def transfer_department(self, new_dept):
        """Transfer the employee to a new department."""
        old_dept = self._department
        self._department = new_dept

        return f"{self.name} moved from {old_dept} to {new_dept}"

    @classmethod
    def get_total_employees(cls):
        """Return the total number of employees."""
        return cls.total_employees

    @staticmethod
    def is_valid_salary(amount):
        """Check whether a salary is valid."""
        if not isinstance(amount, (int, float)):
            return False

        return Employee.MIN_SALARY <= amount <= Employee.MAX_SALARY

    def __str__(self):
        """Return a readable employee summary."""
        return (
            f"Employee[{self.emp_id}] {self.name} | "
            f"{self._department} | Rs.{self.salary:,.2f}"
        )


def main():
    """Demonstrate all Employee class requirements."""

    print("Company:", Employee.company_name)
    print("Employees before:", Employee.get_total_employees())

    e1 = Employee(101, "Ravi Kumar", "Engineering", 60000)
    e2 = Employee(102, "Anita Sharma", "Finance", 75000)

    print(e1)
    print(e2)

    print("Employees after:", Employee.get_total_employees())

    print("PF for e1:", e1.calculate_pf())

    print("After 10% hike:", e1.apply_hike(10))

    print(e1.transfer_department("Data Science"))

    print("is_valid_salary(9000):", Employee.is_valid_salary(9000))

    try:
        e1.salary = 5000
    except ValueError as e:
        print("Blocked:", e)

    try:
        e1.emp_id = 999
    except AttributeError as e:
        print("Blocked:", e)

    # _department is a protected attribute. The single underscore is only a
    # naming convention that tells programmers it is intended for internal use.
    # Python does not actually prevent access from outside the class.
    #
    # __pan_number is a private attribute. Python changes its name internally
    # using name mangling, so __pan_number becomes _Employee__pan_number.
    # Therefore, it can still be accessed from outside using the mangled name.
    # The double underscore mainly prevents accidental access/name conflicts;
    # it does not provide true private access control.

    print("protected :", e1._department)

    print("private :", e1._Employee__pan_number)


if __name__ == "__main__":
    main()