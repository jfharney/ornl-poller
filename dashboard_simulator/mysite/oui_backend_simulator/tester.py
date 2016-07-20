import requests

url = 'http://localhost:9000/oui_backend_simulator/update/'

def main():
    print 'in main'
    
    #test_get_in_progress()
    
    #post_status('complete',1)
    #config_options: '{"compiler": "intel", "runspec": "/User Documents/acmetest/asdf/testfile.txt", "mppwidth": 144, "mach": "titan", "casename": "F1850C5.ne30.6mos", "res": "ne30_g16", "destination": "", "project": "cli115", 
    #"stop_option": "ndays", "compset": "F1850C5", "walltime": "60, 60", "stop_n": "60, 60"}'

    
    #payload = {'request': 'new', 'user': 'test', 'testdata': 'hello2', 'model': 'CMIP5'}
    
    #MUST INCLUDE USER for a post!!!!!!!!!!!
    
    payload = {
               'user' : 'test',
               'request' : 'new',
               "compiler": "intel",
               "runspec": "/User Documents/acmetest/asdf/testfile.txt",
               "mppwidth": 144,
               "mach": "titan",
               "casename": "F1850C5.ne30.6mos",
               "res": "ne30_g16",
               "destination": "", 
               "project": "cli115",
               "stop_option": "ndays", 
               "compset": "F1850C5",
               "walltime": "60, 60", 
               "stop_n": "60, 60"
               }
    
    
    
    
    test_post_new(payload)
    
    get_status('failed')
    
    #post_status('in_progress',15)
    #get_status('new')
    #get_status('in_progress')
    #get_status('failed')
    #get_status('complete')
    
    #test_get_in_progress()
    
    #
    
    
    #test_get_next()
    
    #job_id = 1
    
    
    #test_post_in_progress(job_id)
    
    #test_get_next()
    

def get_status(status):
    payload = {'request' : status}
    r = requests.get(url, params=payload)
    print 'status: ' + str(status) + '\n' + str(r.text) + '\n' + '\n' + str(r.json())
    
    
    #for key in r.json():
    #    print 'key: ' + str(key)
        
    #print str(r.json().has_key('job_id'))
    '''
    if r.text == None:
        print 'Nonde'
    elif r.text == '':
        print 'none'
    elif r.text == {}:
        print 'n'
    '''

def post_status(status,job_id):
    
    payload = {'request' : status, 'job_id' : job_id}
    r = requests.post(url, data=payload)



def test_get_in_progress():
    
    payload = {'request' : 'in_progress'}
    r = requests.get(url, params=payload)
    print 'in_progress: ' + str(r.text)
    

def test_get_next():
    payload = {'request': 'next'}
    #r = requests.get(self.live_server_url + '/poller/update/', params=payload)
    r = requests.get(url, params=payload)
    
    print 'next: ' + str(r.text)
    #self.assertTrue(r.status_code == requests.codes.ok)



def test_post_in_progress(job_id):
        payload = {'request': 'in_progress', 'job_id': job_id}
        r = requests.post(url, data=payload)
        
        
        '''
        self.assertTrue(r.status_code == requests.codes.ok)
        payload = {'request': 'job', 'job_id': 1}
        r = requests.get(self.live_server_url + '/poller/update/', params=payload)
        self.assertTrue(r.status_code == requests.codes.ok)
        data = json.loads(r.content)
        self.assertEquals(data['status'], 'in_progress')
        '''

def test_post_all_with_user():
        payload = {'request': 'all', 'user': 'acmetest', 'status': 'complete'}
        r = requests.post(self.live_server_url + '/poller/update/', data=payload)
        self.assertTrue(r.status_code == requests.codes.ok)
        payload = {'request': 'all', 'user': 'acmetest'}
        r = requests.get(self.live_server_url + '/poller/update/', params=payload)
        for job in r.json():
            self.assertEquals(job['status'], 'complete')
        payload = {'request': 'all', 'user': 'acme'}
        r = requests.get(self.live_server_url + '/poller/update/', params=payload)
        for job in r.json():
            self.assertNotEquals(job['status'], 'complete')


def test_post_new(payload):
        r = requests.post(url, data=payload)
        
        
        print 'r.json(): ' + str(r.text)
        
        
        
        #self.assertTrue(r.status_code == requests.codes.ok)
        #for job in r.json():
        #    self.assertEquals(job['status'], 'new')
        
        
        '''
        self.assertTrue(r.status_code == requests.codes.ok)
        payload = {'request': 'all', 'user': 'test'}
        r = requests.get(self.live_server_url + '/poller/update/', params=payload)
        self.assertTrue(r.status_code == requests.codes.ok)
        for job in r.json():
            self.assertEquals(job['status'], 'new')
        '''
    
if __name__ == "__main__": main()



