#!/usr/bin/env python
import pika
import sys

with pika.BlockingConnection(pika.ConnectionParameters('localhost')) as rabbit_con:
    channel = rabbit_con.channel()
    channel.queue_declare(queue='hello')  # Создание очереди

    message = ' '.join(sys.argv[1:]) or "Hello World!"
    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body=f'{message}')
    print(f" [x] Sent {message}")

