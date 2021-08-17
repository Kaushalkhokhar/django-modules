from django.db import models

"""
Part 1 OneToOne Ralationship
"""
class Student(models.Model):
    name = models.CharField(max_length=25)
    age = models.IntegerField()


    def __str__(self):
        return self.name

class StudentResult(models.Model):

    student = models.OneToOneField(Student, on_delete=models.CASCADE, primary_key=True)

    # student = models.OneToOneField(Student, on_delete=models.PROTECT, primary_key=True)
    # here, protect will not allow to delete student before deleting the result associated with that students
    # means, we need to first delete the result of that student then we can delete the studen

    # student = models.OneToOneField(Student, on_delete=models.PROTECT, primary_key=True,
    #                                         limit_choices_to={'name__contains': 'a'})
                                            # here we have limited the user can create result table
                                            # only name which contains a letter a can allow to add result
    marks = models.IntegerField()

# we also implemented a reverse deletion using the signal
# means, when we delete result row then student associated with that
# row will be deleted

class ResultColor(StudentResult):
    result = models.OneToOneField(StudentResult, on_delete=models.CASCADE, primary_key=True, parent_link=True)
    # here we have used multitable model inheritance, which links onetoone field between two table by default
    # but here we have assigned it by our self with parent_link=True 
    color = models.CharField(max_length=25, choices=[('Red', 'Red'),
                                                     ('Blue', 'Blue'),   
                                                    ])
                                                

"""
Part 2 ManyToOne Relationships
"""

class Subject(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    # student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='sub') 
    # here, related_name is used when we use filter on subject model

    # student = models.ForeignKey(Student, on_delete=models.PROTECT)
    # student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    # here it sets the null value to student column if student of that column is deleted

    subject = models.CharField(max_length=25)

    def __str__(self):
        return self.subject



"""
Part 3 ManyToMany Relationships
"""

class Teacher(models.Model):
    student = models.ManyToManyField(Student)
    name = models.CharField(max_length=25)

    def student_list(self):
        return ','.join([str(s) for s in self.student.all()])
    # this is added to list_display in admin.py to see the list of students

# to retrive teahcer from studetn object we can user teahcer_set method
# i.e student.teacher_set.all()