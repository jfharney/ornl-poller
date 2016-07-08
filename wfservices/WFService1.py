    
'''
WFService1 launches Workflow with a one to one mapping to startWorkflow
'''
import sys

sys.path.append('/Users/8xo/software/ornl-poller/ornl-poller/')


from simulator import AbstractWF


def wfservice1(pathToWF):
    
    response = 'response'
    wf = AbstractWF()
    wf.startWorkflow(pathToWF)
    
    return response


def main():
    print 'in WFService1 main'



if __name__ == "__main__": main()