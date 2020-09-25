#!/usr/bin/python3

import click
import jinja2


@click.command()
@click.argument('--start', type=int, help='Start number')
@click.argument('--instances', type=int, help='Number of devices to flash')
@click.argument('--tuya-files', type=click.Path(exists=True), help='Location of tuya-convert/files directory')
@click.argument('yaml', type=click.File('r'), help='Base yaml file with templating')
def provision():
    # loop through from 'start' for 'instances' amount, generating a yaml file (templating?)
    # and compiling them, copying them to tuya-convert's flashing directory and flashing
    # before deleting the bin file

    # generate yaml > esphome compile > cp to directory from firmware.bin to NAME.bin > flash using tuya-convert > delete bin
    pass


if __name__ == '__main__':
    provision()
