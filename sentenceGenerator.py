from nltk.corpus import treebank

# extra_words = []
def get_trees_sentences():
	trees = []
	sentences = []
	for file in treebank.fileids():
		for tree in treebank.parsed_sents(file):
			tree_str = str(tree)
			trees.append(tree_str)
		for sentence in treebank.sents(file):
			s=""
			s=" ".join(words for words in sentence)
			sentences.append(s)
	assert len(trees) == len(sentences)
	sentences = list(map(lambda x: x.lower(), sentences))
	return (trees, sentences)

def replace_extra_words(sentence=None):
	sent_word_list = sentence.split()
	replaced_list = ['[UNK]' if x.startswith('*') else x for x in sent_word_list]
		
	sentence = " ".join(words for words in replaced_list)
	return sentence

if __name__ == '__main__':
	(trees, sentences) = get_trees_sentences()
	sentences = list(map(replace_extra_words, sentences))
	for sent2 in sentences:
		print(sent2)
