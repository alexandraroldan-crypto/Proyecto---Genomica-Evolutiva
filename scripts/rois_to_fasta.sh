## Descargar genomas cloroplastidiales

python ../ROIS/descarga.py

## Obtencion de Rois

python ../ROIS/extraer_rois.py


mkdir diversidad
for gen in rbcL matK trnH-psbA; do
    cat rois/*_${gen}.fasta > diversidad/todos_${gen}.fasta
    mafft --auto diversidad/todos_${gen}.fasta > diversidad/${gen}_alineado.fasta
done


## Datos de parametos de Roi's
python ../ROIS/diversidad.py

mkdir alineados
for gen in rbcL matK trnH-psbA; do
    cat rois/*_${gen}.fasta > alineados/todos_${gen}.fasta
done

for file in alineados/todos_*.fasta; do
    mafft --auto --adjustdirection --reorder $file > ${file%.fasta}_alineado.fasta
done

# Usa script para concatenar alineados (mantén IDs consistentes)
python -c "from Bio.AlignIO import MultipleSeqAlignment; from Bio import AlignIO; alns = [AlignIO.read(f, 'fasta') for f in glob.glob('alineados/*_alineado.fasta')]; concat = MultipleSeqAlignment([]); for aln in alns: concat += aln; AlignIO.write(concat, 'filogenia/concatenado.fasta', 'fasta')"

mkdir filogenia
iqtree2 -s alineados/todos_rbcL_alineado.fasta -m MFP -B 1000 -T AUTO -pre filogenia/rbcL_tree
# Repite por otros genes o concatenado

