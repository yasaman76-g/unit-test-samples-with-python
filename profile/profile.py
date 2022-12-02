class Profile:
    def __init__(self,name,age,job):
        self.name = name
        self.age = age
        self.job = job
        
    def getName(self):
        print(self.name)
    
    def getAge(self):
        print(self.age)
        
    def getJob(self):
        print(self.job)