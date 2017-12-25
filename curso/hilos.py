import threading

def contar():
    '''Contar hasta cien'''
    contador = 0
    while contador<500:
        contador+=1
        print('Hilo:', 
              threading.current_thread().getName(), 
              'con identificador:', 
              threading.current_thread().ident,
              'Contador:', contador)

hilo1 = threading.Thread(target=contar)
hilo2 = threading.Thread(target=contar)
hilo3 = threading.Thread(target=contar)
hilo4 = threading.Thread(target=contar)
hilo5 = threading.Thread(target=contar)
hilo6 = threading.Thread(target=contar)
hilo1.start()
hilo2.start()
hilo3.start()
hilo4.start()
hilo5.start()
hilo6.start()


