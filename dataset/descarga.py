import sys
import os # Import the os module

from Bio import SeqIO
from Bio import Entrez, SeqIO
Entrez.email = "alerol194@example.com"  # Reemplaza con tu email (requerido por NCBI)

generos = ["Dracula", "Odontoglossum"]  # Añade más géneros si necesitas
retmax_por_genero = 20  # Máximo por género (cubrirá 5 y 3 fácilmente)

# Create the 'descarga' directory if it doesn't exist
os.makedirs("descarga", exist_ok=True)
# Diagnostic check: ensure the directory exists after creation attempt
if not os.path.exists("descarga"):
    print("Error: The 'descarga' directory could not be created or is not accessible. Check permissions.")
    # Depending on severity, you might want to exit here or raise an exception

for genero in generos:
    handle = Entrez.esearch(db="nuccore", term=f"{genero}[ORGN] AND chloroplast[ALL] AND complete genome[TITL]", retmax=retmax_por_genero)
    record = Entrez.read(handle) # Changed eread to read
    ids = record["IdList"]
    print(f"Encontrados {len(ids)} plastomas para {genero}")

    for id in ids:
        fetch_handle = Entrez.efetch(db="nuccore", id=id, rettype="gbwithparts", retmode="text")
        with open(f"descarga/{genero}_{id}.gb", "w") as out_file:
            out_file.write(fetch_handle.read())
    handle.close()
