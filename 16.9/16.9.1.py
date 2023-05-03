from classes import Rectangle, Client

rect1 = Rectangle(20,30,6,10)

print(rect1)
print(rect1.getArea())


client1 = Client('Dmitriy', 'Egorov', 'Cherepovetc', 48)
print(client1)

client2 = Client('Olga', 'Egorova', 'Cherepovetc', 51)
client3 = Client('Vladimir', 'Rukin', 'Vologda', 37)

clientList = [client1, client2, client3]

for client in clientList:
    print(client.getClientList())