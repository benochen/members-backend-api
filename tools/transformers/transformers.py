from logzero import logger
class Transformers:
    def __init__(self):
        pass


    @staticmethod
    def transform_document_list_to_dict(document_list):
        logger.debug("transformer")
        members=list()
        for document in document_list:
            member=dict()
            logger.debug(document.first_name)
            member["last_name"]=document.last_name
            member["first_name"]=document.first_name
            logger.debug(f"{document.first_name} transformed")

            member["phone"]=document.phone
            logger.debug(f"{document.phone} transformed")

            member["mail"]=document.email
            logger.debug(f"{document.email} transformed")

            member["adresse"]=document.address
            logger.debug(f"{document.address} transformed")

            member["ville"]=document.ville
            logger.debug(f"{document.ville} transformed")

            member["zip"]=document.zip_code
            logger.debug(f"{document.zip_code} transformed")

            member["authorized_rs"]=document.social_network_authorized
            logger.debug(f"{document.social_network_authorized} transformed")

            member["authorized_web"]=document.ecreadys_site_web_authorized
            logger.debug(f"{document.ecreadys_site_web_authorized} transformed")

            member["authorized_press"]=document.press_media_authorized
            logger.debug(f"{document.press_media_authorized} transformed")

            member["cotisation"]=document.payment
            logger.debug(f"{document.payment} transformed")

            logger.debug("document will be append")
            members.append(member)
        return members