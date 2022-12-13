import os.path
import sched
import time
import subprocess, shlex
from os import path
from datetime import datetime
from sendemail import send_email
from logs import check_disk, clear_logs_elastic, clear_logs_kibana 

scheduler = sched.scheduler(time.time, time.sleep)

# Função mãe
def main():
    # data e hora
    today = datetime.now()
    today = today.strftime('[%Y-%m-%d %H:%M:%S]')
    disk = check_disk()
    disk = disk.decode("utf-8")
    # verifica o espaço em disco 
    if disk >= '90%':
        # Chama a função para apagar os logs do kibana
        kibana = clear_logs_kibana()

        # Chama a função para apagar os logs do ElasticSearch
        elastic = clear_logs_elastic()

        # Mensagem de disco cheio
        print(today, "Limite atigindo! Used:", disk )
            
        # Verifica se os logs do ElasticSearch foram apagados
        if elastic[1].decode("utf-8") == '':
            print(today, "Logs do ElasticSearch foram apagados.")
        else:
            print(today, "Não foi possível apagar os logs do ElasticSearch!")
            print(elastic[1].decode("utf-8"))
            
        # Verificando se os logs do Kibana foram apagados
        if kibana[1].decode("utf-8") == '':
            print(today, "Logs do Kibana foram apagados.")
        else:
            print(today, "Não foi possível apagar os logs do Kibana")
            print(kibana[1].decode("utf-8"))
        
    # Mensagem avisando que o sistema está ativo
    else:
        print(today, "Espaço em disco aceitável. Used:",disk)
        try:
            send_email() 
            print(today, "Equipe MDR foi notificada!")
        except OSError:
            print(today, "Email de com dados do ElasticSearch não foi enviado!")
    # Temporizador     
    scheduler.enter(60, 1, main)
    scheduler.run()

