import dbm.dumb

def run (tupleKeys, tupleValues, dbName):
    print("Elena Stefanova")

    db = dbm.open(dbName, 'c')

    #populate the database
    for i in range(len(tupleKeys)):
        db[tupleKeys[i]] = tupleValues[i]
    
    for i in db:
        print("key: ", i, "value: ", db[i])

    db.close()



myKeys = b'name',b'age',b'gender'
myValues = b'Joe',b'39',b'male'
databaseName = 'database'

run(myKeys,myValues,databaseName)


