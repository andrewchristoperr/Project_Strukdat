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
    def __init__(self, namaPemesan):
        self.head = None
        self.next = None
        self.namaPemesan = namaPemesan
        self.ambil = False

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

    def countTotal(self):
        temp = self.head
        total = 0
        i = 0
        while temp:
            total = total + (temp.quantity*temp.harga)
            temp = temp.next

        return total
    
    def rate(self):
        print("Please rate your order!")
        temp = self.head
        while temp:
            
            print("Rate: ", temp.nama, " (1-5)")
            rating = input("-> ")
            temp.rating = rating
            temp = temp.next
        print("Thanks! :)")

    def confirmOrder(self):
        print(self.namaPemesan, "'s Order: ")
        self.printList()
        print("Total: Rp ", self.countTotal())

class Queue:
    def __init__(self):
        self.front = self.rear = None
        self.size = 0
    
    def addToQueue(self, order):
        if self.front is None:
            self.front = self.rear = order
            self.size = self.size + 1
            return self.size
        
        self.rear.next = order
        self.rear = order
        self.size = self.size + 1
        return self.size
    
    def ambilOrderan(self, nomor):
        if self.front is None:
            return

        if self.antrianSaatIni() == nomor:
            itr = self.front
            current = 1
            while itr.next:
                if itr is self.rear:
                    break
                if current == nomor:
                    itr.ambil = True
                current += 1
                itr = itr.next
            print("Thanks for buying! :)")
            customer()
        else:
            print("Belum bisa mengambil orderan")
            print("Antrian saat ini: ", self.antrianSaatIni())
    
    # hitung jumlah cust dlm 1 hari
    def countCustomer(self):
        return self.size

    # buat cek nama yg diinput di antrian ke brp
    def checkAntrian(self, nama):
        antrian = 1
        if self.front is None:
            return
        
        itr = self.front
        while itr.next:
            if itr is self.rear:
                break   
            
            if itr.namaPemesan == nama:
                break
            antrian += 1
            itr = itr.next

        return antrian
    
    # cek skrg lg antrian no brp
    def antrianSaatIni(self):
        itr = self.front
        current = 1
        while itr.next:
            if itr == self.rear:
                break
            if itr.ambil == False:
                break
            current += 1
            itr = itr.next
        
        return current

    # list nama yg order
    def orderList(self):
        if self.front is None:
            return

        itr = self.front
        while itr:
            if itr is self.rear:
                break
            print(itr.namaPemesan)
            itr = itr.next

        print(itr.namaPemesan)

def cekAntrian():
    while True:
        print("1. Cek Nomor Antrianmu")
        print("2. Cek Antrian Saat Ini")
        print("3. Ambil Orderan")
        print("4. Exit")
        choice2 = int(input("Choice: "))
        if choice2 == 1:
            nama = input("Nama: ")
            print("No. Antrian: ", q.checkAntrian(nama))
        elif choice2 == 2:
            print("Antrian saat ini: ", q.antrianSaatIni())
        elif choice2 == 3:
            nomor = int(input("Masukkan nomor antrianmu: "))
            q.ambilOrderan(nomor)
        elif choice2 == 4:
            customer()
        else:
            print("Tidak ada dalam pilihan")

def customer():
    namaPemesan = input("Masukkan nama anda: ")
    print("Menu: ")
    menu.printList()
    print()
    choice = 0
    order = Order(namaPemesan)
    while(choice != 7):
        print("Keranjang: ")
        order.printList()
        print()
        print("1. Tambah Order")
        print("2. Delete Order")
        print("3. Confirm Order")
        print("4. Edit Order")
        print("5. Tambah Notes")
        print("6. Cek Antrian")
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
        elif choice == 3:
            if order.isEmpty() is True:
                print("Keranjang masih kosong")
                print()
            else:
                order.confirmOrder()
                print("No Antrian: ", q.addToQueue(order))
                order.rate()
                cekAntrian()
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
        elif choice == 6:
            cekAntrian()
menu = Menu()
menu.add("KENTANG", 20000)
menu.add("NASI GORENG", 25000)
menu.add("AIR PUTIH", 3000)
password = 'admin123'
choice = input("Admin: (Ya/Tidak)\n")
choice.lower()
q = Queue()
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
            print("PASSWORD SALAH!")
            print()
else:
    customer()