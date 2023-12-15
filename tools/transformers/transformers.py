from logzero import logger
class Transformers:
    def __init__(self):
        pass


    @staticmethod
    def transform_document_list_to_dict(document_list):
        members=list()
        for document in document_list:
            member=dict()
            member["last_name"]=document.last_name
            member["first_name"]=document.first_name

            member["phone"]=document.phone

            member["mail"]=document.email

            member["adresse"]=document.address

            member["ville"]=document.ville

            member["zip"]=document.zip_code

            member["authorized_rs"]=document.social_network_authorized

            member["authorized_web"]=document.ecreadys_site_web_authorized

            member["authorized_press"]=document.press_media_authorized

            member["cotisation"]=document.payment

            members.append(member)
        return members