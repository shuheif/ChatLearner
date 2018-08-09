
# Copyright 2018 Shuhei Fujita. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
# Create a new conversation file based on a_papaya_new.txt
# Execute changebotname.py before running this file
import os
from settings import BOT_NAME
import nltk
nltk.download('punkt')

PAPAYA_FILE = 'a_papaya_new.txt'
NEW_FILE = BOT_NAME + '_conversation.txt'

if os.path.isfile(PAPAYA_FILE) and PAPAYA_FILE.lower().endswith('.txt'):
	with open(PAPAYA_FILE, 'r') as f, open(NEW_FILE, 'a') as f_out:
		for line in f:
			if '===' in line:
				f_out.write("{}\n".format(line.strip()))
			if 'Q: ' in line:
				f_out.write("{}\n".format(line.strip()))
				print(line.strip())
			if 'A: ' in line:	
				input_answer = input('A: ')
				tokens = nltk.word_tokenize(input_answer)
				answer = "A: " + ' '.join(tokens[:]).strip()
				if '_func' in line:
					answer += ' '
					index = line.index('_func')
					answer += line[index:].strip()
				f_out.write("{}\n".format(answer))
