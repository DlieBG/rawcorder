# -*- coding: utf-8 -*-
"""
rawcorder - Advanced Anomaly Detection in Internet Routing
Copyright (C) 2024 Benedikt Schwering

This software is distributed under the terms of the MIT license.
It can be found in the LICENSE file or at https://opensource.org/licenses/MIT.

Author Benedikt SCHWERING <mail@bschwer.ing>
"""
from pathlib import Path
from rich import print
import pika, os

def record_command(output: Path, append: bool):
    """ Record Queue Data to a file.
    
        Author:
            Benedikt SCHWERING <mail@bschwer.ing>

        Params:
            output (Path): The path to the output file.
            append (bool): Append to the file.
    """
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host=os.getenv('RABBIT_MQ_HOST'),
        ),
    )
    channel = connection.channel()

    channel.queue_declare(
        queue='frontend_group4',
        durable=True,
    )

    # Clear the output file if not in append mode.
    if not append:
        if output.exists():
            output.unlink()
        output.touch()

    def callback(ch, method, properties, body):
        print(f'Received [green]{body}[/]')
        with output.open('ab') as file:
            file.write(body + '\n'.encode())

    channel.basic_consume(
        queue='frontend_group4',
        on_message_callback=callback,
        auto_ack=True,
    )

    print('[blue]Waiting for messages. To exit press CTRL+C[/]')
    channel.start_consuming()
