El usuario ingresa la información del cliente,

  cantidad de tintas,
  ancho
  largo mm,
  tipo de impresión (digital, flexográfica o formas continuas)
  tipo de papel, 
  máquina de impresión, 
  porcentaje de desperdicio del papel

  cantidad de etiquetas a cotizar
  porcentaje de utilidad (ganancia).


Se pueden ingresar múltiples cantidades de etiquetas a cotizar.

Digital: ((área de la etiqueta) * cantidad de etiquetas * costo del papel) + (tiempo de impresión * costo por hora del operador)

Flexográfica: ((área de la etiqueta + desperdicio) * cantidad de etiquetas * costo del papel) + ((tiempo de preparación de la máquina*numero de tintas) * costo por hora del operador)
+ (tiempo de impresión * costo por hora del operador)

Formas continuas: (área de la etiqueta * cantidad de etiquetas * costo del papel) + (tiempo de preparación de la máquina * costo por hora del operador) + (tiempo de impresión * costo por hora del operador)

Cada máquina de impresión debe tener definido el tiempo de preparación en horas, el ancho máximo del rodillo en pulgadas y la velocidad de impresión en pulgadas por minuto.

El sistema debe calcular el costo mínimo de impresión para cada cantidad de etiquetas a cotizar y debe mostrar los datos del cliente, el tamaño de la etiqueta, la cantidad de tintas y el precio cotizado por cada cantidad de etiquetas solicitada