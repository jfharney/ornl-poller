
import random
from simulator import AbstractWF

from simulator import WorkflowInstance

print str(dir(WorkflowInstance))

def main():
    print 'in main'
    
    path = '/some_path/'
    
    simulator = WFBlackBoxSimulator()
    
    #wfi = WorkflowInstance.WorkflowInstance()
    
    #id1 = simulator.startWorkflow(path)
    #id2 = simulator.startWorkflow(path)
    
    

class WFBlackBoxSimulator(AbstractWF.AbstractWF):
    
    def __init__(self):
        print 'initializing'
        #self.running_workflows = []
    
    def jsonToWorkflow(self,json,pathToWF):
        return
    
    def startWorkflow(self,pathToWF):
        
        print 'in startWorkflow for path: ' + str(pathToWF)
        
        response = 'OK'
        submit_ok = random.randint(1,20)
        if submit_ok > 18:
            response = 'ERROR'
        
        
        return response
        
    
    def stopWorkflow(self,ID):
        
        submit_ok = random.randint(1,20)
        response = 1
        
        '''
        if submit_ok > 18:
            response = -1
        else:
            
            for workflow in self.running_workflows:
                if workflow == ID:
                    self.running_workflows.remove(workflow)
                
        '''
        
        return response
        
        
    def queryWorkflow(self,ID):
        
        response = 'IN_PROGRESS'
        
        submit_ok = random.randint(1,20)
        
        if submit_ok > 18:
            response = 'ERROR'
        elif submit_ok < 3:
            response = 'DONE'
            
        return response
    
    
    
    def queryPerformance(self,ID):
        return
    

       

if __name__ == "__main__": main()



'''
    def __init__(self):
        print 'initializing'
        self.running_workflows = []
    
    
    #helper function to remove an existing workflow
    def removeWF(self,id):
        for workflow in self.running_workflows:
            if workflow['id'] == id:
                self.running_workflows.remove(workflow)
    
    
    
    #obtain a workflow id
    def json2Wf(self,data,path):
        print 'in json2Wf for data: ' + str(data) + ' and path: ' + str(path)
        
        submit_ok = random.randint(1,20)
        response = 1
        if submit_ok > 18:
            response = -1
        
        return response
    
    
    
    
    def startWf(self,path):
        print 'if startWf for path: ' + str(path)
        
        id = 'id' + str(random.randint(1,3000))
        response = id
        
        submit_ok = random.randint(1,20)
        error_check = 1
        if submit_ok > 18:
            error_check = -1
        
        if error_check == -1:
            response = "Error"
        
        if response != "Error":
            #add workflow to the simulator here
            start = None
            duration = 1
            wfi = WorkflowInstance(id,"WF"+str(id),start,duration)
            self.running_workflows.append(id)
        
        
        return response
    
    
    
    def stopWf(self,id):
        print 'in stopWf for id: ' + str(id)
        
        submit_ok = random.randint(1,20)
        response = 1
        if submit_ok > 18:
            response = -1
        
        return response
    
    
    
        
    def query(self,id):
        print 'in query for id: ' + str(id)
        rand_response = random.randint(1,20)
        response = 0
        if rand_response > 17:
            print 'wf incomplete - error received'
            
            #self.running_workflows.remove(id)
            response = -1
        elif rand_response < 3:
            #self.running_workflows.remove(id)
            self.removeWF(id)
            print 'wf complete'
            response = 1
            
        return response

'''
''' old startWF
        id = 'id' + str(random.randint(1,3000))
        response = id
        
        
        submit_ok = random.randint(1,20)
        error_check = 1
        
        if submit_ok > 18:
            error_check = -1
        
        if error_check == -1:
            response = "Error"
        
        if response != "Error":
            #add workflow to the simulator here
            #add workflow to the simulator here
            start = None
            duration = 1
            wfi = WorkflowInstance.WorkflowInstance(id,"WF"+str(id),start,duration)
            self.running_workflows.append(id)
        
        print 'submit_ok: ' + str(submit_ok) + ' response: ' + str(response)
        print 'running workflows: ' + str(self.running_workflows)
'''