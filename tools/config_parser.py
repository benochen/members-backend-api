from logzero import logger, logfile
import os
import configparser
class config_parser:

    def __init__(self,config_file):
        if not os.path.exists(config_file):
            logger.error(f"The log file {config_file} does not exists")
            exit(1)
        logger.info(f"The config file {config_file} exists")
        self.config_file=config_file
        self.config_parser = configparser.ConfigParser()
        self.config_parser.read(config_file)

    def parse_config_api(self):
        logger.debug(f"The parsing of the API section start")
        return self.config_parser["HELLOASSO-API"]

    def parse_config_excel(self):
        logger.debug(f"The parsing of the excel section start")
        return self.config_parser["EXCEL"]

    def parse_config_mongo(self):
        logger.debug(f"The parsing of the mongo section start")
        return self.config_parser["MONGO"]


    def parse_config_json(self):
        logger.debug(f"The parsing of the json section start")
        return self.config_parser["JSON"]


    def parse_config_gdrive(self):
        logger.debug(f"The parsing of the gdrive section start")
        return self.config_parser["GDRIVE"]


