import rclpy
from rclpy.node import Node
from std_msgs.msg import String

# Clase GeekSubscriber heredada de Node
class GeekSubscriber(Node):

	# Constructor de la clase GeekSubscriber
    def __init__(self):
    
    	# Damos nombre al nodo
        super().__init__('nodo_subscriptor')
        
        # Creamos el subscriptor. Cuando reciba mensajes de tipo String 
		# en el topico denominado chatter llamará a la funcion subscriber_callback
        self.subscription = self.create_subscription(String, 'chatter', self.subscriber_callback, 10)

	# Funcion a la que se va a llamar cada vez que se reciba un mensaje
    def subscriber_callback(self, msg):
    
    	# Imprimimos en pantalla el mensaje recibido
        self.get_logger().info('He escuchado: ' + str(msg.data))


def main(args=None):
	# Inicializamos el nodo
    rclpy.init(args=args)

	# Creamos la instancia subscriptor de la clase GeekSubscriber
    subscriptor = GeekSubscriber()

	# Hacemos que se ejecute el nodo ininterrumpidamente
    rclpy.spin(subscriptor)

	# Eliminamos el nodo antes de salir del programa
    # Cuando paramos la ejecucion via CTRl+C, por ejemplo
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
	main()
