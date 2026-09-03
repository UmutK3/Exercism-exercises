def to_rna(dna_strand):
    matches = {"A" : "U", "T" : "A",  "C" : "G", "G" :"C"}
    return "".join(matches[nucleotid] for nucleotid in dna_strand if nucleotid in matches)
print(to_rna("ACGTGGTCTTAA"))


























        
#for nucleotid in dna_strand:
       # if nucleotid in matches:
            #rna_form += matches[nucleotid]