import pika

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declarar una cola de pedidos de comida
    channel.queue_declare(queue='food_orders')

    # Simular envío de pedidos
    orders = ['Pizza', 'Hamburguesa', 'Tacos', 'Sushi', 'Empanadas']

    for order in orders:
        channel.basic_publish(exchange='',
                              routing_key='food_orders',
                              body=order)
        print(f" [x] Pedido enviado: {order}")

    connection.close()

if __name__ == '__main__':
    main()
