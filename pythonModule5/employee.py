'''
Как сделать remove by email так и не понял
Остальные тесты проходят успешно
'''

class Employee:
    def __init__(self, first_name, last_name, salary):
        self.salary = int(salary)
        self.first_name = first_name.capitalize()
        self.last_name = last_name.capitalize()

    @property
    def email(self):
        return (self.first_name + "_" + self.last_name + "@example.com").lower()

    @property
    def full_name(self):
        return "{}, {}".format(self.first_name, self.last_name)

    @full_name.setter
    def full_name(self, full_name):
        self.first_name = full_name.split(", ")[0].capitalize()
        self.last_name = full_name.split(", ")[1].capitalize()

    @classmethod
    def from_str(cls, empl_str):
        return Employee(*empl_str.split(","))


class DevOps(Employee):
    def __init__(self, first_name, last_name, salary, skills=None):
        super().__init__(first_name, last_name, salary)
        if skills is None:
            self.skills = []
        else:
            self.skills = skills

    def add_skill(self, skill):
        if str(skill).capitalize() not in self.skills:
            self.skills.append(str(skill).capitalize())

    def remove_skill(self, skill):
        if str(skill).capitalize() in self.skills:
            self.skills.remove(str(skill).capitalize())
        else:
            self.skills = self.skills


class Manager(Employee):

    def __init__(self, first_name, last_name, salary, subordinates=None):
        super().__init__(first_name, last_name, salary)
        if subordinates is None:
            self.subordinates = []
        else:
            self.subordinates = subordinates

    def add_subordinate(self, emp):
        if emp not in self.subordinates:
            self.subordinates.append(emp)
        else:
            self.subordinates = self.subordinates

    def remove_subordinate(self, emp):
        if emp in self.subordinates:
            self.subordinates.remove(emp)
        else:
            self.subordinates = self.subordinates




