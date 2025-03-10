# -*- coding: utf-8 -*-
"""
rawcorder - Advanced Anomaly Detection in Internet Routing
Copyright (C) 2024 Benedikt Schwering

This software is distributed under the terms of the MIT license.
It can be found in the LICENSE file or at https://opensource.org/licenses/MIT.

Author Benedikt SCHWERING <mail@bschwer.ing>
"""
from src.commands.record import record_command
from src.commands.replay import replay_command
from dotenv import load_dotenv, find_dotenv
from pathlib import Path
import click

load_dotenv(find_dotenv())

@click.group()
def cli():
    pass

@cli.command(
    'record',
)
@click.option(
    '--output',
    '-o',
    type=click.Path(
        dir_okay=False,
        file_okay=True,
        resolve_path=True,
    ),
    required=True,
)
@click.option(
    '--append',
    '-a',
    is_flag=True,
)
def record(output: str, append: bool):
    """ Record Queue Data to a file.

        Author:
            Benedikt SCHWERING <mail@bschwer.ing>

        Params:
            output (str): The path to the output file.
            append (bool): Append to the file.
    """
    record_command(
        output=Path(output),
        append=append,
    )

@cli.command(
    'replay',
)
@click.option(
    '--input',
    '-i',
    type=click.Path(
        dir_okay=False,
        file_okay=True,
        resolve_path=True,
        exists=True,
    ),
    required=True,
)
@click.option(
    '--delay',
    '-d',
    type=int,
    default=500,
    show_default=True,
)
def replay(input: str, delay: int):
    """ Replay Queue Data from a file.
    
        Author:
            Benedikt SCHWERING <mail@bschwer.ing>

        Params:
            input (str): The path to the input file.
            delay (int): The delay between each message in milliseconds.
    """
    replay_command(
        input=Path(input),
        delay=delay,
    )
