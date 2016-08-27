__author__ = 'Raghava'

class Students:
    def __init__(self,name,sem,result,marks):
        self.name=name
        self.sem=sem
        self.result=result
        self.marks=marks
        #self.total=total
    def __str__(self):
        return self.name+"_"+str(self.marks)+"_"+str(self.sem)+"_"+str(self.result)+"_" #+str(self.total)