#prototipado agenda
#voy a hacer una ventana con la opcion de ingresar contacto

from tkinter import *
from tkinter import messagebox
from ContactoAgenda import *

#
#
#------------------------------------------TO DO
#
#falta hacer el label del --> def findThis que diga que no se han encontrado coincidencias.
#ver si existe la posibilidad real de "borrar". ver como se borran en diccionarios y entender la aplicacion real.
#IMPLEMENTAR::: ErrorAddContact  -- mensaje de error en forma de vantana pop up




#--------------------Creating GUI
root=Tk()
root.title("Agenda")
root.config(bg="black")
#root.resizable(0,0)

frame1=Frame(root,bg="black",width=500,height=400)
frame1.pack(fill=X, expand=True)

frame2=Frame(root,bg="black",width=500,height=400)
frame2.pack()

#--------------------Fixing Dimensions
l1=Label(frame1,bg="black",fg="red",text="-------------------------------------------------------------------------")
l1.grid(row=5,column=1)
l2=Label(frame2,bg="black",text="                                                                                                                          ")
l2.grid(row=5,column=0)

#--------------------Creating Dictionary
agenda={}
index=0

#--------------------Methods

def EraseWidget():
	global frame2
	for widget in frame2.winfo_children():
		widget.destroy()
	nameAddString.set("")
	surnameAddString.set("")
	cityAddString.set("")
	phoneAddString.set("")
	nameSearchString.set("")
	surnameSearchString.set("")
	citySearchString.set("")
	phoneSearchString.set("")

def AddContact():
	EraseWidget()
	auxLabel=Label(frame2,text="Completar los datos: ",fg="yellow",bg="#575348")
	auxLabel.grid(row=0,column=0,columnspan=8)
	labelAddName=Label(frame2,text="Nombre",fg="yellow",bg="#575348",width=15)
	labelAddName.grid(row=1,column=1,sticky="e")
	entryAddName=Entry(frame2,textvariable=nameAddString,bg="black",fg="yellow",width=20,justify="left")
	entryAddName.grid(row=1,column=2,sticky="nsew")
	labelAddSurname=Label(frame2,text="Apellido",fg="yellow",bg="#575348",width=15)
	labelAddSurname.grid(row=2,column=1,sticky="nsew")
	entryAddSurname=Entry(frame2,textvariable=surnameAddString,bg="black",fg="yellow",width=20,justify="left")
	entryAddSurname.grid(row=2,column=2,sticky="nsew")
	labelAddCity=Label(frame2,text="Ciudad",fg="yellow",bg="#575348",width=15)
	labelAddCity.grid(row=3,column=1,sticky="nsew")
	entryAddCity=Entry(frame2,textvariable=cityAddString,bg="black",fg="yellow",width=20,justify="left")
	entryAddCity.grid(row=3,column=2,sticky="nsew")
	labelAddPhone=Label(frame2,text="Telefono",fg="yellow",bg="#575348",width=15)
	labelAddPhone.grid(row=4,column=1,sticky="nsew")
	entryAddPhone=Entry(frame2,textvariable=phoneAddString,bg="black",fg="yellow",width=20,justify="left")
	entryAddPhone.grid(row=4,column=2,sticky="nsew")

	labelAux=Label(frame2,text="",bg="black",fg="yellow")
	labelAux.grid(row=5,column=0,columnspan=5)
	buttonRegistry=Button(frame2,text="Registrar Contacto",command=lambda:RegisterContact())
	buttonRegistry.grid(row=6,column=3)

def CheckRegister():

	if nameAddString.get() == "" or surnameAddString.get() == "" or cityAddString.get() == "" or phoneAddString.get() == "":
		return False
	else:
		return True

def ErrorAddContact():
	messagebox.showinfo("Error al registrar contacto","Uno o más de los campos están vacíos")

def RegisterContact():
	#Tengo que pasar todos los datos de los <name>AddString al diccionario.
	#tiene que chequear que estén todos los field llenos, en caso contrario, que avise con un pop up que falta.
	if CheckRegister() == True:
		global index

		auxName=nameAddString.get()
		auxSurname=surnameAddString.get()
		auxCity=cityAddString.get()
		auxPhone=phoneAddString.get()
		contact=ContactoAgenda(auxName.lower(),auxSurname.lower(),auxCity.lower(),auxPhone)
		agenda[index]=contact
		index +=1
		#despues sigue el codigo
		EraseWidget()
		#---------MESSAGE: Register done.
		label1=Label(frame2,text="Contacto Registrado",bg="black",fg="yellow")
		label1.grid(row=1,column=1,columnspan=5)
	else:
		label1=Label(frame2,text="ERROR al ingresar los datos. Todos los campos tienen que estar llenos.")
		label1.grid(row=7,column=1,columnspan=5)
		label11=Label(frame2,text="                      ",bg="black")
		label11.grid(row=8,column=1,columnspan=5)

