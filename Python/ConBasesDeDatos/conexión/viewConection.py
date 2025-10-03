import tkinter as tk
import mysql.connector
#import Connection as myCn
root=tk.Tk()
root.title("Conexión a BD")
root.geometry("600x600")
frameConection=tk.Frame()
label = tk.Label()
label.config(background="gray", width=40, height=10)

#con=myCn.Connection()
def conecctionBD():
    cn=mysql.connector.connect(host='localhost', port=3306, user="root",
                               database="escuela")
    cursor1=cn.cursor()
    cursor1.execute("show databases")
    for base in cursor1:
      print(base)
    print(cn)
    cursor1.close()
def mostrardatos():
  texto_total = ""
  cn=mysql.connector.connect(host='localhost', port=3306, user="root",database="escuela")
  
  cursor1=cn.cursor()
  cursor1.execute("select * from alumnos")
  for fila in cursor1:
    
    print(fila)
    texto_total += str(fila) + "\n_"

  label.configure(text=texto_total)
    

def insertarDatos():
  cn=mysql.connector.connect(host='localhost', port=3306, user="root",database="escuela")
  cursor1=cn.cursor()
  sql="insert into alumnos (matricula,nombre,apellido) values(%s,%s,%s)"
  datos=(12344,"Alex","Téllez")
  cursor1.execute(sql,datos)
  cursor1.close()
  cn.commit()
  print("Datos registrados")
  
def eliminarRegistro():
  cn=mysql.connector.connect(host='localhost', port=3306, user="root",database="escuela")
  cursor1=cn.cursor()
  
  #  con.createConnection()
btnConection=tk.Button(frameConection,text="Conectar BD",command=conecctionBD)
btnConection.pack(pady=15)
btnConection=tk.Button(frameConection,text="Mostrar...",command=mostrardatos)
btnConection.pack(pady=15)

btnConection=tk.Button(frameConection,text="Insertar...",command=insertarDatos)
btnConection.pack(pady=15)

frameConection.pack()
label.pack()
root.mainloop()