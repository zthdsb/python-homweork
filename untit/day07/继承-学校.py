class School(object):
    def __init__(self,name,addr):
        self.name=name
        self.addr=addr
        self.student=[]
        self.teacher=[]
    def enroll(self,stu_obj):
        print("为[%s]学生办理注册手续"%stu_obj.name)
        self.student.append(stu_obj)
    def heir(self,ter_obj):
        print("为[%s]老师办理入职手续"%ter_obj.name)
        self.teacher.append(ter_obj)

class SchoolMember(object):
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def tell(self):
        pass


class Teacher(SchoolMember):
    def __init__(self,name,age,sex,salary,course):
        super(Teacher, self).__init__(name,age,sex)
        self.salary=salary
        self.course=course
    def tell(self):
        print('''
        --------info of Teacher %s-----
        Name:%s
        Age:%s
        Sex:%s
        Salary:%s
        Course:%s
        '''%(self.name,self.name,self.age,self.sex,self.salary,self.course))
    def teach(self):
        print("%s is teaching %s"%(self.name,self.course))


class Student(SchoolMember):
    def __init__(self,name,age,sex,stu_id,grade):
        super(Student, self).__init__(name,age,sex)
        self.stu_id=stu_id
        self.grade=grade
    def tell(self):
        print('''
        --------info of Student %s-----
        Name:%s
        Age:%s
        Sex:%s
        Stu_id:%s
        Grade:%s
        '''%(self.name,self.name,self.age,self.sex,self.stu_id,self.grade))
    def pay_tuition(self,amount):
        print("%s has paied tuition $%s"%(self.name,amount))

school=School("老男孩IT","沙河")

t1=Teacher("Oldman",45,"mf",2000000,"Linux")
t2=Teacher("Alex",32,"m",2000,"Python")

s1=Student("chenronghua",21,"m",1001,"PythonDev")
s2=Student("徐良伟",16,"m",1002,"PythonBianxie")


t1.tell()
s1.tell()
school.enroll(s1)
school.enroll(s2)
school.heir(t1)
school.teacher[0].teach()
for stu in school.student:
    stu.pay_tuition(5000)