def DeleteContact():

	EraseWidget()
	labelName=Label(frame2,text="Nombre",fg="white",bg="green",width=15)
	labelName.grid(row=0,column=3,sticky="nsew")
	entryName=Entry(frame2,textvariable=nameSearchString,bg="black",fg="blue",width=20,justify="left")
	entryName.grid(row=0,column=4,sticky="nsew")
	buttonGoName=Button(frame2,text="Buscar",command=lambda:findThis(0,nameSearchString.get(),1),width=12)
	buttonGoName.grid(row=0,column=5,sticky="nsew")
	#----Surname
	labelSurname=Label(frame2,text="Apellido",fg="white",bg="green")
	labelSurname.grid(row=1,column=3,sticky="nsew")
	entrySurname=Entry(frame2,textvariable=surnameSearchString,bg="black",fg="blue",width=20,justify="left")
	entrySurname.grid(row=1,column=4,sticky="nsew")
	buttonGoSurname=Button(frame2,text="Buscar",command=lambda:findThis(1,surnameSearchString.get(),1),width=12)
	buttonGoSurname.grid(row=1,column=5,sticky="nsew")
	#----City
	labelCity=Label(frame2,text="Ciudad",fg="white",bg="green")
	labelCity.grid(row=2,column=3,sticky="nsew")
	entryCity=Entry(frame2,textvariable=citySearchString,bg="black",fg="blue",width=20,justify="left")
	entryCity.grid(row=2,column=4,sticky="nsew")
	buttonGoCity=Button(frame2,text="Buscar",command=lambda:findThis(2,citySearchString.get(),1),width=12)
	buttonGoCity.grid(row=2,column=5,sticky="nsew")
	#----Phone
	labelPhone=Label(frame2,text="Telefono",fg="white",bg="green")
	labelPhone.grid(row=3,column=3,sticky="nsew")
	entryPhone=Entry(frame2,textvariable=phoneSearchString,bg="black",fg="blue",width=20,justify="left")
	entryPhone.grid(row=3,column=4,sticky="nsew")
	buttonGoPhone=Button(frame2,text="Buscar",command=lambda:findThis(3,phoneSearchString.get(),1),width=12)
	buttonGoPhone.grid(row=3,column=5,sticky="nsew")

def nowDelete(indexNumber):
	EraseWidget()
	global agenda
	#lo que voy a hacer es copiar el último al lugar del index number y luego borrar el ultimo
	#despues, reordeno
	print("en nowDelete")
	aux=len(agenda)
	print("aux (len(agenda)) -> ",aux)
	if aux > 0:
		agenda[indexNumber]=agenda[aux-1]
		del (agenda[aux-1])
		ReordenarAgenda()
	else:
		del (agenda[indexNumber])

def ReordenarAgenda():
	global agenda
	for x in range(len(agenda)):
		for y in range(len(agenda)-1):
			if agenda[x].getName() > agenda[y+1].getName() and y >= x:
				aux=agenda[y+1]
				agenda[y+1]=agenda[x]
				agenda[x]=aux

def SearchContact():
	EraseWidget()
	#acá tendrian que aparecer los labels de las busquedas parciales y luego, los entry, posteriormente los botones.
	#----Name
	labelName=Label(frame2,text="Nombre",fg="white",bg="#575348",width=15)
	labelName.grid(row=0,column=3,sticky="nsew")
	entryName=Entry(frame2,textvariable=nameSearchString,bg="black",fg="yellow",width=20,justify="left")
	entryName.grid(row=0,column=4,sticky="nsew")
	buttonGoName=Button(frame2,text="Buscar",command=lambda:findThis(0,nameSearchString.get(),0),width=12)
	buttonGoName.grid(row=0,column=5,sticky="nsew")
	#----Surname
	labelSurname=Label(frame2,text="Apellido",fg="white",bg="#575348")
	labelSurname.grid(row=1,column=3,sticky="nsew")
	entrySurname=Entry(frame2,textvariable=surnameSearchString,bg="black",fg="yellow",width=20,justify="left")
	entrySurname.grid(row=1,column=4,sticky="nsew")
	buttonGoSurname=Button(frame2,text="Buscar",command=lambda:findThis(1,surnameSearchString.get(),0),width=12)
	buttonGoSurname.grid(row=1,column=5,sticky="nsew")
	#----City
	labelCity=Label(frame2,text="Ciudad",fg="white",bg="#575348")
	labelCity.grid(row=2,column=3,sticky="nsew")
	entryCity=Entry(frame2,textvariable=citySearchString,bg="black",fg="yellow",width=20,justify="left")
	entryCity.grid(row=2,column=4,sticky="nsew")
	buttonGoCity=Button(frame2,text="Buscar",command=lambda:findThis(2,citySearchString.get(),0),width=12)
	buttonGoCity.grid(row=2,column=5,sticky="nsew")
	#----Phone
	labelPhone=Label(frame2,text="Telefono",fg="white",bg="#575348")
	labelPhone.grid(row=3,column=3,sticky="nsew")
	entryPhone=Entry(frame2,textvariable=phoneSearchString,bg="black",fg="yellow",width=20,justify="left")
	entryPhone.grid(row=3,column=4,sticky="nsew")
	buttonGoPhone=Button(frame2,text="Buscar",command=lambda:findThis(3,phoneSearchString.get(),0),width=12)
	buttonGoPhone.grid(row=3,column=5,sticky="nsew")

