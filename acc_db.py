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
        accId= collection.insert_one(AccInfo).inserted_id
        return accId