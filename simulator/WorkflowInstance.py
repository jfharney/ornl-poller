class WorkflowInstance(object):
    
    def __init__(self,id,name="default",start=None,duration=1):
        print 'creating workflow instance id: ' + str(id)
        self.id = id
        self.name = name
        self.start = start
        self.duration = duration
        
    
    def printName(self):
        print self.name    
    
    

def main():
    
    id = 'id1'
    name = 'default'
    start = 1
    duration = 1
    instance = WorkflowInstance(id,name,start,duration)
    
    print instance.id
    
if __name__ == "__main__": main()