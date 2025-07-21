import gdown
import zipfile
import os

# Google Drive File-ID
file_id = "1l4q7BNx5p01onEJt4t8HXcLEr8lJJY93"
# Ziel-Dateiname
output_file = "klonk_daten.zip"

# URL zusammensetzen
url = f"https://drive.google.com/uc?id={file_id}"

# Download starten
print(f"Lade Datei von Google Drive herunter...\nURL: {url}")
gdown.download(url, output_file, quiet=False)

# Wenn ZIP-Datei, dann entpacken
if output_file.endswith(".zip"):
    extract_dir = "klonk_daten"
    print(f"Entpacke {output_file} nach '{extract_dir}'...")
    with zipfile.ZipFile(output_file, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)
    print("Entpackt.")
