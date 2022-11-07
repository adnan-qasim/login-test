import pymongo
client = pymongo.MongoClient('mongodb+srv://AdnanQasim:11%40Ug2000@testingmongodb.u8xgxpo.mongodb.net/test')

class acc_crud:
    def add_acc(name,user,mail,passw):
        db = client['Accounts-DB']
        collection = db.newAccDB
        AccInfo={
            "Full Name": name,
            "Username": user,
            "Email Address": mail,
            "Password": passw
        }
        accId=collection.insert_one(AccInfo).inserted_id
        return accId

    def acc_pass(uname):
        db = client['Accounts-DB']
        collection = db.newAccDB
        acc=collection.find_one({"Username":uname})
        if acc!=None:
            return acc["Password"]
        else:
            return None
    def same_acc(uname):
        db = client['Accounts-DB']
        collection = db.account
        acc=collection.find_one({"Username":uname})
        if acc==None:
            return False
        if acc!=None:
            return True
    def same_mail(mail):
        db = client['Accounts-DB']
        collection = db.account
        acc=collection.find_one({"Email Address":mail})
        if acc==None:
            return False
        if acc!=None:
            return True

    def all_acc():
        db = client['Accounts-DB']
        collection = db.newAccDB
        for accs in collection.find():
            for acc in accs:
                print(f'{acc}: {accs[acc]}')
            print('\n')
    def up_acc(user,field,data):
        db = client['Accounts-DB']
        collection = db.newAccDB
        result=collection.update_one({"Username": user},{'$set' : {field: data}})
        return result
        
    def del_acc(user):
        db = client['Accounts-DB']
        collection = db.newAccDB
        result=collection.delete_one({"Username": user})
        return result