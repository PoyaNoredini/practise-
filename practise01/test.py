from practise01.db import Database

sender_card_id = input("please enter your card id: ")
sender_data = Database.get_first("SELECT * FROM `persons` WHERE `card_id` = ?", (sender_card_id, ))

if not sender_data:
    name = input("please enter your name: ")
    Database.do("INSERT INTO `persons` (card_id, name) VALUES (?, ?)", (sender_card_id, name))
    sender_data = Database.get_first("SELECT * FROM `persons` WHERE `card_id` = ?", (sender_card_id, ))

receiver_card_id = input("please enter receiver card id: ")
receiver_data = Database.get_first("SELECT * FROM `persons` WHERE `card_id` = ?", (receiver_card_id, ))

if not receiver_data:
    name = input("please enter receiver name: ")
    Database.do("INSERT INTO `persons` (card_id, name) VALUES (?, ?)", (receiver_card_id, name))
    receiver_data = Database.get_first("SELECT * FROM `persons` WHERE `card_id` = ?", (receiver_card_id, ))

receiver_country = input("please enter receiver country: ")
receiver_postal_code = input("please enter receiver postal_code: ")
receiver_address = input("please enter receiver address: ")

Database.do("""INSERT INTO `parcels` (sender_id, receiver_id, country, postal_code, address)
             VALUES (?, ?, ?, ?, ?)""",
            (sender_data[0], receiver_data[0], receiver_country, receiver_postal_code, receiver_address)
        )
parcel_data = Database.get_first("SELECT * FROM `parcels` ORDER BY `id` DESC LIMIT 1")
print(parcel_data)