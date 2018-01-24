import configparser

class Config:
    def __init__(self, config_file):
        # self.config_file = config_file
        config = configparser.ConfigParser()

        config.read(config_file)

        self.token = config.get('Credentials', 'Token', fallback='')  