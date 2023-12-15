from logzero import logger, logfile
import os
import configparser
class config_parser:

    def __init__(self,config_file):
        if not os.path.exists(config_file):
            exit(1)
        self.config_file=config_file
        self.config_parser = configparser.ConfigParser()
        self.config_parser.read(config_file)

    def parse_config_api(self):
        return self.config_parser["HELLOASSO-API"]

    def parse_config_excel(self):
        return self.config_parser["EXCEL"]

    def parse_config_mongo(self):
        return self.config_parser["MONGO"]


    def parse_config_json(self):
        return self.config_parser["JSON"]


    def parse_config_gdrive(self):
        return self.config_parser["GDRIVE"]


