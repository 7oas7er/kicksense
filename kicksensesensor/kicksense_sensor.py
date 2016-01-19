# from sense_hat import SenseHat
import http.client as httplib, sys, time, math, json

baseUri = 'https://stormy-woodland-9591.herokuapp.com/moveevent'
id="kicker1"

sense = SenseHat()


headers = {}
headers['Content-Type'] = 'application/json'
headers['User-Agent'] = 'Kicker Rasperry Pi'
headers['Accept'] = '*/*'

def createConnection():
    conn = httplib.HTTPConnection('stormy-woodland-9591.herokuapp.com')
    conn.connect()
    conn.debuglevel = 1
    return conn

def getValues():
    x, y, z = sense.get_accelerometer_raw().values()
    return [round(x, 2),round(y, 2),round(z, 2)]

def changed(x,y,z):
    x1, y1, z1 = getValues()
    rumbleOffset = 0.02

    print ("Current Delta X> ", math.fabs(x-x1))
    print ("Current Delta Y> ", math.fabs(y-y1))
    print ("Current Delta Z> ", math.fabs(z-z1))

    return math.fabs(x-x1)>rumbleOffset or math.fabs(y-y1)>rumbleOffset or math.fabs(z-z1)>rumbleOffset


conn = createConnection()
while True:
    x, y, z = getValues()

    print(x,y,z)
    time.sleep(1)
    if changed(x,y,z):
        print ("Changed!!")
        body={"x":x,"y":y,"z":z}
        try:
            print ("Try to send POST", body)
            print ("Try to send POST as json> ", json.dumps(body))

            # request = conn.request('POST', baseUri+'/'+id+'/', str(body).encode('ascii'), headers)
            # request = conn.request('POST', baseUri+'/', str(body).encode('ascii'), headers)
            request = conn.request('POST', baseUri+'/', json.dumps(body), headers)
            print ("POST is raus, Antwort lautet")
            reply = conn.getresponse()
            print (reply.read())
            # sense.show_message("!", text_colour=[255, 0, 0])
            sense.load_image("circle.png")
            # sense.set_pixels()

        except:
            e = sys.exc_info()[0]
            print('Oh, Request could not be sent: {}', e)
            conn = createConnection()


