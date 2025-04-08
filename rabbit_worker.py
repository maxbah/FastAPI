#!/usr/bin/env python
import pika
import time

with pika.BlockingConnection(pika.ConnectionParameters('localhost')) as rabbit_con:
    channel = rabbit_con.channel()
    channel.queue_declare(queue='hello') # Создание очереди
    print(' [*] Waiting for messages. To exit press CTRL+C')


    def callback(ch, method, properties, body):
        print(f" [x] Received {body.decode()}")
        time.sleep(body.count(b'.'))
        print(" [x] Done")
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_consume('hello', on_message_callback=callback)
    # channel.basic_consume('math', callback, auto_ack=True)
    channel.start_consuming()
