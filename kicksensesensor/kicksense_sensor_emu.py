import http.client as httplib, sys, time, math, json, random

baseUri = 'https://stormy-woodland-9591.herokuapp.com/moveevent'
# id="kicker1"

headers = {}
headers['Content-Type'] = 'application/json'
headers['User-Agent'] = 'Kicker Rasperry Pi-Emulator'
headers['Accept'] = '*/*'

def createConnection():
    conn = httplib.HTTPConnection('stormy-woodland-9591.herokuapp.com')
    conn.connect()
    conn.debuglevel = 1
    return conn

def getValues():
    x = random.random()
    y = random.random()
    z = random.random()
    return [round(x, 2),round(y, 2),round(z, 2)]

conn = createConnection()

# here is where the shit gets real
while True:
    x, y, z = getValues()
    time.sleep(1)
    print ("I feel good vibrations!!!")
    body={"x":x,"y":y,"z":z}
    try:
        print ("Try to send POST as json: ", json.dumps(body))
        request = conn.request('POST', baseUri+'/', json.dumps(body), headers)
        print ("posted, response is: : ")
        reply = conn.getresponse()
        print (reply.read())
    except:
        e = sys.exc_info()[0]
        print('Oh, something went wrong: {}', e)
        conn = createConnection()
