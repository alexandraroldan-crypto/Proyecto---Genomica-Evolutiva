
## Descargar genomas cloroplastidiales

python descarga.py

## Obtencion de Rois

python extraer_rois.py


mkdir diversidad
for gen in rbcL matK trnH-psbA; do
    cat rois/*_${gen}.fasta > diversidad/todos_${gen}.fasta
    mafft --auto diversidad/todos_${gen}.fasta > diversidad/${gen}_alineado.fasta
done


## Datos de parametos de Roi's
python diversidad.py

mkdir alineados
for gen in rbcL matK trnH-psbA; do
    cat rois/*_${gen}.fasta > alineados/todos_${gen}.fasta
done

for file in alineados/todos_*.fasta; do
    mafft --auto --adjustdirection --reorder $file > ${file%.fasta}_alineado.fasta
done

# Usa script para concatenar alineados (mantén IDs consistentes)
python -c "from Bio.AlignIO import MultipleSeqAlignment; from Bio import AlignIO; alns = [AlignIO.read(f, 'fasta') for f in glob.glob('alineados/*_alineado.fasta')]; concat = MultipleSeqAlignment([]); for aln in alns: concat += aln; AlignIO.write(concat, 'filogenia/concatenado.fasta', 'fasta')"


mkdir -p filogenia

for alineado in alineados/*_alineado.fasta; do
    # Extrae el nombre del marcador (ej: rbcL, matK, trnH-psbA)
    marcador=$(basename "$alineado" _alineado.fasta | sed 's/todos_//')

    echo "Construyendo árbol para $marcador..."

    iqtree2 -s "$alineado" \
            -m MFP \
            -B 1000 \
            -T AUTO \
            --prefix filogenia/${marcador}_tree
done



python arbol.py

