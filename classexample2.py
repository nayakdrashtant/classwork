class myMac():
     def __init__(self):
         self.mylist = [0x00,0x00,0x00,0x00,0x00,0x00]

thispc = myMac()
def printmac(somemac): 
    print(somemac.mylist)

printmac(thispc)
