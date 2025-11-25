# Proyecto---Genomica-Evolutiva
## Evaluación de regiones codificantes (CDS) del genoma cloroplastidial como loci de barcoding para orquídeas del departamento de San Martín, Perú

Se realizará un análisis evolutivo de géneros de orquídeas centrado en regiones codificantes (CDS) del genoma cloroplastidial. El objetivo principal será evaluar la capacidad de distintos CDS para servir como zonas de amplicón (barcoding): medir variabilidad entre especies, identificar zonas conservadas para diseño de cebadores y proponer loci candidatos para estudios de identificación y filogenia.

Proyección del trabajo

• 	Compilar lista de géneros de orquídeas reportados en San Martín y obtener secuencias cloroplastidiales disponibles en NCBI para esos géneros.
• 	Extraer todos los CDS presentes en los genomas cloroplastidiales descargados y organizar por locus (un archivo FASTA por CDS que contenga todas las muestras disponibles).
• 	Realizar alineamientos múltiples locus-por-locus (MAFFT) y análisis de variabilidad (sítios variables, π, distancia media, %identidad).
• 	Identificar regiones conservadas flanqueantes a zonas variables y sugerir posiciones/longitudes de amplicones útiles para diseño de cebadores.
• 	Evaluar potencia de discriminación (resolución taxonómica) de cada CDS mediante árboles (IQ-TREE) y métricas de monofilia / soporte.
• 	Proveer recomendaciones de loci candidatos para barcoding en orquídeas (priorizando balance entre variabilidad y longitud/amplificabilidad).


## 🎯 Objetivos

### Objetivo general
Se realizará un análisis evolutivo de géneros de orquídeas presentes en el departamento de San Martín (Perú) centrado en regiones codificantes (CDS) del genoma cloroplastidial. El objetivo principal será evaluar la capacidad de distintos CDS para servir como zonas de amplicón (barcoding): medir variabilidad entre especies, identificar zonas conservadas para diseño de cebadores y proponer loci candidatos para estudios de identificación y filogenia.


---

## 🧩 Datos y muestras

- **Número de géneros esperados**: ~15–20  
- **Número de especies por género**: variable (1–5, según disponibilidad en NCBI)  
- **Tipo de datos**: Genomas cloroplastidiales completos (FASTA)  
- **Fuente**: NCBI GenBank  

---

## ⚙️ Metodología y pipeline

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

<img width="1024" height="1536" alt="image" src="https://github.com/user-attachments/assets/4368c929-1083-434f-a58c-f4bfbdcd0cca" />

---
