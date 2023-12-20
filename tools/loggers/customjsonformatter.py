import traceback

from pythonjsonlogger import jsonlogger


class CustomJsonFormatter(jsonlogger.JsonFormatter):

    def add_fields(self, log_record, record, message_dict):
        try:
            super(CustomJsonFormatter, self).add_fields(log_record, record, message_dict)

            log_record = CustomJsonFormatter.init_log_record_new_attribute(log_record)

            if log_record.get("context"):
                context = log_record.get("context")
                if context.get("request"):
                    self.fill_request_info(log_record)
                if context.get("uuid"):
                    log_record["uuid"]=context.get("uuid")
                else:
                    log_record["uid"]="N/A"
                if context.get("event_sec_type"):
                    log_record["event_sec_type"]=context.get("event_sec_type")
                else:
                    log_record["event_sec_type"]="N/A"
                if context.get("client_ip"):
                    log_record["client_ip"]=context.get("client_ip")
                else:
                    log_record["client_ip"]="N/A"
                log_record.pop("context")
        except Exception as e:
            traceback.print_exc()

    def fill_request_info(self, log_record):
        if log_record.get("context").get("request"):
            request = log_record.get("context").get("request")
            request_dict = self.parse_request(request)
            for k, v in request_dict.items():
                log_record[k]=v
        if log_record.get("context").get("user"):
            user=log_record.get("context").get("user")
            user_dict= self.parse_user(user)
            for k,v in user_dict.items():
                log_record[k]=v

        return log_record

    def parse_request(self, request):
        request_dict = dict()
        if request.url:
            request_dict["call_url"]=request.url
        return request_dict

    def parse_user(self,user_info):
        user_info_dict=dict()
        if user_info["email"]:
            user_info_dict["user"]=user_info["email"]
        return user_info_dict

    @staticmethod
    def init_log_record_new_attribute(log_record):
        log_record["client_ip"] = "N/A"
        log_record["call_url"] = "N/A"
        log_record["user"] = "GUEST"
        return log_record
