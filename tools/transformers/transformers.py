from logzero import logger
class Transformers:
    def __init__(self):
        pass


    @staticmethod
    def transform_document_list_to_dict(document_list):
        logger.debug("transformer")
        for document in document_list:
            logger.debug(document.first_name)