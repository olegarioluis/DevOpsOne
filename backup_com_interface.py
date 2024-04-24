# Bibliotecas importadas
import shutil
import os
import datetime
import PySimpleGUI as sg


def fazer_backup(origem, destino):
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
                f'O Diretório de origem "{origem}" não existe.')

        # Verifica se o diretório de destino existe
        if not os.path.exists(destino):
            raise FileExistsError(f'O Diretório de destino "{destino}" não existe.')
            

        # Adiciona a data atual ao nome do arquivo de backup
        data_atual = datetime.datetime.now().strftime('%Y-%m-%d')
        nome_backup = f'backup_{data_atual}.tar.gz'

        # Cria o arquivo de backup no diretório de destino
        caminho_backup = os.path.join(destino, nome_backup)

        # Faz a cópia dos arquivos e pastas
        shutil.make_archive(caminho_backup, 'gztar', origem)

        print(f'Backup realizado com sucesso em: {caminho_backup}')
        return True
    except Exception as e:
        print(f'Erro ao fazer backup: {str(e)}')
        return False


sg.theme('LightBrown')
# Layout da interface
layout = [
    [sg.Text('Origem')],
    [sg.FolderBrowse(), sg.Input(key='-INP-', size=(25, 1))],
    [sg.Text('Destino')],
    [sg.FolderBrowse(), sg.Input(key='-INP1-', size=(25, 1))],
    [sg.Button('Backup')]   

]

window = sg.Window('Backup', layout, element_justification='c')

# Loop para menter a interface aberta
while True:
    evento, valores = window.read()

    if evento == sg.WIN_CLOSED:
        break
    # Ação ao aperta o Butão de backup
    if evento == 'Backup':

        ori = valores['-INP-']
        des = valores['-INP1-']

        if __name__ == "__main__":

            origem = f'{ori}'
            destino = f'{des}'

            # Feedback visual
            if fazer_backup(origem, destino):
                sg.popup('Backup realizado com Sucesso!', no_titlebar=True, button_justification='c')
            else:
                sg.popup(
                    'Erro ao fazer backup. Verifique os diretórios informados', no_titlebar=True, button_justification='c')

window.close()
