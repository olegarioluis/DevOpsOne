# Bibliotecas usadas
import psutil
import time
import os


def monitoramento():

    try:
        # Esse Loop mantém a impressão das informações na tela e a sua atualização.
        while True:
            os.system('clear')
            # Coleta de Informações do Sistema
            uso_cpu = psutil.cpu_percent()
            inf_mem = psutil.virtual_memory().percent
            uso_rede_rec = psutil.net_io_counters().bytes_recv
            uso_rede_env = psutil.net_io_counters().bytes_sent
            uso_disk = psutil.disk_usage('/').percent

            # Formatação e impressão das Informações coletadas.
            print("========== Monitoramento do Sistema ==========")
            print(f'Uso de CPU: {uso_cpu:.2f}%')
            print(f'Uso de Memória: {inf_mem:.2f}%')
            print(
                f'Uso de Rede: Dados Enviados {uso_rede_env} bytes, Dados Recebidos {uso_rede_rec} bytes.')
            print(f'Uso do Disco: {uso_disk:.2f}%')
            print("===============================================")

            time.sleep(2)  # Aguarda 2 segundos antes de atualizar.

    except KeyboardInterrupt:
        print('Monitoramento encerrado!')


if __name__ == '__main__':
    monitoramento()
