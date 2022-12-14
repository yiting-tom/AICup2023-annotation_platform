# Copyright 2018 Amazon Research Cambridge
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import json
import sys
from nltk import word_tokenize
from typing import Tuple


def count_file(file_path) -> Tuple:
    total_claims, total_tokens = 0, 0
    with open(file_path, encoding="utf-8") as data_in:
        for line in data_in:
            data_json = json.loads(line)
            claim = data_json["claim"]
            claim_tokens = word_tokenize(claim)
            total_claims += 1
            total_tokens += len(claim_tokens)
    return total_claims, total_tokens


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Please enter at least one file name.")
        print("Usage: %s <file_name> [<file_name_2> ...]" % "dataset_stats.py")
        exit(1)
    files = sys.argv[1:]
    grand_total_claims, grand_total_tokens = 0, 0
    for file in files:
        claims, tokens = count_file(file)
        average = tokens / claims
        print(
            "File: %s -- Claims: %d, Tokens: %d, Average length: %.2f"
            % (file, claims, tokens, average)
        )
        grand_total_claims += claims
        grand_total_tokens += tokens
    grand_average = grand_total_tokens / grand_total_claims
    print("-------------")
    print(
        "Total Claims: %d, Total Tokens: %d, Average length: %.2f"
        % (grand_total_claims, grand_total_tokens, grand_average)
    )
