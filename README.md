# 1º Projeto Prático - DevOps

## Automação de Rotinas em Ambiente Linux com Python.
<h3>1. backup_com_interface.</h3>
<h5>Descrição</h5>
O script permite que o usuário faça backup de um diretório de origem para um diretório de destino especificado. O backup é criado como um arquivo '.tar.gz' (gzip compressed tar file) com a data atual como parte do nome do arquivo, facilitando a organização e identificação dos backups.

<h5>Como usar</h5>

1- Iniciar o Script:
* Abra um terminal ou linha de comando e navegue até o diretório onde o script está salvo. Execute o script usando:

      'python3 backup_com_interface.py'

2- Interface Gráfica:
* A interface gráfica será exibida.
* Utilize os botões "Browse" para selecionar os diretórios de origem e destino.
* Após selecionar os diretórios, clique no botão "Backup".

3- Feedback:
* Após clicar em "Backup", o script processará o pedido e exibirá uma janela popup indicando sucesso ou falha no backup.

<h5>Dependências</h5>

* Para executar o script você precisará da biblioteca 'PySimpleGUI'.

* Você pode instalar as bibliotecas necessárias usando pip: 'pip3 install PySimpleGUI'

<h3>2. script_backup</h3>
<h5>Descrição</h5>
Este script realiza o backup de um diretório específico, compactando-o em um arquivo `.tar.gz` e armazenando-o em um diretório de destino.

<h5>Uso</h5>

* Para usar este script, você precisa especificar o diretório de origem e o diretório de destino. O diretório de origem é o local dos arquivos que você deseja fazer backup, e o diretório de destino é onde o backup será armazenado.

<h5>Iniciar o script</h5>

* Abra o script 'script_backup.py'.
* Modifique as variáveis 'origem' e 'destino' no bloco 'if __name__ == '__main__':' no final do arquivo para refletir os caminhos desejados no seu sistema. Por exemplo:

      origem = '/caminho/para/diretorio/origem'
      destino = '/caminho/para/diretorio/destino'

* Abra um terminal ou linha de comando e navegue até o diretório onde o script está salvo. Execute o script usando:

      'python3 script_backup.py'

<h3>3. script_monitoring</h3>
<h5>Descrição</h5>

Este script monitora continuamente vários aspectos do sistema, como uso de CPU, memória, rede e disco em uma máquina Linux. Ele exibe as informações em tempo real e atualiza esses dados a cada 2 segundos.

<h5>Funcionalidades</h5>

O script oferece as seguintes funcionalidades:

* Monitoramento de CPU: Exibe o percentual de uso atual da CPU.
* Monitoramento de Memória: Mostra o percentual de uso da memória RAM.
* Monitoramento de Rede: Relata a quantidade de dados enviados e recebidos pela rede.
* Monitoramento de Disco: Exibe o uso atual do disco no diretório raiz ("/").

<h5>Como Usar</h5>

* Abra um terminal e execute o script com o seguinte comando:

      'python3 script_monitoring'

* Para interromper o monitoramento, pressione CTRL+C no terminal.

<h5>Plataforma</h5>

* Este script foi projetado para funcionar em sistemas Linux, pois usa o comando 'clear' para limpar a tela entre as atualizações. Para usar em Windows, substitua 'os.system('clear')' por 'os.system('cls')' no script.

<h5>Dependências</h5>

* Este script depende da biblioteca psutil, que é usada para coletar informações do sistema. Se você não tiver essa biblioteca instalada, pode instalá-la usando o pip: 'pip3 install psutil'

<h3>4. script_permission</h3>

<h5>Funcionalidades</h5>

1- obter_permissao_arquivo(caminho_arquivo):
* Obtém as permissões atuais de um arquivo especificado.
* Exibe as permissões em formato octal.
2- alterar_permissao_arquivo(caminho_arquivo, nova_permissao):
* Altera as permissões de um arquivo para o valor especificado.
* Exibe as novas permissões do arquivo em formato octal após a alteração.

<h5>Como Usar</h5>

1- Definir o caminho do arquivo:
* No final do script, defina o caminho para o arquivo que você deseja gerenciar. Exemplo:

      arquivo = '/caminho/para/arquivo.txt'

2- Obter permissões do arquivo:
* Para obter as permissões atuais do arquivo, chame a função 'obter_permissao_arquivo' passando o caminho do arquivo como argumento.

3- Alterar permissões do arquivo:
Para alterar as permissões do arquivo, primeiro defina a nova permissão em formato octal e então chame a função 'alterar_permissao_arquivo'.

    nova_permissao = 0o777  # Permissão total
    alterar_permissao_arquivo(arquivo, nova_permissao)
    
4- Abra um terminal ou linha de comando e navegue até o diretório onde o script está salvo. Execute o script usando:

     'python3 script_permission.py'

    
