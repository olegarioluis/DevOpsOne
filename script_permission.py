# Biblioteca usada
import os


def obter_permissao_arquivo(caminho_arquivo):
    try:
        # Tenta obter informações sobre o arquivo especificado
        info_arquivo = os.stat(caminho_arquivo)

        # Obtém as permissões do arquivo
        permissao = info_arquivo.st_mode

        # Converte as permissões para representação octal
        permissao_octal = oct(permissao & 0o777)

        # Exibe as permissões do arquivo
        print(f'Permissões do arquivo {caminho_arquivo}: {permissao_octal}')
    except FileNotFoundError as e:
        # Captura e trata o erro se o arquivo não for encontrado
        print(f"Erro: {e}")
    except Exception as e:
        # Captura e trata quaisquer outros erros inesperados
        print(f"Ocorreu um erro inesperado: {e}")


def alterar_permissao_arquivo(caminho_arquivo, nova_permissao):
    try:
        # Altera as permissões do arquivo para a nova permissão especificada
        os.chmod(caminho_arquivo, nova_permissao)

        # Exibe as novas permissões do arquivo após a alteração
        print(
            f'A novas permissões do arquivo {caminho_arquivo} são: {oct(nova_permissao)}')
    except FileNotFoundError as e:
        # Captura e trata o erro se o arquivo não for encontrado
        print(f"Erro: {e}")
    except Exception as e:
        # Captura e trata quaisquer outros erros inesperados
        print(f"Ocorreu um erro inesperado: {e}")


# Exemplo de uso:
arquivo = f'/caminho/para/arquivo.txt'

# Obtendo e exibindo as permissões atuais do arquivo
obter_permissao_arquivo(arquivo)

# Alterando as permissões do arquivo
nova_permissao = 0o777  # Altere esses 3 número de acordo com a base octal
alterar_permissao_arquivo(arquivo, nova_permissao)
