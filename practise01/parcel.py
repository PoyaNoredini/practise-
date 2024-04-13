from practise01.db import Database

parcel_id = int(input("please enter the parcel id: "))
parcel_data = Database.get_first("SELECT * FROM `parcels` WHERE `id` = ? LIMIT 1", (parcel_id, ))
print(parcel_data)