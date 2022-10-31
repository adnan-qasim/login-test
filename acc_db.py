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
    def same_acc(uname):
        client = pymongo.MongoClient('mongodb://localhost:27017/')
        db = client['Accounts-DB']
        collection = db.account
        acc=collection.find_one({"Username":uname})
        if acc==None:
            return False
        if acc!=None:
            return True
    def same_mail(mail):
        client = pymongo.MongoClient('mongodb://localhost:27017/')
        db = client['Accounts-DB']
        collection = db.account
        acc=collection.find_one({"Email Address":mail})
        if acc==None:
            return False
        if acc!=None:
            return True

    def all_acc():
        client = pymongo.MongoClient('mongodb://localhost:27017/')
        db = client['Accounts-DB']
        collection = db.accounts
        for accs in collection.find():
            for acc in accs:
                print(f'{acc}: {accs[acc]}')
            print('\n')
    def up_acc(user,field,data):
        client = pymongo.MongoClient('mongodb://localhost:27017/')
        db = client['Accounts-DB']
        collection = db.accounts
        result=collection.update_one({"Username": user},{'$set' : {field: data}})
        return result
        