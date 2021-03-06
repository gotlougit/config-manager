#script to manage configuration files

import os, json

#set both variables before using code!
fname = '' 
default_data = {} 

#for example, this will setup a web_config.json file in current folder
#fname = os.getcwd() + os.sep.join(('','web_config.json'))

def saveData(data):

    with open(fname,'w') as f:
        json.dump(data, f, indent = 1)

def loadData():
    
    try: 
        with open(fname) as f:
            out = json.load(f)
    except FileNotFoundError:
        saveData(default_data)
        out = default_data
        print('config file not found! creating one with default values..')
    return out
