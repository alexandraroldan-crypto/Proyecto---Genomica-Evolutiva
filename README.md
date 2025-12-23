# Proyecto---Genomica-Evolutiva

## Pipeline bioinformático para la selección de regiones de interés y preparación de referencias para Nanopore Adaptive Sampling
Se realizará un análisis evolutivo de géneros de orquídeas centrado en regiones codificantes (CDS) del genoma cloroplastidial. El objetivo principal será evaluar la capacidad de distintos CDS para servir como zonas de amplicón (barcoding): medir variabilidad entre especies, identificar zonas conservadas para diseño de cebadores y proponer loci candidatos para estudios de identificación y filogenia.

---

## 🎯 Objetivos

### Objetivo general
Desarrollar un pipeline bioinformático para la extracción, evaluación y organización de secuencias de códigos de barras cloroplásticos estándar (rbcL, matK y trnH-psbA) a partir de genomas cloroplásticos completos públicos, con el fin de generar bases de referencia en formato FASTA de alta calidad, listas para su almacenamiento en NAS y uso en identificación molecular de muestras vegetales secuenciadas.

---

## 🧩 Datos y muestras

- **Número de géneros esperados**: ~ 5  
- **Número de especies por género**: variable (1–5, según disponibilidad en NCBI) 
- **Tipo de datos**: Genomas cloroplastidiales completos (FASTA)  
- **Fuente**: NCBI GenBank  

---

## ⚙️ Lenguajes y herramientas utilizados en el proyecto
### Lenguaje
- Bash
  Usado para automatización de flujos de trabajo, bucles de procesamiento masivo, conversión de formatos y ejecución encadenada de herramientas bioinformáticas.
- Python 3
  Lenguaje principal para scripts personalizados. Bibliotecas utilizadas:
   - Biopython (módulos SeqIO, Entrez, AlignIO) — descarga desde NCBI, parsing de GenBank/FASTA, extracción precisa de regiones genéticas.
   - numpy: cálculos de distancias genéticas y diversidad nucleotídica (π).

### Herramienta
- NCBI / GenBank — descarga de secuencias de referencia (matK, rbcL, ITS, trnH-psbA)
- SeqKit — filtrado, extracción y limpieza de secuencias (longitud, Ns, orientación)
- MAFFT — alineamiento por locus (matK, rbcL, ITS, etc.)
- IQ-TREE — inferencia filogenética y evaluación de soporte
- AMAS — concatenación de loci por muestra
- Python / Biopython — automatización de descargas, PCR in silico y análisis comparativos

---

## Scripts incluidos

| Script                             | Función                                                                                      |
|-----------------------------------|----------------------------------------------------------------------------------------------|
| descarga.py                       | Obtener los genomas clorplastidiales de los generos de interes                               |
| extraer_rois.py                   | Extraer los ROI's de interes de manera simultanea                                            |
| diversidad.py                     | Cuantificar la variabilidad genética intra e inter-taxon para cada marcador                  |
| rois_to_fasta.sh                  | Unificación de comandos en un archivo bash                                                   |


