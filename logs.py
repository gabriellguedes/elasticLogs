import subprocess
import os.path
from os import path
from datetime import datetime

# Objeto para limpar os logs
today = datetime.utcnow()

#Função para verificar o espaço em disco
def check_disk():
    disk1 = subprocess.Popen("df -h /dev/sda1 |tail -n1", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    disk = disk1.communicate()
    lista=[]
    for fields in disk[0].split():
        lista.append(fields)
    resultado = lista[4]
    return resultado
        
# Verificando e apaga logs do ElasticSearch	
def clear_logs_elastic():
    directory = path.exists("/var/log/elasticsearch")
    if directory != True:
        created = subprocess.Popen("mkdir /var/log/elasticsearch", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        if created.returncode == 0:
            return True
        else:
            responseError = created.communicate()
            return responseError
    else:
        clear = subprocess.Popen("rm -r /var/log/elasticsearch/*",stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        if clear.returncode == 0:
            return True
        else:
            responseError = clear.communicate()
            return responseError
        
# Verifica e apaga Logs do Kibana             
def clear_logs_kibana():
    directory = path.exists("/var/log/kibana")
    if directory != True:
        created = subprocess.Popen("mkdir /var/log/kibana", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        if created.returncode == 0:
            return True
        else:
            responseError = created.communicate()
            return responseError
    else:
        clear = subprocess.Popen("rm -r /var/log/kibana/*",stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        if clear.returncode == 0:
            print(clear.returncode)
            return True
        else:
            responseError = clear.communicate()
            return responseError
