#!/usr/bin/env python

# Implements the Pegasus instance interface for poller to call

import poller
import json
import os
import subprocess
import json

class Pegasus(poller.Poller):

  def which(self, program):
    def is_exe(fpath):
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

    fpath, fname = os.path.split(program)
    if fpath:
        if is_exe(program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            path = path.strip('"')
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                return exe_file

    return None

  def jsonToWorkflow(self, jsonstring, pathToWF):
    '''
    print("jsonToWF")
    items = ['casename', 'res', 'compiler', 'stop_n', 'project', 'mppwidth', 'user', 'stop_option', 'compset', 'mach', 'walltime']

    values = json.loads(jsonstring)

    # Write configuration file
    filename = os.path.join(pathToWF, values['casename']+".cfg")
    print 'Creating configuration file: '+ filename
    f = open(filename, 'w')
    f.write('[acme]\n')

    for i in items:
      f.write(str(i)+" = "+str(values[i])+"\n")

    f.close()

    return [filename, values['casename']] 
    '''
    return 'response for jsonToWorkflow'

  def startWorkflow(self, jsonstring, pathToWF):
    pegasusConfig = '/ccs/home/bmayer/ACME-Workflow/'
    pegasusACMEPath = ''
    pegasusRunCommand = ''
    
    '''
    # Check if pegasus is available
    if self.which('pegasus-run') is None:
        print("Can't find Pegasus")
        return 1

    # Check if Python is available
    if self.which('python') is None:
        print("Can't find python")
        return 1

    # Generate the DAX config from JSON
    names = self.jsonToWorkflow(jsonstring, pathToWF)

    # Generate the DAX
    # python daxgen.py test.cfg mysetup.sh DIRNAME
    daxgen = 'daxgen.py'
    setup = 'mysetup.sh'
    wfdirectory = os.path.join(pathToWF, names[1])
    cmdlist = ['python', os.path.join(pegasusConfig, daxgen), os.path.join(pegasusConfig, names[0]), os.path.join(pegasusConfig, setup), wfdirectory]

    try:
        subprocess.check_call(cmdlist)
    except subprocess.CalledProcessError as e:
        print(e)
        return 1
    except Exception, e:
        print(e)
        return 1

    # ./plan.sh DIRNAME
    ret = ""
    cmdlist = [os.path.join(pegasusConfig,'plan.sh'), wfdirectory]
    try:
        ret = subprocess.check_output(cmdlist)
    except subprocess.CalledProcessError as e:
        print(e)
        return 1
    except Exception, e:
        print(e)
        return 1

    for line in iter(ret.splitlines()):
        if line.find('pegasus-run ') >= 0:
            pegasusACMEPath = line.split()[1]
            pegasusRunCommand = line.split()
            
    # pegasus-run $DIR
    cmdlist = pegasusRunCommand 
    print(cmdlist)
    try:
        subprocess.check_call(cmdlist)
    except subprocess.CalledProcessError as e:
        print(e)
        return 1
    except Exception, e:
        print(cmdlist)
        print(e)
        return 1

    # build return JSON
    jsonString = json.dumps({'pegasusID':pegasusACMEPath})    
    return jsonString
    '''
    return 'jsonString'

  def stopWorkflow(self, ID):
      
    '''
    # Check if pegasus is available
    if self.which('pegasus-run') is None:
        print("Can't find Pegasus")
        return 1

        # Check if Python is available
    if self.which('python') is None:
        print("Can't find python")
        return 1    

    # pegasus-remove $rundirectory
    cmdlist = ['pegasus-remove', ID]
    try:
        subprocess.check_call(cmdlist)
    except subprocess.CalledProcessError as e:
        print(e)
        return 1
    except Exception, e:
        print(e)
        return 1

        return
    '''
    return 'response for stopworkflow'

  def queryWorkflow(self, ID):

    '''
    # Check if pegasus is available
    if self.which('pegasus-run') is None:
        print("Can't find Pegasus")
        return 1

        # Check if Python is available
    if self.which('python') is None:
        print("Can't find python")
        return 1

    # pegasus-status -l $RUNDIR
    cmdlist = ['pegasus-status', '-l', ID]
    try:
        subprocess.check_call(cmdlist)
    except subprocess.CalledProcessError as e:
        print(e)
        return 1
    except Exception, e:
        print(cmdlist)
        print(e)
        return 1
        return 
    '''
    return 'response for queryworkflow'

  def queryPerformance(self, ID):
    # Check if pegasus is available

    # ???
    return