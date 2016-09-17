#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""{{ cookiecutter.title }}.

{{ cookiecutter.short_description }}
"""
import logging

__title__ = '{{ cookiecutter.title }}'
__author__ = '{{ cookiecutter.full_name }}'
__email__ = '{{ cookiecutter.email }}'
__version__ = '0.1.0'


def main():
    """Main entry point."""
    log_file, log_level = (None, logging.DEBUG)
    log_format = '%(levelname)s: %(message)s'
    logging.basicConfig(filename=log_file, level=log_level, format=log_format)
    logging.info('Running %s', __file__)
    # TODO: Add some useful code.
    raise NotImplementedError('Add calling code to main() function.')

if __name__ == '__main__':
    main()
