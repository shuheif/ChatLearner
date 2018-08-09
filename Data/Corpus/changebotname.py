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
# Change name in the dataset, which is originally 'Papaya'.
import os
from settings import BOT_NAME
ORIGINAL_NAME = 'Papaya'
dir_list = ['Augment0', 'Augment1', 'Augment2']
# File path where this python file exists.
cur_dir = os.path.dirname(os.path.realpath(__file__))

print('Changing bot name from', ORIGINAL_NAME, 'to', BOT_NAME)
for dir in dir_list:
	file_dir = os.path.join(cur_dir, dir)
	for file in sorted(os.listdir(file_dir)):
		full_path = os.path.join(file_dir, file)
		if os.path.isfile(full_path) and file.lower().endswith('.txt'):
			tmp_file = file.lower().replace('.txt', '_tmp.txt')
			tmp_full_path = os.path.join(file_dir, tmp_file)
			with open(full_path, 'r') as f, open(tmp_full_path, 'a') as f_out:
				count = 0
				for line in f:
					if ORIGINAL_NAME in line:
						line = line.replace(ORIGINAL_NAME, BOT_NAME)
						count += 1
					f_out.write("{}\n".format(line.strip()))
				os.remove(full_path)
				os.rename(tmp_full_path, full_path)
				print('Replaced ', count, ' words in ', full_path)
