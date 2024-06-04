import pandas as pd
import os
from pathlib import Path
BASE_DIR = str(Path(os.path.dirname(__file__)).parent)
from meuPacote.bookToScrape import getPrice
from dotenv import load_dotenv #instalar o pacote python-dotenv
load_dotenv()# Para ler as variaveis do arquivo .env
from meuPacote.email import enviar_email


def main():    
    file = BASE_DIR + '/data/livros_classics.xlsx'

    print(f'Email enviado com sucesso!')

if __name__ == '__main__':
    main()