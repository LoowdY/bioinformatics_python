#Define as possibilidades de nucleotideos
Nucleotideos = ("A", "C", "T", "G")

#função de tratamento de exceçoes: caso o usuário digite algum nucelotide inválido
def validacaoSeq(seq_dna):
    tempseq = seq_dna.upper()
    for nuc in tempseq:
        if nuc not in Nucleotideos:
            return False
    return tempseq

#função que conta cada nucleotídeo a partir de uma string de uma string de entrada
def contaNucleotideos(seq):
    NucFreqDic = {"A": 0, "C": 0, "T": 0, "G": 0}
    for nuc in seq:
        NucFreqDic[nuc] += 1
    return NucFreqDic
