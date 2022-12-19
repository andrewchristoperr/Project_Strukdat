class Node:
    def __init__(self, nama, harga:int):
        self.next = None
        self.nama = nama
        self.harga = harga
        self.quantity = 0
        self.rating = None
        self.notes = None

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

    def hapus(self, key):
        temp = self.head

        if self.head is not None:
            if temp.nama == key:
                self.head = temp.next
                temp = None
                return

        while temp is not None:
            if temp.nama == key:
                break
            prev = temp
            temp = temp.next
        
        if temp == None:
            return

        prev.next = temp.next
        temp = None

    def printList(self):
        temp = self.head
        i = 0
        while temp:
            i+=1
            print(i ,'.', temp.nama, temp.harga)
            temp = temp.next

class Order:
    def __init__(self):
        self.head = None
        self.next = None

    def add(self, nama, harga):
        temp = self.head
        bool = False
        while temp:
            if nama == temp.nama:
                temp.quantity += 1
                
                bool = True
                break
            temp = temp.next
        if bool == False:
            if self.head == None:
                newNode = Node(nama, harga)
                self.head = newNode
                newNode.quantity += 1
            else:
                newNode = Node(nama, harga)
                temp = self.head
                while temp.next:
                    temp = temp.next
                temp.next = newNode
                newNode.quantity += 1

    def hapus(self, key):
        temp = self.head

        if self.head is not None:
            if temp.nama == key:
                self.head = temp.next
                temp = None
                return

        while temp is not None:
            if temp.nama == key:
                break
            prev = temp
            temp = temp.next
        
        if temp == None:
            return

        prev.next = temp.next
        temp = None
    
    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False

    def printList(self):
        temp = self.head
        i = 0
        while temp:
            if temp.notes == None:
                print(temp.quantity, temp.nama, temp.quantity * temp.harga)
            else:
                print(temp.quantity, temp.nama, temp.quantity * temp.harga, '            Notes', temp.notes)
            temp = temp.next

    def tambahOrder(self, temp, nomer):
        i = 0
        while temp:
            i += 1
            if i == nomer:
                self.add(temp.nama, temp.harga)
            temp = temp.next

    def hapusOrder(self, nama):
        bool = False
        temp = self.head
        while temp:
            if temp.nama == nama:
                self.hapus(nama)
                bool = True
            temp = temp.next
        if bool == False:
            print("Makanan tidak terdaftar")

    def editOrder(self, nama):
        quantity = int(input("Masukkan quantity: "))
        bool = False
        temp = self.head
        while temp:
            if temp.nama == nama:
                temp.quantity = quantity
                bool = True
            temp = temp.next
        if bool == False:
            print("Makanan tidak terdaftar")

    def addNotes(self, nama):
        notes = input("Notes: ")
        bool = False
        temp = self.head
        while temp:
            if temp.nama == nama:
                temp.notes = notes
                bool = True
            temp = temp.next
        if bool == False:
            print("Makanan tidak terdaftar")

def customer():
    print("Menu: ")
    menu.printList()
    print()
    choice = 0
    order = Order()
    while(choice != 6):
        print("Keranjang: ")
        order.printList()
        print()
        print("1. Tambah Order")
        print("2. Delete Order")
        print("3. Confirm Order")
        print("4. Edit Order")
        print("5. Tambah Notes")
        print("6. Exit")
        choice = int(input("Choice: "))
        print()
        if choice == 1:
            nomer = int(input("Masukkan nomer order pada menu: "))
            temp = menu.head
            order.tambahOrder(temp, nomer)
                    
        elif choice == 2:
            if order.isEmpty() is True:
                print("Keranjang masih kosong")
                print()
            else:
                nama = input("Masukkan nama makanan yang ingin dicancel: ").upper()
                order.hapusOrder(nama)
        elif choice == 4:
            if order.isEmpty() is True:
                print("Keranjang masih kosong")
                print()
            else:
                nama = input("Masukkan nama makanan yang ingin diedit quantitynya: ").upper()
                order.editOrder(nama)
        elif choice == 5:
            if order.isEmpty() is True:
                print("Keranjang masih kosong")
                print()
            else:
                nama = input("Masukkan nama makanan yang ingin diberi notes: ").upper()
                order.addNotes(nama)  
        else:
            print("PASSWORD SALAH!")
            print()
menu = Menu()
menu.add("KENTANG", 20000)
menu.add("NASI GORENG", 25000)
menu.add("AIR PUTIH", 3000)
password = 'admin123'
choice = input("Admin: (Ya/Tidak)\n")
choice.lower()
inputPass = ''
if choice == 'ya':
    while inputPass != password:
        inputPass = input("Password: \n")
        if inputPass == password:
            pilihan = 0
            print("------ADMIN------")
            while(pilihan != 4):
                print("Menu: ")
                menu.printList()
                print()
                print("1. Tambah Menu")
                print("2. Delete Menu")
                print("3. Edit Menu")
                print("4. Exit")
                pilihan = int(input("Choice: "))
                print()
                if pilihan == 1:
                    namaMenu = input("Masukkan nama menu: ").upper()
                    harga = int(input("Masukkan harga menu: "))
                    menu.add(namaMenu, harga)
                elif pilihan == 2:
                    nama = input("Masukkan nama menu yang mau didelete: ").upper()
                    menu.hapus(nama)
                elif pilihan == 3:
                    nama =  input("Masukkan nama menu yang mau diedit: ").upper()
                    nama2 = input("Masukkan nama menu baru: ").upper()
                    harga = int(input("Masukkan harga: "))
                    temp = menu.head
                    while temp:
                        if temp.nama == nama:  
                            temp.nama = nama2
                            temp.harga = harga
                        temp = temp.next
                elif pilihan == 4:
                    customer()
else:
    customer()