""" This script adds an addendum to each note, adding all notes that link to it.
"""

import click
import os
import os.path
import frontmatter
import re

from collections import defaultdict
from typing import List, Set


NOTES_DIR = './notes'

def _get_all_notes():
    all_notes = []
    for _, _, files in os.walk(NOTES_DIR):
        all_notes.extend([filename for filename in files if filename.endswith('.md')])
    return all_notes

def _list_note_links(note: List[str]):
    """ Return a list of notes that the given node links to

    Example return value: ["index.md"]
    """
    regex = re.compile(r"(\{% link notes/)+(?P<note_name>\w+)(\.md %\})+")
    links = []
    for line in open(os.path.join(NOTES_DIR, note)):
        # Need the line to match a regex with checks for
        # something like ({% link notes/graded_cut.md %}) and
        # then get the note name out of it
        matches = regex.finditer(line)
        for match in matches:
            links.append(f"{match.group('note_name')}.md")
    return links


def _get_note_title(note_filename: str):
    note = frontmatter.load(os.path.join(NOTES_DIR, note_filename))
    return note['title']


def write_backlinks_to_note(note_filename: str, backlinks: Set[str]):
    if len(backlinks) == 0:
        return

    note = frontmatter.load(os.path.join(NOTES_DIR, note_filename))
    note['backlinks'] = {link: _get_note_title(link) for link in backlinks}
    with open(os.path.join(NOTES_DIR, note_filename), 'wb') as f:
        frontmatter.dump(note, f)


@click.command()
@click.option('--dry-run', is_flag=True)
def main(dry_run):
    """ This function loops through all markdown files in the notes directory,
    assuming a flat notes directory.

    It finds backlinks and for each backlink, adds an entry to the original note.

    Use --dry-run to test what it does, without modifying the files.
    """
    all_notes = _get_all_notes()
    backlink_map = defaultdict(set)
    for note in all_notes:
        links = _list_note_links(note)
        for link in links:
            backlink_map[link].add(note)
    for note, backlinks in backlink_map.items():
        if dry_run:
            print(note, ": ", backlinks)
            print("\n")
        else:
            write_backlinks_to_note(note, backlinks)


if __name__ == '__main__':
    main()
