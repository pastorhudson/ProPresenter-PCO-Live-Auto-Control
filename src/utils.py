import configparser
import os
from pypco import PCO
import logging
import colorlog
from datetime import datetime


def setup_logger(logger_name):
    # Create a logger
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)

    # Create a color formatter for the console
    color_formatter = colorlog.ColoredFormatter(
        "%(log_color)s%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt=None,
        reset=True,
        log_colors={
            'DEBUG': 'cyan',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'red,bg_white',
        },
        secondary_log_colors={},
        style='%'
    )

    # Create a console handler and set the color formatter
    ch = logging.StreamHandler()
    ch.setFormatter(color_formatter)

    # Create a file handler and set level to debug
    date = datetime.now().strftime('%Y-%m-%d')
    fh = logging.FileHandler(f'{date}.log')

    # Create a standard formatter for the file
    file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(file_formatter)

    # Add handlers to logger
    logger.addHandler(ch)
    logger.addHandler(fh)

    return logger


logger = setup_logger(__name__)


def get_pco():
    """
    Retrieve the PCO object.

    This method reads the configuration file 'config.ini' and creates a PCO object with the specified application ID and secret.

    :return: The PCO object.
    """
    check_config()

    try:
        config = configparser.ConfigParser()
        config.read('config.ini')
    except Exception:
        logger.error(Exception)

    return PCO(config.get('app', 'application_id'), config.get('app', 'secret'))


def check_config():
    # Check if the file does not exist
    if not os.path.isfile('config.ini'):

        # Create a configparser object
        config = configparser.ConfigParser()

        # Populate the configparser object with your data
        config['app'] = {
            ';Get your Planning Center application_id and secret at https://api.planningcenteronline.com/oauth/applications': '',
            'application_id': 'pco_app_id',
            'secret': 'pco_app_secret',
            ';Default is localhost 127.0.0.1 this is for running the program on the same machine as ProPresenter': '',
            'pro_presenter_ip': '127.0.0.1',
            'pro_presenter_port': '50001',
        }

        # Write the populated configparser object to config.ini file
        with open('config.ini', 'w') as configfile:
            config.write(configfile)
        raise Exception("ProPresenter configuration not found.\n"
                        "One has been created for you. Please edit the config.ini with your own settings.")
    # logger.info("Config File Found")
    return


def get_propresenter_config():
    """
    Returns the IP address and port number of the ProPresenter application
    configured in the 'config.ini' file.

    :return: The IP address and port number of the ProPresenter application.
    """
    check_config()

    config = configparser.ConfigParser()
    config.read('config.ini')

    return config.get('app', 'pro_presenter_ip'), config.get('app', 'pro_presenter_port')


if __name__ == '__main__':
    print(check_config())