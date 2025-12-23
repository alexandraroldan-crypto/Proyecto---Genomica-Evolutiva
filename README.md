# Proyecto---Genomica-Evolutiva

## Pipeline bioinformático para la extracción y organización de secuencias degeneración de bases de referencia FASTA de códigos de barras cloroplásticos en plantas
Se realizará un análisis evolutivo de géneros de orquídeas centrado en regiones codificantes (CDS) del genoma cloroplastidial. El objetivo principal será evaluar la capacidad de distintos CDS para servir como zonas de amplicón (barcoding): medir variabilidad entre especies, identificar zonas conservadas para diseño de cebadores y proponer loci candidatos para estudios de identificación y filogenia.

### Lenguajes y herramientas utilizados en el proyecto
- Bash
  Usado para automatización de flujos de trabajo, bucles de procesamiento masivo, conversión de formatos y ejecución encadenada de herramientas bioinformáticas.
- Python 3
  Lenguaje principal para scripts personalizados. Bibliotecas utilizadas:
   - Biopython (módulos SeqIO, Entrez, AlignIO) — descarga desde NCBI, parsing de GenBank/FASTA, extracción precisa de regiones genéticas.

   - numpy: cálculos de distancias genéticas y diversidad nucleotídica (π).


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

### Etapas principales:
1. **Descarga de datos**
   - Descarga de genomas cloroplastidiales
   - Obtener genomas completos desde NCBI (Entrez / datasets).
2. **Extracción de CDS**
   - Extraer todos los coding sequences (CDS) de cada genoma y organizarlos por locus en FASTA individuales.
3. **Control de calidad**
   - Filtrar secuencias por longitud, ambigüedades y duplicados por especie.
4. **Alineamiento por locus**
   - Alinear cada archivo de CDS con MAFFT.
5. **Limpieza del alineamiento**
   - Recortar extremos con gaps, revisar marcos de lectura y uniformidad.
6. **Cálculo de variabilidad**
   - Obtener métricas por locus: sitios variables, π, p-distance, % identidad, cobertura.
7. **Filogenias por CDS**
   - Construir árboles con IQ-TREE para evaluar poder resolutivo por locus.
8. **Identificación de regiones candidatas para amplicones**
   - Analizar ventanas deslizantes para localizar zonas conservadas (cebadores) y regiones internas variables (discriminación).



---
