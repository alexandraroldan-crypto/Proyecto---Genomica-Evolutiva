## Instalar Miniconda

## Descargar archivos
  wget -r -nH --cut-dirs=3 ftp://ftp.ncbi.nlm.nih.gov/refseq/release/plastid/
ls -lh *genomic*
rm *protein*
gunzip -d *genomic*

grep -A 5 "Dracula" *genomic*


plastid.3.genomic.gbff:DEFINITION  Dracula mendozae chloroplast, complete genome.
plastid.3.genomic.gbff-ACCESSION   NC_085156
plastid.3.genomic.gbff-VERSION     NC_085156.1
plastid.3.genomic.gbff-DBLINK      BioProject: PRJNA927338
plastid.3.genomic.gbff-KEYWORDS    RefSeq.
plastid.3.genomic.gbff:SOURCE      chloroplast Dracula mendozae
plastid.3.genomic.gbff:  ORGANISM  Dracula mendozae
plastid.3.genomic.gbff-            Eukaryota; Viridiplantae; Streptophyta; Embryophyta; Tracheophyta;
plastid.3.genomic.gbff-            Spermatophyta; Magnoliopsida; Liliopsida; Asparagales; Orchidaceae;
plastid.3.genomic.gbff:            Epidendroideae; Epidendreae; Pleurothallidinae;Dracula.
plastid.3.genomic.gbff-REFERENCE   1  (bases 1 to 157484)
plastid.3.genomic.gbff-  CONSRTM   NCBI Genome Project
plastid.3.genomic.gbff-  TITLE     Direct Submission
plastid.3.genomic.gbff-  JOURNAL   Submitted (31-JAN-2024) National Center for Biotechnology
plastid.3.genomic.gbff-            Information, NIH, Bethesda, MD 20894, USA
--
plastid.3.genomic.gbff:                     /organism="Dracula mendozae"
plastid.3.genomic.gbff-                     /organelle="plastid:chloroplast"
plastid.3.genomic.gbff-                     /mol_type="genomic DNA"
plastid.3.genomic.gbff-                     /db_xref="taxon:2706247"
plastid.3.genomic.gbff-     gene            complement(join(100001..100805,70178..70291))
plastid.3.genomic.gbff-                     /gene="rps12"
--
