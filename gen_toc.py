#!/usr/bin/env python

import re
import glob


def gen_toc(base_url, directory="", exclude=None):
    """
    Searches given directory for Markdown files and creates a linked Table of Contents.

    Args:
        base_url (str): URL to prepend all hyperlinks with.
        directory (str): Directory to search, defaults to current directory.
        exclude (list[str]): Files to exclude from search.

    Returns:
        (str): String containing Table of Contents Markdown.
    """

    # Get all Markdown filenames
    md_files = glob.glob("{}*.md".format(directory))

    # Filter out excluded files
    exclude = exclude if exclude else []
    md_files = [md_file for md_file in md_files if md_file not in exclude]

    # Build ToC by reading each file and converting headers into ordered lists with links
    toc = ""

    for md_file in sorted(md_files):
        last_level = 0

        with open(md_file, 'r') as fd:
            for line in fd.read().split('\n'):
                match = re.match('^(?P<header>#{1,6})(?P<text>.+)$', line)

                if not match:
                    continue

                header_level = len(match.groupdict().get('header'))

                # Mildly deal with jumps in level
                if header_level - last_level > 1:
                    header_level = last_level + 1
                else:
                    last_level = header_level

                spacing = "    " * (header_level - 1)
                text = match.groupdict().get('text').strip()
                anchor = re.sub("[^a-zA-Z\-\d]+", "", text.lower().replace(' ', '-'))
                url = "{base_url}{md_file}#{anchor}".format(base_url=base_url, md_file=md_file, anchor=anchor)
                toc += "{spacing} * [{text}]({url})\n".format(spacing=spacing, text=text, url=url)

    return toc

def main():
    toc = gen_toc(
        base_url="https://github.com/LAHacknight/cheatsheets/blob/master/",
        exclude=['readme.md', 'toc.md']
    )

    with open('toc.md', 'w') as fd:
        fd.write(toc)

if __name__ == "__main__":
    main()
