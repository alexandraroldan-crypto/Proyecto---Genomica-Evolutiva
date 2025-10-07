# Proyecto---Genomica-Evolutiva

Las orquídeas constituyen una de las familias más diversas y abundantes dentro de las angiospermas. En Perú, su presencia es especialmente significativa, con una alta concentración de especies en la región de San Martín, considerada uno de los principales centros de diversidad para este grupo vegetal.
Este proyecto tiene como objetivo realizar un análisis evolutivo de los géneros de orquídeas presentes en San Martín, utilizando datos genómicos disponibles en el repositorio NCBI. El enfoque estará centrado en el estudio del genoma cloroplastidial, dada su utilidad en reconstrucciones filogenéticas y en la comprensión de relaciones evolutivas entre especies.

Proyección del trabajo

• 	Recolección de datos: Identificación de géneros reportados en San Martín y descarga de secuencias cloroplastidiales desde NCBI.

• 	Análisis filogenético: Alineamiento de secuencias, construcción de árboles evolutivos y evaluación de divergencias genéticas.


## 🎯 Objetivos

### Objetivo general
Evaluar las relaciones evolutivas entre géneros de orquídeas presentes en San Martín mediante análisis filogenómicos basados en genomas cloroplastidiales.

### Objetivos específicos
1. Identificar los géneros de orquídeas reportados para la región de San Martín.  
2. Descargar genomas cloroplastidiales disponibles en NCBI correspondientes a dichos géneros.  
3. Realizar alineamientos múltiples y construir árboles filogenéticos.  
4. Evaluar la divergencia genética y las agrupaciones evolutivas resultantes.

---

## 🧩 Datos y muestras

- **Número de géneros esperados**: ~15–20  
- **Número de especies por género**: variable (1–5, según disponibilidad en NCBI)  
- **Tipo de datos**: Genomas cloroplastidiales completos o parciales (FASTA)  
- **Fuente**: NCBI GenBank  
- **Región de estudio**: Departamento de San Martín, Perú  

---

## ⚙️ Metodología y pipeline

### Etapas principales:
1. **Descarga de datos**
   - Uso de `Entrez` (Biopython) o `ncbi-datasets` para obtener secuencias cloroplastidiales.
   - Script: `scripts/download_ncbi_chloroplast.py`.

2. **Procesamiento y alineamiento**
   - Alineamiento con **MAFFT** (`scripts/align_sequences.sh`).
   - Limpieza y concatenación con **AMAS** (`scripts/concat_alignment.py`).

3. **Construcción de filogenias**
   - Árbol filogenético con **IQ-TREE** (`scripts/build_tree_iqtree.sh`).
   - Bootstrap automático (ultrafast) y selección de modelo.

4. **Visualización y análisis**
   - Visualización con **ETE3**, **iTOL** o **FigTree**.
   - Análisis exploratorio en Jupyter Notebooks (`notebook/visualizacion_arboles.ipynb`).

---

## 💻 Tecnologías y herramientas

| Tipo | Herramienta / Lenguaje |
|------|------------------------|
| Descarga y manejo de datos | Python (Biopython, Pandas) |
| Alineamientos | MAFFT |
| Filogenia | IQ-TREE |
| Concatenación | AMAS |
| Automatización del flujo | Bash / Nextflow |
| Visualización | Python (ETE3, Matplotlib) / iTOL |
| Control de versiones | Git + GitHub |
