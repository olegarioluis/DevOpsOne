# Bibliotecas usadas
import shutil
from datetime import datetime
import os


def backup(origem, destino):
    """
    Faz backup de um diretório de origem para um diretório de destino.

    Parameters:
        origem (str): O diretório de origem que será copiado para o backup.
        destino (str): O diretório de destino onde o backup será armazenado.

    Returns:
        None
    """

    try:

        # Verifica se o diretório de origem existe
        if not os.path.exists(origem):
            raise FileNotFoundError(
                f'O diretório de Origem "{origem}" não existe.')

        # Verifica se o diretório de destino existe
        if not os.path.exists(destino):
            raise FileNotFoundError(
                f'O diretório de Destino "{destino}" não existe.')

        # Adiciona a data e hora atual ao nome do arquivo de backup
        data_hora = datetime.now().strftime(r'%Y-%m-%d')
        nome_arquivo = f'backup_{data_hora}.tar.gz'

        # Cria o arquivo de Backup no diretório de destino
        rota_backup = os.path.join(destino, nome_arquivo)

        # Faz a cópia dos arquivos e pastas
        shutil.make_archive(rota_backup, 'gztar', origem)

        print(f'Backup realizado com sucesso: {rota_backup}')

    except Exception as e:
        print(f'Erro ao fazer backup: {str(e)}')


if __name__ == '__main__':

    # Diretório de origem e destino para backup
    origem = f'/caminho/para/diretorio/origem'
    destino = f'/caminho/para/diretorio/destino'

    backup(origem, destino)
