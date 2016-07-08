def main():
    
    print 'in main for post_client'

    post()
        

def post(message='default_message'):
    payload_post = {'json_message':message}
    
    r = requests.post('http://localhost:9000/oui_backend_simulator/about/4/',data=payload_post)
    print r.text   

if __name__ == "__main__": main()