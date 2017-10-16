import paho.mqtt.client as mqtt
import protocol


username = ""
bip=""
reciepent = ""
dataA=str('a')
dataB=str('b')


def on_connect(client,userdata,flags,rc):
    print "\n(connected)"
    client.subscribe("shekharApp/chat/"+username,1)
    client.subscribe("shekharApp/chat/all")
    client.publish("shekharApp/chat/all",username+" connected\n",1)


def on_message(client,userdata,msg):
    newmsg=str(msg.payload)
    val=protocol.decode(username,newmsg)
    val=str(val)
    newList=val.split(":")
    if len(newList)>2:
        if newList[0]==username:
            client.publish("chat/"+reciepent,val, 1)
        else:
            print "\n\n\n"+newList[0]+">>>"+" "+newList[1]
            print "at "+newList[3]+"\n\n\n"

def on_disconnect(client,usredata,rc):
    print "\n(Disconnectd from broker)"

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect


client.connect("iot.eclipse.org",1883,120)

client.loop_start()

while True:

    username=raw_input("Enter your name  ")
    print "\nIs it your name ? >> " +username
    i=raw_input("YES[Y]  NO[N]  ")
    i=i.upper()
    if i=="Y":
        break
    elif i=="N":
        continue

print "\nenter 'user'<space>'username' only to change reciepent"
while True:
    msg=raw_input("\n\nEnter your messege  >>>")

    msglist=msg.split(" ")
    if len(msglist)>0:
        if msglist[0]=="user":
            reciepent = msglist[1]
            protocol.setRec(msglist[1])
            continue

        if reciepent == "":
            reciepent = raw_input("\nPlease enter reciepent >> ")
            protocol.setRec(reciepent)

        elif msg=="exit":
            exit()
    tele=protocol.encode(username,msg)
    client.publish("shekharApp/chat/"+reciepent,tele,1)






