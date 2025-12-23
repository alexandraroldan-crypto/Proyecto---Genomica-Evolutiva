# extrae_rois.py
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqFeature import CompoundLocation
import os, glob

os.makedirs("rois", exist_ok=True)

def write_fasta(path, header, seq):
    with open(path, "w") as f:
        f.write(f">{header}\n{str(seq)}\n")

def rc_if_needed(seq, strand):
    return seq if strand != -1 else Seq(str(seq)).reverse_complement()

for gb in glob.glob("descarga/*.gb"):
    rec = SeqIO.read(gb, "genbank")
    base = os.path.basename(gb)[:-3]

    # rbcL
    rbcL_hits = [f for f in rec.features if f.type=="CDS" and "rbcL" in f.qualifiers.get("gene",[])]
    if rbcL_hits:
        f = rbcL_hits[0]; seq = rc_if_needed(f.extract(rec.seq), f.location.strand)
        write_fasta(f"rois/{base}_rbcL.fasta", f"{base}|rbcL", seq)

    # matK
    matK_hits = [f for f in rec.features if f.type=="CDS" and "matK" in f.qualifiers.get("gene",[])]
    if matK_hits:
        f = matK_hits[0]; seq = rc_if_needed(f.extract(rec.seq), f.location.strand)
        write_fasta(f"rois/{base}_matK.fasta", f"{base}|matK", seq)

    # trnL intrón
    trnL_feats = [f for f in rec.features if "trnL" in f.qualifiers.get("gene",[])]
    for f in trnL_feats:
        if isinstance(f.location, CompoundLocation) and len(f.location.parts)==2:
            left,right = f.location.parts
            intron_seq = rec.seq[int(left.end):int(right.start)]
            intron_seq = rc_if_needed(intron_seq, f.location.strand)
            write_fasta(f"rois/{base}_trnL.fasta", f"{base}|trnL_intron", intron_seq)
            break
