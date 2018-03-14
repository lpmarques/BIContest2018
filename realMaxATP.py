from sys import argv

def glycolysis(glumols):
	atpmols = 2.0*glumols # 2 ATP payoff for each glucose consumed
	return atpmols

def respiration(glumols,oxymols):
	glyc_atpmols = glycolysis(glumols)

	if glyc_atpmols/2.0 <= oxymols/6.0: # 6 O2 and 2 ATP needed on each respiration cycle
		trans_atpmols = glyc_atpmols
	else:
		trans_atpmols = (oxymols/6.0)*2

	glyc_atpmols -= trans_atpmols # 'transATP' = ATP taken from glycolysis' payoff to invest in respiration
	atpmols = glyc_atpmols + 19*trans_atpmols # 38 ATP payoff for each 2 'transATP' invested
	return atpmols

IN = open(argv[0],"r")

for line in IN:
	[glu_price,oxy_price,max_cost] = (int(x) for x in line.split(" "))
	glu_prop = 0
	maxatp = 0
	prev_atpmols = 0
	step = 0.1
	downsteps = 0
	maxdown = 1
	converged = False

	while not converged:
		glu_prop += step
		if glu_prop > 1:
			break

		glumols = (glu_prop*max_cost)/glu_price
		oxymols = ((1-glu_prop)*max_cost)/oxy_price	
		atpmols = respiration(glumols,oxymols)

		if maxatp < atpmols:
			maxatp = atpmols
		elif atpmols < prev_atpmols:
			downsteps+=1
			if downsteps >= maxdown:
				glu_prop -= downsteps*step+step
				if glu_prop < 0:
					glu_prop = 0

				downsteps = 0

				step /= 10
				maxdown = maxdown*2
				if step<1e-9:
					converged = True

		prev_atpmols = atpmols

	print(str(maxatp))

IN.close()
