import re
class contact:
    def __init__(self, name, number):
        self.name=name
        self.number=number

def insert_contact(contactlog, Name, Number):
    temp=contact(Name, Number)
    Name=Name.lower()
    if len(contactlog)==0:
        contactlog.append(temp)
    else:
        for i in range(len(contactlog)):
            if contactlog[i].name.lower() > Name:
                contactlog.insert(i,temp)
                break
            else:
                if i==len(contactlog)-1:
                    contactlog.append(temp)
                else:
                    continue

def display(contactlog):
    i=1
    for obj in contactlog:
        print(i,".","Name : ",obj.name,"\n","contact No. : ",obj.number,"\n")
        i=i+1


def search_name(contactlog, string):
    contacts=[]
    for obj in contactlog:
        temp=re.search(string, obj.name)
        if temp is not None:
            contacts.append(obj)
    return contacts

contactlog=[]
insert_contact(contactlog, "Parth Prajapati", 1234567890)
insert_contact(contactlog, "Ronak Jethava", 9997455631)
insert_contact(contactlog, "Jigar Makvana", 9874563211)
insert_contact(contactlog, "Smit Savan", 1223342156)
insert_contact(contactlog, "Raj Soni", 4567852130)
insert_contact(contactlog, "Pratham Shah", 5789463214)
insert_contact(contactlog, "Harsh Patel", 75461234578)
insert_contact(contactlog, "Meet Prajapati", 1234578945)
insert_contact(contactlog, "Soham Manglam", 2530354575)
insert_contact(contactlog, "Parth Shah", 1234567891)

while 1:
    print("\n--->Contact Log:\n")
    print("1.Add a new contact","\n2.Search contact No.","\n3.Show All contacts\n4.Nothing\n")

    choice=int(input("Choose What do you want to do: "))

    if choice==1:
        Name=input("Enter Name: ")
        Contact_No=input("Enter Contact No.: ")
        insert_contact(contactlog, Name, Contact_No)
    elif choice==2:
        search_input = input("Enter Name or Word which you want to find : ")
        Contactl=contactlog
        while 1:
            contacts=search_name(Contactl, search_input)
            if len(contacts)==1:
                print("\n",contacts[0].name)
                a=input("Is this Contact number is same as you want to find? [y/n]\n")
                if a=='y':
                    print("\nName: ",contacts[0].name,"\nContact No.: ",contacts[0].number)
                else:
                    print("Name isn't found in Contact List.Check Name")
                break
            elif len(contacts)==0:
                print("Name isn't found in Contact List.Check Name")
                break
            else:
                i = 1
                for obj in contacts:
                    print(i, ".", obj.name)
                    i = i + 1
                Contactl=contacts
                for i in range(len(Contactl)-1):
                    k=0;
                    if Contactl[i].name != Contactl[i+1].name:
                        k=1
                        break
                if k==1:
                    search_input = input("\ntype a Name from Choices given above : ")
                else:
                    i=0
                    print("\nName: ",Contactl[0].name,"\nNumber: ")
                    for obj in Contactl:
                        i=i+1
                        print(i,".",obj.number,"\n")
                    break
    elif choice==3:
        display(contactlog)
    else:
        break





