En el codigo del archivo deber3
Muestra una interfaz interactiva con el usuario de un campo de futbol con su respectivo balon, cuando el sobrepase la linea de meta aparecera un mensaje de gol, el mensaje cambia de color dependiendo de donde se anote el gol
para este codigo se usa la libreria tkinter
esta libreria posee varias herramientas que son utiles para programar

La sentencia tk=Tk() crea la ventana principal del programa, y la asigna a la variable w. Toda interfaz gráfica debe tener una ventana principal en la que se irán agregando cosas. Esta línea va al principio del programa.
La sentencia tk.mainloop() indica a la interfaz que debe quedarse esperando a que el usuario haga algo. Esta línea siempre debe ir al final del programa.
Al ejecutarlo, puede darse cuenta que el programa no termina. Esto ocurre porque la llamada al método mainloop() se «queda pegada» esperando que algo ocurra. Esto se llama un ciclo de eventos, y es simplemente un ciclo infinito que está continuamente esperando que algo ocurra.
Todos los programas con interfaz gráfica deben seguir esta estructura: la creación de la ventana al principio del programa y la llamada al ciclo de eventos al final del programa.

El widget de Canvas proporciona facilidades gráficas para Tkinter. Entre estos objetos gráficos se encuentran líneas, círculos, imágenes e incluso otros widgets. Con este widget es posible dibujar gráficos y diagramas, crear editores de gráficos e implementar varios tipos de widgets personalizados. 

