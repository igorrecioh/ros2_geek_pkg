import rclpy
from rclpy.node import Node
from std_msgs.msg import String

# Clase GeekPublisher heredada de Node
class GeekPublisher(Node):

    # Constructor de la clase
    def __init__(self):

	# Damos nombre al nodo
        super().__init__('nodo_publicador')

	# Creamos el publicador. Transmitirá mensaje de tipo String 
	# en el topico denominado chatter
        self.publicador_ = self.create_publisher(String, 'chatter')

	# Creamos la variable denominada periodo y le asignamos 
	# el valor de 2 segundos
        periodo = 2

	# Creamos el temporizador pasándole el periodo (2seg) y 
	# la funcion a llamar cada 2 segundos (callback)
        self.temporizador = self.create_timer(periodo, self.callback)

	# Variable i que iremos incrementando
        self.i = 0

    # Funcion a la que se va a llamar cada 2 segundos
    def callback(self):

	# Creacion del mensaje de tipo String y asignacion del mensaje a enviar
        msg = String()
        msg.data = 'Mensaje numero ' + str(self.i)

	# Publicamos el mensaje
        self.publicador_.publish(msg)

	# Imprimimos en pantalla el mensaje publicado
        self.get_logger().info('He publicado: ' + str(msg.data))

	# Incrementamos la variable i
        self.i += 1


def main(args=None):

    # Inicializamos el nodo
    rclpy.init(args=args)

    # Creamos la instancia publicador de la clase GeekPublisher
    publicador = GeekPublisher()

    # Hacemos que se ejecute el nodo ininterrumpidamente
    rclpy.spin(publicador)

    # Eliminamos el nodo antes de salir del programa
    # Cuando paramos la ejecucion via CTRl+C, por ejemplo
    publicador.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

