

class graph:

    def __init__(self,gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def edges(self):
        return self.findedges()
# Add the new edge

    def AddEdge(self, edge):
        edge = set(edge)
        (vrtx1, vrtx2) = tuple(edge)
        if vrtx1 in self.gdict:
            self.gdict[vrtx1].append(vrtx2)
        else:
            self.gdict[vrtx1] = [vrtx2]

# List the edge names
    def findedges(self):
        edgename = []
        for vrtx in self.gdict:
            for nxtvrtx in self.gdict[vrtx]:
                if {nxtvrtx, vrtx} not in edgename:
                    edgename.append({vrtx, nxtvrtx})
        return edgename

# Create the dictionary with graph elements
graph_elements = { "a" : ["b","c"],
                "b" : ["a", "d"],
                "c" : ["a", "d"],
                "d" : ["e"],
                "e" : ["d"]
                }

g = graph(graph_elements)
g.AddEdge({'a','e'})
g.AddEdge({'a','c'})
print(g.edges())


def overlap(X, Y):
	L = [[0 for x in range(len(Y)+1)] for x in range (len(X)+1)]

	for i in range(len(X)+1):
		for j in range(len(Y)+1):
			if i == 0 or j == 0:
				L[i][j] = 0
			elif X[i-1] == Y[j-1]:
				L[i][j] = L[i-1][j-1] + 1 
			else:
				L[i][j] = max(L[i-1][j], L[i][j-1])
	index = L[len(X)][len(Y)]
	lcs = [""] * (index + 1)
	lcs[index] = ""
	i = len(X)
	j = len(Y)
	while i > 0 and j > 0:
		if X[i-1] == Y[j-1]:
			lcs[index-1] = X[i-1]
			i-=1
			j-=1
			index-=1
		elif L[i-1][j] > L[i][j-1]:
			i-=1
		else:
			j-=1
	print ("".join(lcs[:-1]))


if __name__ == "__main__": 
  
    str1 = 'TGTCTAGTATTATTTACACGGCAGAACAAAGTACGTACCAAACTCCCCAGTTGGTGCAGGTGAGGTGCGCGGTTTCCCAGGATATGAGTGGATACAACCTCTTGTACTGAGTCATCTATAAGTCATTTTCAGAGACCAAGATCAACTGCTGACAGACTACTCAGTACCGCCTGTTAATCCTCGAGTATTTATATACGACCGGTCTAGTTAATACATCTACGGCGTGTGCGACGTGTCACGGACGGCTGGCGTTTATCCTCGAAATGCGGGAAGGGAGTTTCTTTAGCTATGGGGGCTGGATCCAGTTGACTAATCAAGAAATATGCAATAAACTAAGACGCTCAGGGTTTTGAAATCGCCCGGATGATCTGAGCTCACCAGTGCGTCGCAGACGCCCTACTTTCCGATGTGTGAAACCAAATATCGGCCTTTAACTAGTGGAGATCTTATACTTCATATGTTCGAGATGTACGGGTGCCGGCTCATCCAGCCCCTTGTCA'
    str2 = 'ATTAAACCCACGCCTTCGGCGACCATGATCACGTAGAGATGCCAAAACCCGATGGCTTAGCAAGCGTTTAGAACACCAATAAGAGTGTATGCTTTATCCGAGACTACCAGAGGCCGACGCTCCGTAAGCATAAACGCAGAACTTCATTCGTTACCAGGACTGACCGTAAATAAGCGGGGTTGCTACTCGGATCCTTCTCAGTCACTACCCCACTCGAACTGACAAGATATGGACCCTTCTAATTCCAAGTCCACTCATCCCATCTTTACGGGGCGTTTTTGGAGATGTCAAAAGGCTACTGCTGCATATATGCGCGCAAGTGCCGTTGCCCTGTAGGGCGAGCAACTTTGAGTGACTCTACCATCTCGTCATACTCACCGCGAAGTATACGCCACCCACCTGGACAATAGTAGCCATCTGAATCTCAACGCCTTGTGGATTGTAAACCACAGATGATAAATCCCGTCTCGGTTATCCTGGTAACCGTACCCTCGATATAT'
    overlap(str1,str2) 
    


#https://www.geeksforgeeks.org/printing-longest-common-subsequence/
#https://ideone.com/tfhY6P
#https://www.bogotobogo.com/python/python_graph_data_structures.php
#https://github.com/BessieChen/Coursera-Genome-Assembly-Programming-Challenge/blob/master/week1/Q1/submit001.py
#https://ocw.mit.edu/courses/biology/7-91j-foundations-of-computational-and-systems-biology-spring-2014/lecture-slides/MIT7_91JS14_Lecture6.pdf
#https://moodle.cs.colorado.edu/pluginfile.php/156853/mod_resource/content/1/Grand%20Challenge_%20Genome%20Assembly.pdf
#https://github.com/AndriiShostatskyi/Genome-Assembly-Programming-Challenge
