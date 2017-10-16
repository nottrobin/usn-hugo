#! /usr/bin/env python3

import re
import dateutil.parser
import glob
import frontmatter


date_re = re.compile(r'(?<=\n[*]).*(?=[*]\n)')

for filepath in glob.iglob('*.md'):
    with open(filepath) as file_handle:
        file_content = file_handle.read()

    file_content = re.sub(r'\n--- +\n', '\n---\n', file_content)
    date_match = date_re.search(file_content)
    front = frontmatter.loads(file_content)

    if date_match:
        text_date = date_match.group()
        date = dateutil.parser.parse(text_date).replace(hour=12)
        if date != front.metadata['date']:
            import ipdb; ipdb.set_trace()
            print(filepath)
