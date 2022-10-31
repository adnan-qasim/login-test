import pymongo

class acc_crud:
    def add_acc(name,user,mail,passw):
        client = pymongo.MongoClient('mongodb://localhost:27017/')
        db = client['Accounts-DB']
        collection = db.accounts
        AccInfo={
            "Full Name": name,
            "Username": user,
            "Email Address": mail,
            "Password": passw
        }
        accId=collection.insert_one(AccInfo).inserted_id
        return accId

    def acc_pass(uname):
        client = pymongo.MongoClient('mongodb://localhost:27017/')
        db = client['Accounts-DB']
        collection = db.accounts
        acc=collection.find_one({"Username":uname})
        if acc!=None:
            return acc["Password"]
        else:
            return None