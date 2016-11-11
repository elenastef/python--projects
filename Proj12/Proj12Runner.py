import dbm.dumb

def run(dbName):
    myKeys = b'name',b'age',b'gender'
    myValues = b'Joe',b'39',b'male'

    print("Elena Stefanova")

    db = dbm.open(dbName, 'c')

    #populate the database
    for i in range(len(myKeys)):
        db[myKeys[i]] = myValues[i]
