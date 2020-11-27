#!/usr/bin/env python3
import os
import sys
import json
import click
from . import blockexplorer


INDENT = 2


def echo_infile(infile):
    """Reads a file into text"""
    for line in infile:
        click.echo(line)


def blockstream_request(param_type, parameter):
    """
    Make blockstream function call based on type requested
    height, hash, transaction or address
    """
    if param_type == 'height':
        return blockexplorer.get_block_by_height(parameter)
    if param_type == 'hash':
        return blockexplorer.get_block_by_hash(parameter)
    if param_type == 'transaction':
        return blockexplorer.get_transaction(parameter)
    if param_type == 'address':
        return blockexplorer.get_address(parameter)
    return {"message": "Error, must be height, hash, transaction, or address"}


class Config(object):

    def __init__(self):
        self.verbose = False


pass_config = click.make_pass_decorator(Config, ensure=True)


@click.group()
@click.argument('infile', type=click.File('r'), default='-')
@click.argument('outfile', type=click.File('w'), default='-')
@click.option('--verbose', '-v', is_flag=True)
@pass_config
def cli(config, infile, outfile, verbose):
    config.verbose = verbose
    if config.verbose:
        click.echo("Verbose mode On")
    config.infile = infile
    config.outfile = outfile


@cli.command()
@click.argument('parameter', type=click.STRING, default="")
@click.option('--param_type', type=click.STRING, required=True,
              help='height, hash, transaction, or address')
@pass_config
def request(config, parameter, param_type):
    """Makes a request to blockstream info api and echos response"""
    param_types = ['height', 'hash', 'transaction', 'address']
    if param_type not in param_types:
        raise click.BadOptionUsage(
            message=f'param_type must be one of these: {param_types}',
            option_name="param_type"
        )
    if config.verbose:
        click.echo(f"Sending API request to blockstream")
    if parameter:
        response = blockstream_request(param_type, parameter)
    else:
        input_parameter = config.infile.readline().strip()
        response = blockstream_request(param_type, input_parameter)
    click.echo(json.dumps(response.serialized(), indent=INDENT))
