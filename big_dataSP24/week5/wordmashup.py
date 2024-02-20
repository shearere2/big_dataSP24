
class WordMashup():
	db = []
	transition = []
	maxorder = 0
	nskips = 0

	def __init__(self, wordlist='', order=2):
		if len(wordlist) > 0:
			self.add(wordlist, order)

	def get(self, sz=100, printsource=False):
		"""Automatically generate text of length sz."""
		out, dbn = self._initialize() # dbn is last used database number
		dbs = 0 # Count of how many time a database has been doubled
		sourcedb = []

		# Get database search order for future randomization
		so = [i for i in range(len(self.db))]
		for i in range(sz):
			random.shuffle(so)
			n = 0 # which db of db search order
			suborder = 0 # subtract from order
			fnd = False
			skips = 0 # number of times we get too low in order
			while not fnd and skips < self.nskips:
				order = len(self.db[so[n]])
				key = tuple(out[-order:])

				if suborder >= order:
					skips += 1
					n += 1
				elif (len(self.transition) > 0 and so[n] == dbn 
					and random.random() < self.transition[dbs]):
					n += 1
				elif key in self.db[so[n]][suborder]:
					fnd = True
				else:
					n += 1

				if n >= len(so):
					n = 0
					suborder += 1

			# Catch situation where we've maxed out transitions but the
			# word is only in the repeated corpus
			if skips == self.nskips:
				suborder = len(self.db[dbn]) - 1
				key = (out[-1],)
			elif so[n] != dbn:
				dbs = 0
				dbn = so[n]
			else:
				dbs += 1
			
			sourcedb.append(dbn)
			out.append(random.choice(self.db[dbn][suborder][key]))

		if printsource: print(sourcedb)
		if out[0][-1] == '.': out = out[1:]
		return ' '.join(out)

	def add(self, path, order=2):
		"""
		Add a new text source with the number of words that must match.
		Path is the path to the file, order is the set of matching words
		"""
		fp = open(path, 'r')
		words = fp.read().split()

		# Save the maximum order for determining initialization
		self.maxorder = order if order > self.maxorder else self.maxorder
		# And save the number of skips in case a transition is forced
		self.nskips += order

		# self.db is a list of sources, with each source being a list of
		# dictionaries of length order, saved in descending order.
		self.db.append([{} for i in range(order)])
		for i in range(len(words) - order):
			key = tuple(words[i:i+order])
			val = words[i+order]
			if key in self.db[-1][0]:
				self.db[-1][0][key].append(val)
			else:
				self.db[-1][0][key] = [val]

		# Now add all lower order keys. This will improve mashups
		pos = 1
		while order - pos > 0:
			for key in self.db[-1][pos - 1]:
				self.db[-1][pos][tuple(list(key)[1:])] = self.db[-1][pos - 1][key]
			pos += 1


	def forceswitch(self, n):
		"""
		Try to force mashups. At length n, the probability that a switch
		will occur is 100% unless the last word is not amongst any other
		word database.
		"""

		if n < 1:
			self.transition = []
		else:
			self.transition = [float(i)/(n - 1) for i in range(n)]

	def _initialize(self):
		self._firstwords()
		dbnum = random.choice(range(len(self.firsts)))
		key = random.choice(self.firsts[dbnum])

		# Return as a list which will become the list of text
		key = list(key)

		# We have to make sure that the initialization is long enough to
		# be added to by any of the word databases.
		if len(key) < self.maxorder:
			for i in range(self.maxorder - len(key)):
				order = len(self.db[dbnum])
				key.append(random.choice(self.db[dbnum][0][tuple(key[-order:])]))

		return (key, dbnum)

	def _firstwords(self):
		"""
		Generate a list of all words that follow periods, if at least
		one database is of order > 1, or list all capitalized words.
		"""

		self.firsts = []

		for i, d in enumerate(self.db):
			self.firsts.append([])
			if self.maxorder == 1 and len(d) == 1:
				for w in d[0].keys():
					if w.istitle():
						self.firsts[i].append(w)
			elif self.maxorder > 1 and len(d) > 1:
				for w in d[0].keys():
					if w[0][-1] == '.':
						self.firsts[i].append(w)

if __name__ == '__main__':
	from sys import argv
	if len(argv) < 3:
		print('ERROR: need path to text corpus and order.')
		exit()

	arglen = len(argv)

	wg = WordMashup()
	if arglen%2 == 0:
		wg.forceswitch(int(argv[-1]))
		arglen -= 1
	for corpus in range(int(round((arglen - 1)/2))):
		wg.add(argv[corpus*2 + 1], int(argv[corpus*2 + 2]))
		print('Added text corpus %s' % (argv[corpus*2 + 1]))
	
	print(wg.get(200, True))