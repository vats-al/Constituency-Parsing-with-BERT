from nltk.corpus import treebank
import re
file_ids = treebank.fileids()
pos_tags = []
for file in file_ids:	
	for tree in treebank.parsed_sents(file):
		tree_str = str(tree)
		tree_pos = re.findall('[A-Z-]+', tree_str)
		pos_tags = pos_tags + tree_pos
stripped_tags = []
for tag in pos_tags:
	stripped_tag = tag.strip('-')
	stripped_tags.append(stripped_tag)
tag_set = set(stripped_tags)
label_dict = {}
label_dict['UNK'] = 0
i = 1
for label in tag_set:
	label_dict[label] = i
	i = i + 1
print(label_dict)
