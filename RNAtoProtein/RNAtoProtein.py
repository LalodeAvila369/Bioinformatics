#RNA to Protein


from textwrap import wrap

def separatesesamo (RNACadena, long, isChar):
	if long == 3 and isChar==False:
		return (RNACadena[0],RNACadena[1],RNACadena[2])
	else:
		return wrap(RNACadena,3)

def convert (lista):
	return "-".join(lista)


RNA=input("Introduce Caneda RNA: ")
RNA_Triple = separatesesamo(RNA,len(RNA),True)
Protein=[]
Prot=[]


for i in RNA_Triple:
	Tripleta=separatesesamo(i,len(i),False)
	if Tripleta[0]=="A":								############Sección A
		if Tripleta[1]=="A":
			if Tripleta[2] == "A" or Tripleta[2] == "G":
				Protein.append("Lisina")
				Prot.append("Lys")

			else:
				Protein.append("Asparragina")
				Prot.append("Asn")
				

		elif Tripleta[1]=="C":
			Protein.append("Treonina")
			Prot.append("Thr")
			

		elif Tripleta[1]=="U":
			if Tripleta[2] == "G":
				Protein.append("Metionina")
				Prot.append("Met")
				
			else:
				Protein.append("Isoleucina")
				Prot.append("Ile")
				

		elif Tripleta[1]=="G":
			if Tripleta[2]== "G" or Tripleta[2] == "A":
				Protein.append("Arginina")
				Prot.append("Arg")
				
			else:
				Protein.append("Serina")
				Prot.append("Ser")
				

		else: 
			print("Error en Cadena Introducida")

	elif Tripleta[0]=="C":							#############Sección C
		if Tripleta[1]=="A":
			if Tripleta[2]=="G" or Tripleta[2] == "A":
				Protein.append("Glutamina")
				Prot.append("Gln")
				
			else:
				Protein.append("Histidina")
				Prot.append("His")
				

		elif Tripleta[1]=="C":
			Protein.append("Prolina")
			Prot.append("Pro")
			

		elif Tripleta[1]=="U":
			Protein.append("Leucina")
			Prot.append("Leu")
			
		elif Tripleta[1]=="G":
			Protein.append("Arginina")
			Prot.append("Arg")
			
		else: 
			print("Error en Cadena Introducida")


	elif Tripleta[0]=="U":							#############Sección C
		if Tripleta[1]=="A":
			if Tripleta[2]=="A" or Tripleta[2]=="G":
				Protein.append("Stop")
				Prot.append("Stop")
				
			else:
				Protein.append("Tirosina")
				Prot.append("Tyr")
				

		elif Tripleta[1]=="C":
			Protein.append("Serina")
			Prot.append("Ser")
			

		elif Tripleta[1]=="U":
			if Tripleta[2]=="A" or Tripleta[2]=="G":
				Protein.append("Leucina")
				Prot.append("Leu")
				
			else:
				Protein.append("Fenilalanina")
				Prot.append("Phe")
				

		elif Tripleta[1]=="G":
			if Tripleta[2]=="A":
				Protein.append("Stop")
				Prot.append("Stop")
				
			elif Tripleta[2]=="G":
				Protein.append("Triptofano")
				Prot.append("Trp")
				
			else:
				Protein.append("Cisteina")
				Prot.append("Cys")
				
		else: 
			print("Error en Cadena Introducida")

	elif Tripleta[0]=="G":
		if Tripleta[1]=="A":
			if Tripleta[2]=="A" or Tripleta[2]=="G":
				Protein.append("Acido Glutamico")
				Prot.append("Glu")
				
			else:
				Protein.append("Acido Aspartico")
				Prot.append("Asp")

		elif Tripleta[1]=="C":
			Protein.append("Alanina")
			Prot.append("Ala")

		elif Tripleta[1]=="U":
			Protein.append("Valina")
			Prot.append("Val")
			
		elif Tripleta[1]=="G":
			Protein.append("Glicina")
			Prot.append("Gly")
			
		else: 
			print("Error en Cadena Introducida")
	else: 
		print("Error en Cadena Introducida")
	print(Tripleta)
print("La cadena introducida de RNA es: "+str(RNA))
print("La tripleta es: "+str(RNA_Triple))
print("La traducción es: "+convert(Protein))
print("La traducción con abreviaturas es: "+convert(Prot))
