""" Basic class registration program """


class StudentError(Exception):
    """ Custom exception class """
    pass


class ClassList:
    """
    Class registration system. Can create a class, add students, remove students.
    Student names in a class must be unique.
    """

        # raise an exception - StudentError - if max_students is zero or negative. 
        # Write test to confirm.

    def __init__(self, max_students):
        if max_students <= 0:
            raise StudentError('Number of students must be greater than 0')
        
        self.class_list = []
        self.max_students = max_students





    def add_student(self, student):
        """ Add student if there is space in the class,
        Raises Error if student is already in the list """
        if len(self.class_list) < self.max_students:
            if student not in self.class_list:
                self.class_list.append(student)
            else:
                raise StudentError('Student %s already enrolled, can\'t add again' % student)


    def remove_student(self, student):
        """ Remove student from class list. Raises Error if student not in list """
        if student not in self.class_list:
            raise StudentError('Student %s not found in class' % student)

        self.class_list.remove(student)


    def is_enrolled(self, student):
        """ Verifies if the student is enrolled or not """
        return student in self.class_list


    def index_of_student(self, student):
        """ Returns position of student in list, indexed from 1
        Returns None if student not present """
        if student in self.class_list:
            return self.class_list.index(student) + 1
        return None


    ## TODO add a method called is_class_full.
    # This should return True or False to indicate if the class is full.
    def is_class_full(class_list, max_students):
        # len(class_list) is not a valid function, because it is asking about the number of objects in a group of objects
        # max_students is the number given to this group of objects, so we can reference that. 
        number_of_students = 0
        for student in class_list:
            number_of_students += 1
        
        if number_of_students >= max_students: # because students can be might be past maximum "theoretically".
            return True
        else:
            return False


    def __str__(self):
        return ", ".join(self.class_list)


def main():

    ## Examples of using the program

    capstone = ClassList(5)
    capstone.add_student('Anna')
    capstone.remove_student('Anna')

    capstone.add_student('Anna')
    capstone.add_student('Bob')
    capstone.add_student('Cathy')
    try:
        capstone.add_student('Cathy')   # Second Cathy not added
    except:
        print('Did not add student twice')

    capstone.add_student('David')
    print(f'888 {capstone}')
    capstone.add_student('Elliot')
    capstone.add_student('Flora')  # Shouldn't add

    try:
        capstone.remove_student('Gus') # not present
    except:
        print('Attempt to remove student not enrolled')

    print(capstone)
    print(capstone.is_enrolled('Bob'))    # True
    print(capstone.is_enrolled('Flora'))  # False

    print('Anna is at position', capstone.index_of_student('Anna') ) ## 4
    print('Alex is at position', capstone.index_of_student('Alex') ) ## None


if __name__ == '__main__':
    main()
