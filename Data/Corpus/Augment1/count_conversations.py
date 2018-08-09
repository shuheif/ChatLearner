
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
# Just counts the number of conversation pairs in a_papaya_new.txt
import os

FILE = 'a_papaya_new.txt'
COM = '==='

if os.path.isfile(FILE) and FILE.lower().endswith('.txt'):
	with open(FILE, 'r') as f:
		count = 0
		for line in f:
			if COM not in line:
				count += 1
		print('This file has ', count, ' lines of conversations')
		print(', which is ', count / 2, ' pairs')