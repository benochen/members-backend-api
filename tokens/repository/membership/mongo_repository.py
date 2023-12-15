from logzero import logger
from models.mongodb.membersDocument import MembersDocument
from tools.transformers.transformers import Transformers
from tokens.repository.mongodb.MembersRepository import MembersRepository
class mongo_repository:

    def __init__(self,config_mongo,form_slug,context=None):
        self.members=list()
        self.config_mongo = config_mongo
        self.form_slug=form_slug
        self.db=config_mongo["mongo_db"]
        self.host=config_mongo["mongo_host"]
        self.port=config_mongo["mongo_port"]
        self.context=context
    def find_all_mockup(self):
        member=dict()
        logger.debug("finall_mockup")

        member["first_name"]="Benoît"
        member["last_name"]="Chenal"
        member["phone"]="0614236680"
        member["mail"]="benoit.chenal.57@gmail.com"
        member["adresse"]="1, rue de la carrière,Saint-Avold"
        member["zip"]="57500"
        member["authorized_rs"]="Oui"
        member["authorized_web"]="Oui"
        member["authorized_press"]="Oui"
        member["cotisation"]=30
        self.members.append(member)

        member=dict()
        member["first_name"]="Bastien"
        member["last_name"]="Chenal"
        member["phone"]="0614236680"
        member["mail"]="bastienchenal@gmail.com"
        member["adresse"]="1, rue de la carrière,Saint-Avold"
        member["zip"]="57470"
        member["authorized_rs"]="Oui"
        member["authorized_web"]="Oui"
        member["authorized_press"]="Oui"
        member["cotisation"]=30
        self.members.append(member)
        return self.members

    def find_all(self):
        members_repository=MembersRepository(host=self.host,port=self.port,db=self.db,context=self.context)
        res=members_repository.findAll()
        self.members=Transformers.transform_document_list_to_dict(res)
        member=dict()


        return self.members