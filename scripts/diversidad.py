from Bio import AlignIO
from skbio import DistanceMatrix
import numpy as np
import glob
import re

generos = ["Dracula", "Aa"]
for gen in ["rbcL", "matK", "trnH-psbA"]:
    align = AlignIO.read(f"diversidad/{gen}_alineado.fasta", "fasta")
    ids = [rec.id for rec in align]

    def p_distance(seq1, seq2):
        diffs = sum(c1 != c2 for c1, c2 in zip(seq1, seq2) if c1 != '-' and c2 != '-')
        length = sum(c1 != '-' and c2 != '-' for c1, c2 in zip(seq1, seq2))
        return diffs / length if length > 0 else 0

    distances = [[p_distance(align[i].seq, align[j].seq) for j in range(len(align))] for i in range(len(align))]
    dm = DistanceMatrix(distances, ids)

    # π global
    pi_global = np.mean([dm[i, j] for i in range(len(ids)) for j in range(i+1, len(ids))])
    print(f"π global para {gen}: {pi_global}")

    # Intra e inter por género
    for g in generos:
        sub_ids = [id for id in ids if g in id]
        if len(sub_ids) > 1:
            sub_dm = dm.filter(sub_ids)
            intra_pi = np.mean([sub_dm[i, j] for i in range(len(sub_ids)) for j in range(i+1, len(sub_ids))])
            print(f"π intra-{g} para {gen}: {intra_pi}")

    # Inter: promedio entre géneros
    inter_dists = [dm[i, j] for i in range(len(ids)) for j in range(i+1, len(ids)) if re.split('_', ids[i])[0] != re.split('_', ids[j])[0]]
    inter_pi = np.mean(inter_dists) if inter_dists else 0
    print(f"π inter-géneros para {gen}: {inter_pi}")
