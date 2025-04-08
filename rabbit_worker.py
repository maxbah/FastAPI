#!/usr/bin/env python
import pika
import time
import sys


with pika.BlockingConnection(pika.ConnectionParameters('localhost')) as rabbit_con:
    channel = rabbit_con.channel()
    channel.exchange_declare(exchange='direct_logs',
                             exchange_type='direct') # Создание обменника
    result = channel.queue_declare(queue='', durable=True, exclusive=True)  # Создание очереди
    queue_name = result.method.queue
    severities = sys.argv[1:]

    if not severities:
        sys.stderr.write("Usage: %s [info] [warning] [error]\n" % sys.argv[0])
        sys.exit(1)

    for severity in severities:
        channel.queue_bind(exchange="direct_logs", queue=queue_name, routing_key=severity)
        print(' [*] Waiting for messages. To exit press CTRL+C')


    def callback(ch, method, properties, body):
        print(f" [x] Received {body.decode()}")
        time.sleep(body.count(b'.'))
        print(f" [x] {method.routing_key}:{body}")
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue=queue_name, on_message_callback=callback)
    channel.start_consuming()
