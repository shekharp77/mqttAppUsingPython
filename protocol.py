from datetime import datetime
blockedList=[]
list1=[]
list2=[]
mList=[]
cmd=[]
rec=""
myusername=""

def setRec(msg):
    global rec
    rec = msg
    print "\nReciepent changed to >>  " + rec


def encode(username,msg):
    myusername=username
    a =(username,msg,rec,str(datetime.now()))
    fin=":".join(a)
    list2=msg.split(" ")
    if len(list2)>0:
        if list2[0]=="block":
            block(list2[1])
            return
        elif list2[0]=="unblock":
            unblock(list2[1])
            return
        elif list2[0]=="show":
            if list2[1]=="all" and list2[2]=="users":
                print "waiting for an automatic reply"
                return username+":"+"show"+":"+"all users"+":"+str(datetime.now())
            elif list2[1]=="blocked":
                print blockedList
            return fin
        else:
            return fin
    else:
        return fin
ard=""
nmsg=""
def decode(myusername, message):
    mList=message.split(":")
    if len(mList)>2:
        nmsg= str(mList[1])
        ard=nmsg.split(" ")
        recep=mList[0]
        if recep not in blockedList and mList[0] != myusername:
            if mList[1] =="show":
                if mList[2]=="all users":
                    return myusername+":"+" is alive "+":"+mList[0]+":"+str(datetime.now())
            elif mList[2]=="all" or mList[2]==myusername:
                return message

def block(msg):
    blockedList.append(msg)



def unblock(user):
    blockedList.remove(user)
