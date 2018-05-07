import sys
import pip

sargs = ''
try:
    sargs = sys.argv[1]
except:
    print("Error!\nTry " + sys.argv[0] + " <URL>. Without url it's not working !")
    sys.exit(2)
    
else:
    if sargs.startswith("http") == False:
        sargs = "http://" + sys.argv[1]
    def install(package):
        pip.main(['install', package])

    try:
        import requests
    except ImportError:
        print ('requests is not installed, installing it now!')
        install('requests')

    import requests
    response = requests.get(sargs)
    print ('RESPOND STRING [ '+ str(response.status_code) +' ]: \n----------------------------------\n')
    print (str(response.content) + '\n\n[END of RESPOND]')
    sys.exit(1)
