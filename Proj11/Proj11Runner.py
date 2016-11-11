import dbm.dumb

def run (tupleKeys, tupleValues, dbName):
    print("Elena Stefanova")

    db = dbm.open(dbName, 'b')

    #populate the database
    for i in range(len(tupleKeys)):
        db[tupleKeys[i]] = tupleValues[i]
    
    

    db.close()
