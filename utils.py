import configparser

from pypco import PCO


def get_pco():
    """
    Retrieve the PCO object.

    This method reads the configuration file 'config.ini' and creates a PCO object with the specified application ID and secret.

    :return: The PCO object.
    """
    config = configparser.ConfigParser()
    config.read('config.ini')

    return PCO(config.get('app', 'application_id'), config.get('app', 'secret'))


def get_propresenter_config():
    """
    Returns the IP address and port number of the ProPresenter application
    configured in the 'config.ini' file.

    :return: The IP address and port number of the ProPresenter application.
    """
    config = configparser.ConfigParser()
    config.read('config.ini')

    return config.get('app', 'pro_presenter_ip'), config.get('app', 'pro_presenter_port')