def showMeAllContacts():
	EraseWidget()
	global agenda
	if len(agenda) == 0:
		label0=Label(frame2,text="                                                           ",bg="black")
		label0.grid(row=0,column=0,columnspan=5,sticky="nsew")
		label1=Label(frame2,text="La agenda está vacía.",bg="black",fg="white")
		label1.grid(row=1,column=0,columnspan=5,rowspan=4)
		label2=Label(frame2,text="                      ",bg="black")
		label2.grid(row=7,column=0,columnspan=5)
		label3=Label(frame2,text="                      ",bg="black")
		label3.grid(row=8,column=0,columnspan=5)
		label4=Label(frame2,text="                      ",bg="black")
		label4.grid(row=9,column=0,columnspan=5)
	else:
		ReordenarAgenda()
		fila=0
		for x in range(len(agenda)):
			aux=agenda[x]
			showMe(aux.getName(),aux.getSurname(),aux.getCity(),aux.getPhone(),fila)
			fila=fila+5

def findThis(option,findThisString,typeOfSearch):
	#esta funcion envia 0/1/2/3 dependiendo la opcion.
	#option es para identificar si el parametro pasado es nombre/apellido/etc
	#findThisString es lo que ha ingresado el usuario
	#el typeOfSearch --> 0 si es por search normal y 1 si es search para borrar

	#el contactFind va a devolver el string con el contacto registrado, que se pone True si lo encuentra.	
	contactFind=False

	global agenda

	#el mostrar con index va a ser un array con el "index" del {agenda} en donde se haya hecho match.
	#tengo que hacer una funcion que pasándole ese array, me muestre los resultados. 
	auxInd=0

	if option==0:
		for contact in agenda:
			auxContact=agenda[contact]
			if auxContact.getName() == findThisString.lower():
			   auxInd=contact
			  # mostrarConIndex.append(contact)
			   contactFind=True

	if option==1:
		for contact in agenda:
			auxContact=agenda[contact]
			if auxContact.getSurname() == findThisString.lower():
			   auxInd=contact
			   #mostrarConIndex.append(contact)
			   contactFind=True		
	if option==2:
		for contact in agenda:
			auxContact=agenda[contact]
			if auxContact.getCity() == findThisString.lower():
			   auxInd=contact
			   #mostrarConIndex.append(contact)
			   contactFind=True
	if option==3:
		for contact in agenda:
			auxContact=agenda[contact]
			if auxContact.getPhone() == findThisString:
			   auxInd=contact 
			   #mostrarConIndex.append(contact)
			   contactFind=True
	
	#borramos la ventana inferior
	EraseWidget()

	#hago la comprobacion si encontró el contacto y con el typeOfSearch veo si es para borrar o mostrar.

	if contactFind==True:
		if typeOfSearch==0:		
			viewContacts(auxInd)
		else:
			nowDelete(auxInd)
	else:
		errorLabel=Label(frame2,text="No existe ese contacto. Vuelva a intentarlo.",fg="white",bg="black")
		errorLabel.grid(row=1,column=1,sticky="nsew")

def viewContacts(mostrar):
	global agenda
	aux=agenda[mostrar]
	#showMe(aux.getName(),aux.getSurname(),aux.getCity(),aux.getPhone())
	showMe(aux.getName(),aux.getSurname(),aux.getCity(),aux.getPhone(),0)

