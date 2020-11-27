#!/usr/bin/env python3
import os
import sys
import json
import click


INDENT = 2


def echo_infile(infile):
    """Reads a file into text"""
    for line in infile:
        click.echo(line)


class Config(object):

    def __init__(self):
        self.verbose = False


pass_config = click.make_pass_decorator(Config, ensure=True)


@click.group()
@click.argument('infile', type=click.File('r'), default='-')
@click.argument('outfile', type=click.File('w'), default='-')
@click.option('--log-file', '-l', type=click.File('w'), default=sys.stderr)
@click.option('--verbose', '-v', is_flag=True)
@click.option('--json', is_flag=True)
@pass_config
def cli(config, infile, outfile, log_file, verbose, json):
    config.verbose = verbose
    config.json = json
    if config.verbose:
        click.echo("Verbose mode On")
        click.echo(f"JSON output: {json}")
    config.infile = infile
    config.outfile = outfile


@cli.command()
@click.argument('parameter', type=click.STRING)
@click.option('--param_type', type=click.STRING, required=True,
              help='block height, hash, transaction, or address')
@pass_config
def request(config, parameter, param_type):
    """Echos a seed in hex format"""
    param_types = ['block height', 'height', 'hash', 'transaction', 'address']
    if param_type not in param_types:
        raise click.BadOptionUsage(
            message=f'param_type must be one of these: {param_types}',
            option_name="param_type"
        )
    if config.verbose:
        click.echo(f"Sending API request to blockstream")
    click.echo(param_type)
    click.echo(parameter)
