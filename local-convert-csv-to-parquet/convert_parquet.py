import pandas as pd
import glob
from pathlib import Path
import os
import shutil

def transform_csv_to_parquet(file_path, output_path, low_memory = True):
    df = pd.read_csv(file_path, delimiter=';', header=[0],encoding="Latin-1", low_memory=low_memory)
    filename = Path(file_path).stem
    df.to_parquet(output_path + filename + ".parquet")

try:
    print("Removendo diretorio output...")
    shutil.rmtree('./output')
except FileNotFoundError as e:
    print("Diretorio output nao existe")
    
print("Criando diretorio output...")
os.mkdir("./output")
os.mkdir("./output/ENEM")
os.mkdir("./output/CENSO")
print("Diretorio output criado")


print("Iniciando conversao dos arquivos de microdados ENEM...")
files_enem = glob.glob("./ENEM/extraidos/MICRODADOS_ENEM_*.csv")
for file in files_enem:
    transform_csv_to_parquet(file, "./output/ENEM/")
    
    
print("Iniciando conversao dos arquivos de microdados do Censo Escolar...")
files_censo = glob.glob("./CENSO/extraidos/microdados_ed_basica_*.csv")
for file in files_censo:
    transform_csv_to_parquet(file, "./output/CENSO/", False)