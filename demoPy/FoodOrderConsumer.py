import pika
import time  # solo para simular tiempo de preparación

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Escucha la cola de pedidos
    channel.queue_declare(queue='food_orders')

    # Lógica que se ejecuta cuando llega un pedido
    def callback(ch, method, properties, body):
        order = body.decode()
        print(f" [x] Pedido recibido: {order}")
        print(f" [.] Preparando {order}...")
        time.sleep(2)  # simula tiempo de preparación
        print(f" [✓] {order} listo para entregar\n")

    channel.basic_consume(queue='food_orders', on_message_callback=callback, auto_ack=True)

    print(' [*] Esperando pedidos. Presiona CTRL+C para salir')
    channel.start_consuming()

if __name__ == '__main__':
    main()

