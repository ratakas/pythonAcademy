import threading

def contar(numero):
    contador = 0
    while contador<500:
        contador+=1
        print(numero, threading.get_ident(), contador)
    
x=0
while x<10:
    hilo = threading.Thread(target=contar, 
                            args=(x,))
    
    print("total ativos: ",threading.active_count())
    if threading.active_count() < 4:
        
        hilo.start()
        x+=1


