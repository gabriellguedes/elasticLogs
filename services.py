import subprocess
import os.path
from os import path
from datetime import datetime

class verificar_services():
    # Data de hoje
    today = datetime.now()
   
   # Verificar serviços do ElasticSearch
    def elastic_service():
        try:
            elastic_status = subprocess.Popen("systemctl status elasticsearch", shell=True)
        except OSError:
            elastic_status.communicate()
            responseError = elastic_status[1].decode("utf-8")
            return responseError
   
   # Verificar serviços do Kibana
    def kibana_service():
        try:
            kibana_status = subprocess.Popen("systemctl status kibana", shell=True)
        except OSError:
            kibana_status.communicate()
            responseError = kibana[1].decode("utf-8")
            return responseError
