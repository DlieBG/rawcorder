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

def replay_command(input: Path):
    """ Replay Queue Data from a file.
    
        Author:
            Benedikt SCHWERING <mail@bschwer.ing>

        Params:
            input (Path): The path to the input file.
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

    with input.open('rb') as file:
        for line in file:
            # Remove trailing newline.
            line = line.strip()

            print(f'Sending [red]{line}[/]')
            channel.basic_publish(
                exchange='',
                routing_key='frontend_group4',
                body=line,
            )
