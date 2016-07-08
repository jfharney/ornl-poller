from celery import Celery


base_dir = '/Users/8xo/software/ornl-poller/ornl-poller'

app = Celery('tasks', backend='amqp', broker='amqp://guest@localhost//')


@app.task
def basicRequestHandlerWrapper(json_request,name):
    
    #add the base directory to the path so that the request handlers can be accessed
    import sys
    sys.path.append(base_dir)
    
    from handlers import requesthandlers
    #name = "BasicRequest"
    handler = requesthandlers.BasicRequestHandler(name)
    handler.launch(json_request)
    
    import time
    time.sleep(5)
    
    print 'after sleeping...'
    
    return name
    