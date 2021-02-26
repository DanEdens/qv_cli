"""
    Init file for generators

    TODO: move imports to this location,
    TODO: to allow use as a stand alone module
"""
# __name__ = 'generators'

from .generator import Generator


async def generator(project):
    """ Entry point for Adaptive card Generator """
    staged_file = Generator(project)
    return staged_file.compile_data()
