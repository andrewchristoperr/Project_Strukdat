class Node:
    def __init__(self, nama, harga:int):
        self.next = None
        self.nama = nama
        self.harga = harga
        self.quantity = None
        self.rating = None

class Menu:
    def __init__(self):
        self.head = None

    def add(self, nama, harga:int):
        #jika masih kosong
        if self.head == None:
            newNode = Node(nama, harga)
            self.head = newNode
        else:
            newNode = Node(nama, harga)
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = newNode

    def printList(self):
        temp = self.head
        i = 0
        while temp:
            i+=1
            print(i ,temp.nama, temp.harga)
            temp = temp.next

class Order:
    def __init__(self):
        self.head = None

    def add(self, nama, harga):
        temp = self.head
        while temp:
            if nama == temp.nama:
                self.quantity =+ 1
            temp = temp.next
        if self.head == None:
            newNode = Node(nama, harga)
            self.head = newNode
        else:
            newNode = Node(nama, harga)
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = newNode

    def printList(self):
        temp = self.head
        i = 0
        while temp:
            i+=1
            print(i ,temp.nama)
            temp = temp.next
menu = Menu()
menu.add("Kentang", 20000)
menu.add("Nasi goreng", 25000)
menu.add("Air Putih", 3000)
print("Menu: ")
menu.printList()
print()
choice = 0
order = Order()
while(choice != 3):
    print("1. Tambah Order")
    print("2. Delete Order")
    print("3. Confirm Order")
    print("Your Order:")
    choice = input("Choice: ")
    if choice == 1:
        nomer = input("Masukkan nomer order pada menu: ")
        if nomer == 1:
            order.add("Kentang")
        