def showMeDeprecated(nname,ssurname,ccity,pphone):
	EraseWidget()
	labelName1=Label(frame2,text="Nombre",fg="white",bg="#575348",width=15)
	labelName1.grid(row=0,column=1,sticky="nsew")
	labelName2=Label(frame2,text=nname.capitalize(),bg="yellow",fg="black",width=20,justify="left")
	labelName2.grid(row=0,column=3,sticky="nsew")
	labelSurname1=Label(frame2,text="Apellido",fg="white",bg="#575348",width=15)
	labelSurname1.grid(row=1,column=1,sticky="nsew")
	labelSurname2=Label(frame2,text=ssurname.capitalize(),bg="black",fg="yellow",width=20,justify="left")
	labelSurname2.grid(row=1,column=3,sticky="nsew")
	labelCity1=Label(frame2,text="Ciudad",fg="white",bg="#575348",width=15)
	labelCity1.grid(row=2,column=1,sticky="nsew")
	labelCity2=Label(frame2,text=ccity.capitalize(),bg="black",fg="yellow",width=20,justify="left")
	labelCity2.grid(row=2,column=3,sticky="nsew")
	labelPhone1=Label(frame2,text="Telefono",fg="white",bg="#575348",width=15)
	labelPhone1.grid(row=3,column=1,sticky="nsew")
	labelPhone2=Label(frame2,text=pphone,bg="black",fg="yellow",width=20,justify="left")
	labelPhone2.grid(row=3,column=3,sticky="nsew")
	labelEndFrame=Label(frame2,text="-------------------------------------------------",bg="black",fg="blue")
	labelEndFrame.grid(row=4,column=0,columnspan=4,sticky="nsew")


def showMe(nname,ssurname,ccity,pphone,fila):
	labelName1=Label(frame2,text="Nombre",fg="white",bg="#575348",width=15)
	labelName1.grid(row=fila+1,column=1,sticky="nsew")
	labelName2=Label(frame2,text=nname.capitalize(),bg="yellow",fg="black",width=20,justify="left")
	labelName2.grid(row=fila+1,column=3,sticky="nsew")
	labelSurname1=Label(frame2,text="Apellido",fg="white",bg="#575348",width=15)
	labelSurname1.grid(row=fila+2,column=1,sticky="nsew")
	labelSurname2=Label(frame2,text=ssurname.capitalize(),bg="black",fg="yellow",width=20,justify="left")
	labelSurname2.grid(row=fila+2,column=3,sticky="nsew")
	labelCity1=Label(frame2,text="Ciudad",fg="white",bg="#575348",width=15)
	labelCity1.grid(row=fila+3,column=1,sticky="nsew")
	labelCity2=Label(frame2,text=ccity.capitalize(),bg="black",fg="yellow",width=20,justify="left")
	labelCity2.grid(row=fila+3,column=3,sticky="nsew")
	labelPhone1=Label(frame2,text="Telefono",fg="white",bg="#575348",width=15)
	labelPhone1.grid(row=fila+4,column=1,sticky="nsew")
	labelPhone2=Label(frame2,text=pphone,bg="black",fg="yellow",width=20,justify="left")
	labelPhone2.grid(row=fila+4,column=3,sticky="nsew")
	labelEndFrame=Label(frame2,text="-------------------------------------------------",bg="black",fg="blue")
	labelEndFrame.grid(row=fila+5,column=0,columnspan=4,sticky="nsew")


#--------------------------VARIABLES
nameAddString=StringVar()
surnameAddString=StringVar()
cityAddString=StringVar()
phoneAddString=StringVar()
nameSearchString=StringVar()
surnameSearchString=StringVar()
citySearchString=StringVar()
phoneSearchString=StringVar()


#--------------------------BUTTON
buttonAddEntry=Button(frame1,text="Agregar contacto",command=lambda:AddContact())
buttonAddEntry.grid(row=0,column=1,sticky="nsew")
buttonShowList=Button(frame1,text="Mostrar todos los contactos",command=lambda:showMeAllContacts())
buttonShowList.grid(row=1,column=1,sticky="nsew")
#-----------------------------------------------------------------Modificar esto "gas", tengo que pedir dato al usuario------
buttonDeleteEntry=Button(frame1,text="Borrar contacto",command=lambda:DeleteContact())
#----------------------------------------------------------------------------------------------------------------------------
buttonDeleteEntry.grid(row=2,column=1,sticky="nsew")
buttonSearch=Button(frame1,text="Buscar contacto",command=lambda:SearchContact())
buttonSearch.grid(row=3,column=1,sticky="nsew")


root.mainloop()