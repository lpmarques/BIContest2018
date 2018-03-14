from sys import argv
import editdistance
  
def getifTandem(r1_start,r1_len,seq,seqlen,maxdprop):
  r2_start = r1_start+r1_len
  maxlev = int(r1_len*maxdprop)
  
  #test case 1: repeats have same length
  rep1 = seq[r1_start:r2_start]
  rep2 = seq[r2_start:r2_start+r1_len]
  lev = editdistance.eval(rep1,rep2)
  passcost = lev-maxlev # number of necessary nucleotide changes in one of the sections to consider it a tandem repeat
  if passcost<=0:
    return [r1_start,r1_len,r1_len,lev]
  
  #test case 2: by virtue of indels, repeats differ in length
  if passcost<=maxlev:
    indlen = int(maxlev)+1
    passcost = 1
    while lev>maxlev:
      lastlev = lev
      indlen = indlen-passcost or -1
      r2_len = r1_len+indlen
      if indlen<0:
        maxlev=r2_len*maxdprop
        if indlen<-maxlev:
          break
      rep2 = seq[r2_start:r2_start+r2_len]
      lev = editdistance.eval(rep1,rep2)
      passcost = lev-int(maxlev)
    else:
      return [r1_start,r1_len,r2_len,lev]
  
  #case 3: the section is not a tandem repeat
  return [lev]

IN = open(argv[1],"r")
maxdprop = argv[2] if len(argv)>2 else 0.1 #maximum proportional difference between two sequence sections to be considered tandem repeats

for line in IN.readlines():
  if line[0]==">":
    continue
    
  seq = line[:-1]
  seqlen = len(seq)

  sectlen = 5000 if seqlen>=10000 else int(seqlen/2) #length of the first sequence section to be evaluated as tandem repeat
  maxd = int(sectlen*maxdprop) #maximum absolute difference between two sections to be considered tandem repeats
  mind = sectlen #minimum difference between any two sections evaluated so far
  sect0 = 0 #start position of the first section
  tandems = []
  
  while 1:
    tandem = getifTandem(sect0,sectlen,seq,seqlen,maxdprop)
    #d = tandem.pop(-1)
    d = tandem[-1]
    if d<mind:
      mind = d
    if len(tandem)>1:
      tandems.append(tandem)

    sect0 += d-maxd if d-maxd>0 else 1
    if sect0+sectlen*2 > seqlen:
      if tandems:
        lt = max(tandems,key=lambda x:(x[1]+x[2],-x[3])) #longest tandem in sequence
        print(lt[0],lt[1],lt[2])
        break
      sectlen -= int((mind-maxd)/2) or 1
      maxd = int(sectlen*maxdprop)
      sect0 = 0
      tandems = []
