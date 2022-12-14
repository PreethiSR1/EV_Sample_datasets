import pandas as pd
import random
from faker import Faker
from faker_vehicle import VehicleProvider
from random import randrange
from datetime import datetime, timedelta
import numpy as np
import uuid
import csv
from random import choices

no_of_evs = 100
fake = Faker('de_DE')
fake.add_provider(VehicleProvider)
evs = []
min_year = 2000
max_year = datetime.now().year
#st_dt, ed_dt = datetime(2015,1,1,0,0,0,0),datetime(2021,12,31,23,59,59,99999)
#time_del = ed_dt - st_dt


rd = random.Random()
rd.seed(0)

for ev_id in range(no_of_evs):
    name = fake.name()
    email = fake.ascii_email()
    address = fake.address()
    city = fake.city()
    country = fake.current_country()
    license_no = fake.license_plate()
    ev_model = fake.vehicle_make_model()
    age = np.random.randint(18,90)
    ev_uid = uuid.UUID(int = rd.getrandbits(128))
    kwh = round(random.uniform(0,10),2)
    soc = round(random.uniform(0.2,0.9),2)

    def gen_parkingtime(min_year = 2015,max_year = datetime.now().year):
        st_time = datetime(min_year,1,1,00,00,00)
        dt_del = max_year - min_year + 1
        end_time = st_time + timedelta(days=365*dt_del)
        return st_time + (end_time - st_time) * random.random()
    
    parking_time = gen_parkingtime()

    
    
    def gen_departtime(min_year = 2015,max_year = datetime.now().year):
        st_time = parking_time
        dt_del = random.randrange(1,6)
        end_time = st_time + timedelta(hours=6*dt_del)
        return st_time + (end_time - st_time) * random.random()

    departure_time = gen_departtime()

    

    evs.append([ev_uid,name,age,email,address,city,country,license_no,ev_model,kwh,soc,parking_time,departure_time])

evs_df = pd.DataFrame(evs, columns=["UID" , "Name" , "Age" , "E-Mail" , "Address" , "City" , "Country" , "License_Num", "Vehicle_Model", "KWh", "SOC", "Parking_time", "Departure_time"])
evs_df.to_csv("ev_dataset_1.csv")