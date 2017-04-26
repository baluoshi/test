

class SchoolMember (object):
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def tell(self):
        print'''---info of %s--
        name:%s
        age:%s
        sex:%s

       ''' %(self.name,self.name,self.age,self.sex)
class Student(SchoolMember):

    def __init__(self,name,age,sex,grade):

         SchoolMember.__init__(self,name,age,sex)
         self.grade=grade
    def pay_money(self):
        print "---%s paying the tuition fee--" %self.name
    def tell(self):
        SchoolMember.tell(self)
        print"--free %s" %self.grade
class Teacher(SchoolMember):
    def __init__(self,name,age,sex,course,salary):
        SchoolMember.__init__(self,name,age,sex)
        self.course=course
        self.salary=salary
    def teaching(self):
        print "Teacher %s is teaching class of %s"%(self.name,self.course)

s= Student("wangsanjin",33,'m',"PY S10")
s2=Student("lisong",22,'f',"PY S12")
t= Teacher("jack",19,"Me","python",62000)
s.tell()
s2.tell()
s.pay_money()
t.teaching()






