import os

os.system("python scripts/data_ingestion.py")
os.system("python scripts/data_cleaning.py")
os.system("python scripts/data_transform.py")

print("Pipeline completed")