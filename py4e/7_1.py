#7.1 Write a program that prompts for a file name, then opens that file and reads through the file,
 #and print the contents of the file in upper case.
 #Use the file words.txt to produce the output below.

#Solicitamos el nombre del fichero
ipfile = input("Enter file name:")
try:
    #Abrimos el  handle del fichero
    txthandle = open(ipfile)
    #Extraemos todo el contenido en la variable
    txt = txthandle.read()
    #Convertimos en Upper e imprimimos
    print(txt.upper())
except:
    print("The file doesn't exist")
    quit()
