"""
    Geo-Instruments
    Sitecheck Scanner

Loads program configuration as a project.tuple object
"""
import configparser
import os.path
import subprocess
import sys
import paho.mqtt as mqtt

from . import *

logger = logging.getLogger('config')
projectstore = os.environ.get('ROOT_DIR', '~') + '/projects.ini'


def edit_txtfile(file=projectstore, header=None):
    """
    Subprocess edit Project configuration file in notepad.

    ::returns:: Edit subprocess returncode
    """
    logger.info(f"{file} file opened. Please close to continue..")
    if header is not None:
        from . import utlis
        utlis.ensure_exists(file)
        with open(file, 'a+') as f:
            content = f.read()
            f.seek(0, 0)
            f.write(header.rstrip('\r\n') + '\n' + content)
    if os.supports_bytes_environ:
        subprocess.Popen(
            [os.environ.get('SCANNER_EDITOR', "vim"), file]
            ).wait()
    else:
        subprocess.Popen(
            [os.environ.get('SCANNER_EDITOR', "notepad"), file]
            ).wait()


def edit_config_option(project, option, value):
    """
    Change an option in the projects.ini file
    :param project: Project who's config to edit
    :param option: Option to edit
    :param value: New value of the option
    Example - edit_config_option(
    """
    config = configparser.ConfigParser()
    config.read(projectstore)
    config[project][option] = value
    try:
        with open(projectstore, 'w') as configfile:
            config.write(configfile)
            logger.debug(f'Editted config file: {project}, {option}, {value}')
    except configparser.Error as err:
        return err


def file_dialog():
    """
        Check and use Tkinter for file dialog, or call generate_default.

        ::returns:: filename
    """
    try:
        import tkinter
        from tkinter import filedialog

        options = {}
        options['defaultextension'] = '.ini'
        options['filetypes'] = [('ini config files', '.ini')]
        options['initialdir'] = os.environ['ROOT_DIR']
        options['initialfile'] = 'projects.ini'
        options['title'] = 'Select Project Configuration File'
        root = tkinter.Tk()
        filename = filedialog.askopenfilename(**options)
        root.destroy()
        return filename
    except ImportError:
        pass


def read_config_file():
    """
    Prompts user to select projects.ini configuration and returns contents as list
    Default projects.ini is ROOT_DIR+"\\project.ini"

    :rtype: list
    """
    if os.path.isfile(projectstore):
        config_file = projectstore
    else:
        config_file = file_dialog()

    if config_file == '':
        sys.exit("No Config selected. Exiting..")
    elif not os.path.isfile(config_file):
        logger.critical("file (%s) not found. " % config_file)
        sys.exit("Exiting..")

    config = configparser.ConfigParser()
    try:
        config.read(config_file)
    except configparser.DuplicateSectionError as e:
        logger.warn('Duplicate Section Error\n' + str(e))
        edit_txtfile()
        logger.warn("config check..")
        read_config_file()
    except configparser.DuplicateOptionError as e:
        logger.warn('Duplicate Setup found in config, '
                    'Please locate the error in notepad \n' + str(e))
        edit_txtfile()
        logger.warn("Rerunning config check..")
        read_config_file()

    return config


def postData(msgs):
    """
    Pub multible messages in same session
    :param msgs: dict
        {
            'topic':   f'Scanner/config/{project}/name',
            'payload': config[project]['name'],
            'retain':  True
        },
    
    """
    mqtt.publish.multiple(msgs, hostname=hostname, port=port)


class fetch_config:
    """ Create's tuple object from given section "project" """

    def __init__(self, project):
        self.isDev = os.environ.get('SCANNER_DEVMODE', False)
        self.project = project
        self.name = ''
        self.planarray = ''
        self.site = ''
        self.skip = ''
        if self.isDev:
            self.mqttConfig()
        else:
            self.fileConfig()

    def fetchData(self, var):
        data = mqtt.subscribe.simple(
            f'Scanner/config/{self.project}/{var}',
            hostname=hostname, port=port, keepalive=1)
        return str(data.payload)

        # sub.callback(
        #     self.on_message_set,
        #     f'Scanner/config/{self.project}/{var}',
        #     hostname=hostname, port=port)

    # def on_message_set(self, client, userdata, message):
    #     print("%s %s" % (message.topic, message.payload))

    def mqttConfig(self):
        self.name = self.fetchData('name')
        self.planarray = self.fetchData('planarray')
        self.site = self.fetchData('site')
        self.skip = self.fetchData('skip')
        return self

    def fileConfig(self):
        config = configparser.ConfigParser()
        config.read(projectstore)
        self.name = config[self.project]['name']
        self.planarray = config[self.project]['planarray']
        self.site = config[self.project]['site']
        self.skip = config[self.project]['skip']
        return self


class pubFullConfig:
    def __init__(self):
        projects = read_config_file()
        config = configparser.ConfigParser()
        config.read(projectstore)
        for project in projects.sections():
            postData([
                {
                    'topic':   f'Scanner/config/{project}/name',
                    'payload': config[project]['name'],
                    'retain':  True
                    },
                {
                    'topic':   f'Scanner/config/{project}/planarray',
                    'payload': config[project]['planarray'],
                    'retain':  True
                    },
                {
                    'topic':   f'Scanner/config/{project}/site',
                    'payload': config[project]['site'],
                    'retain':  True
                    },
                {
                    'topic':   f'Scanner/config/{project}/skip',
                    'payload': config[project]['skip'],
                    'retain':  True
                    }
                ])
