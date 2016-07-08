from WFBlackBoxSimulator import WFBlackBoxSimulator

def main():
    print 'in main'
    
    path = '/some_path/'
    
    # create a poller object
    
    
    # create a requesthandler object
    
    
    # create a simulator object for the WF Black Box
    simulator = WFBlackBoxSimulator()
    
    id = simulator.startWf(path)
    
    print 'id: ' + str(id)
    
    response = 0
    
    while(response == 0):
      response = simulator.query(id)
      print str(simulator.running_workflows)
      print 'response: ' + str(response)
    
    print str(simulator.running_workflows)
    
    # create an object for service 1 - json2Wf listening
    # create an object for service 2 listening
    # create an object for service 3 listening
    # create an object for service 4 listening
    
    '''
    Wf.json2Wf(data,path)
    
    Wf.startWf(path)
    
    Wf.stopWf(id)
        
    Wf.query(id)
    '''
    
    
    
    
    
    
    #id = simulator.startWf(path)

if __name__ == "__main__": main()
