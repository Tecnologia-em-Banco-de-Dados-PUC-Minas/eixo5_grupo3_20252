import os
import boto3
import zipfile
from io import BytesIO
from pyspark.sql import SparkSession

# Inicializa sessão Spark
spark = SparkSession.builder.appName("transform_raw_to_processed").getOrCreate()

# Configurações
BUCKET = "projeto-puc-fraud-prevention"
RAW_PREFIX = "raw/"
PROCESSED_PREFIX = "processed/"
ZIP_FILENAME = "credit_risk_dataset.csv.zip"

# Baixar o arquivo zip do S3
s3 = boto3.client("s3")
zip_obj = s3.get_object(Bucket=BUCKET, Key=f"{RAW_PREFIX}{ZIP_FILENAME}")
zip_content = BytesIO(zip_obj['Body'].read())
print(f"Arquivo {ZIP_FILENAME} baixado do S3 com sucesso.")

# Descompactar no /tmp/
extract_path = "/tmp/dataset"
os.makedirs(extract_path, exist_ok=True)
with zipfile.ZipFile(zip_content) as zip_ref:
    zip_ref.extractall(extract_path)
print(f"Arquivos descompactados em {extract_path}")

# Ler todos os CSVs extraídos com Spark
df_raw = spark.read.csv(f"file://{extract_path}/*.csv", header=True, inferSchema=True)
print("Esquema detectado:")
df_raw.printSchema()

# Salvar em Parquet no S3 na pasta processed
output_path = f"s3://{BUCKET}/{PROCESSED_PREFIX}"
df_raw.write.mode("overwrite").parquet(output_path)
print(f"Dados transformados e salvos em {output_path}")
