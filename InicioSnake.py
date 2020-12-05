import turtle


Ventana=turtle.Screen()
Ventana.title('Iniciar')
Ventana.setup(width=600,height=600)
Ventana.bgcolor('#FFFFFF')
Ventana.bgpic("img/FondoIniciar.gif")
Ventana.register_shape("img/FondoIniciar.gif")
Ventana.register_shape("img/star.gif")

BotonIniciar=turtle.Turtle()
BotonIniciar.shape("img/star.gif")
BotonIniciar.speed(0)
BotonIniciar.color('#FCDC6D')
BotonIniciar.penup()
BotonIniciar.goto(0,-110)

#TEXTO1
texto1= turtle.Turtle()
texto1.speed(0)
texto1.color('#FCDC6D')
texto1.penup()
texto1.hideturtle()
texto1.goto(0,150)
texto1.write('Game', align='center', font=('Poppins',25, 'bold'))

#TEXTO2
texto2= turtle.Turtle()
texto2.speed(0)
texto2.color('#FCDC6D')
texto2.penup()
texto2.hideturtle()
texto2.goto(0,30)
texto2.write('Snake', align='center', font=('Poppins',80, 'bold'))

#DETECTAR CLICK
def BtnoClick(x,y): 
       if(x > -73 < 70 and y > -143 and y < -80):
        import turtle
        import time
        import random

        posponer= 0.1
        texto1.clear()
        texto2.clear()
        BotonIniciar.hideturtle()
        #MARCADOR
        score=0
        highScore=0

        #CONFIGURACION DE LA VENTANA
        Ventana=turtle.Screen()
        Ventana.title('Juego Snake')
        Ventana.setup(width=600,height=600)
        Ventana.bgcolor('#FFFFFF')
        Ventana.bgpic("img/FondoJuego.gif")
        Ventana.tracer(0)

        #REGISTRAR IMAGENES
        Ventana.register_shape("img/Comida.gif")
        Ventana.register_shape("img/FondoJuego.gif")
        Ventana.register_shape('img/SnakeCafeUp.gif')
        Ventana.register_shape('img/SnakeCafeDown.gif')
        Ventana.register_shape('img/SnakeCafeLeft.gif')
        Ventana.register_shape('img/SnakeCafeRight.gif')

        #CABEZA SERPIENTE
        cabeza=turtle.Turtle()
        cabeza.speed(0)
        cabeza.shape('img/SnakeCafeUp.gif')
        cabeza.right(90)
        cabeza.color('#16DA34')
        cabeza.penup()
        cabeza.goto(0,0)
        cabeza.direction='stop'

        #COMIDA SERPIENTE

        comida=turtle.Turtle()
        comida.shape('img/Comida.gif')
        comida.color('red')
        comida.speed(0)
        comida.penup()
        comida.goto(0,100)


        #SEGMENTOS/CUERPO
        segmentos=[]

        #TEXTO
        texto= turtle.Turtle()
        texto.speed(0)
        texto.color('white')
        texto.penup()
        texto.hideturtle()
        texto.goto(0,260)
        texto.write('Score: 0             High Score: 0 ', align='center', font=('Courier',17, 'bold'))
        #FUNCIONES DE MOVIMIENTO TECLADO
        def Arriba():
            cabeza.direction='up'
            cabeza.shape('img/SnakeCafeUp.gif')

        def Abajo():
            cabeza.direction='down'
            cabeza.shape('img/SnakeCafeDown.gif')

        def Izquierda():
            cabeza.direction='left'
            cabeza.shape('img/SnakeCafeLeft.gif')

        def Derecha():
            cabeza.direction='right'
            cabeza.shape('img/SnakeCafeRight.gif')


        #FUNCION DE MOVIMIENTOS
        def movimientoSnake():
            if cabeza.direction=='up':
                y = cabeza.ycor()
                cabeza.sety(y + 20)

            if cabeza.direction=='down':
                y = cabeza.ycor()
                cabeza.sety(y - 20)

            if cabeza.direction=='left':
                x = cabeza.xcor()
                cabeza.setx(x - 20)

            if cabeza.direction=='right':
                x = cabeza.xcor()
                cabeza.setx(x + 20)


        #EVENTOS TECLADO

        Ventana.listen()
        Ventana.onkeypress(Arriba, 'Up')
        Ventana.onkeypress(Abajo, 'Down')
        Ventana.onkeypress(Izquierda, 'Left')
        Ventana.onkeypress(Derecha, 'Right')

        
        while True:
            Ventana.update()

        #COLICION BORDER
            if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 280 or cabeza.ycor() < -280:

                #TEXTO FINALIZACION
                texto4= turtle.Turtle()
                texto4.speed(0)
                texto4.color('white')
                texto4.hideturtle()
                texto4.goto(0,0)
                texto4.write('JUEGO TERMINADO', align='center', font=('Courier',30, 'bold'))
                time.sleep(1)
                cabeza.goto(0,0)
                cabeza.direction='stop'

        #Escoder los segmentos.
                for segmento in segmentos:
                    segmento.hideturtle()
         #limpiar lista de segmentos
                segmentos.clear()

        #RESETAR MARCADOR
                score=0
                texto.clear()
                texto.write('Score: {}             High Score: {}'.format(score,highScore),align='center', font=('Courier',17, 'bold'))       
                texto4.clear()
        #COLICION COMIDA
            if cabeza.distance(comida) < 20:
                x = random.randint(-280,280)
                y = random.randint(-280,280)
                comida.goto(x,y)

                NuevoSeg=turtle.Turtle()
                NuevoSeg.speed(0)
                NuevoSeg.shape('circle')
                NuevoSeg.color('#834827')
                NuevoSeg.penup()
                segmentos.append(NuevoSeg)

        #AUMENTAR COMIDA
                score+=10

                if(score > highScore):
                    highScore= score
                texto.clear()    
                texto.write('Score: {}             High Score: {}'.format(score,highScore),align='center', font=('Courier',17, 'bold'))
        
        #MOVER EL CUERPO    
            totalSeg = len(segmentos)
            for index in range(totalSeg-1,0,-1):
                x=segmentos[index-1].xcor()
                y=segmentos[index-1].ycor()
                segmentos[index].goto(x,y)

            if totalSeg > 0:
                x=cabeza.xcor()
                y=cabeza.ycor()
                segmentos[0].goto(x,y)

            movimientoSnake()
            time.sleep(posponer)

            for segmento in segmentos:
                if segmento.distance(cabeza) < 20:
                    texto5= turtle.Turtle()
                    texto5.speed(0)
                    texto5.color('white')
                    texto5.hideturtle()
                    texto5.goto(0,0)
                    texto5.write('JUEGO TERMINADO', align='center', font=('Courier',30, 'bold'))
                    time.sleep(1)
                    cabeza.goto(0,0)
                    cabeza.direction='stop'
                    
                
                #Escoder los segmentos.
                    for segmento in segmentos:
                      segmento.hideturtle()
                #limpiar lista de segmentos
                    segmentos.clear()

                    #RESETAR MARCADOR
                    score=0
                    texto.clear()
                    texto.write('Score: {}             High Score: {}'.format(score,highScore),align='center', font=('Courier',17, 'bold'))
                    texto5.clear()

turtle.onscreenclick(BtnoClick, 1)
turtle.listen()
turtle.done()

