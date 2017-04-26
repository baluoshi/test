

class Peole(object):
    info ='test'
  #  info_dic={"name":"xiekean","lover":"haiqing"}
    def __init__(self,name,age,job):
        self.name1=name
        self.age2=age
        self.job6=job
        self.info='t2'
        self.info_dic={"name":"xiekean","lover":"haiqing"}
        print '__runing init  '
    def __breath(self):
        print"%s is breathing",self.name1
    def walk(self):
        print "i am walking....",self.__breath()

    def talk(self):
         print"talking with sb....",self.age2,Peole.info

p1 =Peole("Wangshanjin",29,"BaoAn")

p2 =Peole("aaa",69,"rtr")
p1.info="fuck"
p1.info_dic["name"]="shit"

print"P1=:" ,p1.info,p1.info_dic
print p2.info, Peole.info
print "ditc",p2.walk()
