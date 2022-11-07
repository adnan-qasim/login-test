from faker import Faker
from acc_db import acc_crud
import random

addFake=Faker()

for i in range(69):
    fake_un=str(addFake.first_name()+str(random.randint(10,9999))).lower()
    id=acc_crud.add_acc(addFake.name(),fake_un,addFake.email(),addFake.password())
    
