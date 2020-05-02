from nltk.corpus import treebank
import re
# extra_words = []
whitespace = "\r\n\t"
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
	
def get_tree_string(tree=None):
	# tree = str(tree)
	tree = tree.replace("\n", "")
	tree = tree.replace("\r", "")
	tree = tree.replace("\t", "")
	tree = re.sub('[ ]{2,}', " ", tree)
	return tree

if __name__ == '__main__':
	(trees, sentences) = get_trees_sentences()	
	sentences = list(map(replace_extra_words, sentences))
	#trees = list(map(get_tree_string, trees))
	#for t in trees:
	#	print(t)
	max_len = 0
	count = 0
	i = 1
	for sent in sentences:
		sent_len = len(sent.split())
		#print(str(i) + " " + str(sent_len))
		max_len = max(max_len, sent_len)
		if sent_len > 60:
			count = count + 1
			#print(sent)
			#print()
		i = i + 1
	print('OUTPUT:',max_len, count)