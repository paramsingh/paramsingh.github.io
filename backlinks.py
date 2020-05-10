""" This script adds an addendum to each note, adding all notes that link to it.
"""

import click
import os
import os.path
import re

from collections import defaultdict


NOTES_DIR = './notes'

def _get_all_notes():
    all_notes = []
    for path, dirs, files in os.walk(NOTES_DIR):
        all_notes.extend([filename for filename in files if filename.endswith('.md')])
    return all_notes

def get_note_title(note):
    for line in open(os.path.join(NOTES_DIR, note), 'r'):
        if line.startswith('title:'):
            return ':'.join([line.strip() for line in line.split(':')[1:]])




def _list_note_links(note):
    """ Return a list of notes that the given node links to
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


def write_backlinks_to_note(note, backlinks):
    if len(backlinks) == 0:
        return

    # Read the file
    original_lines = []
    for line in open(os.path.join(NOTES_DIR, note), 'r'):
        if 'Links to this note' in line:
            original_lines.pop() # remove the last ___ separator
            original_lines.pop()
            break
        original_lines.append(line)

    # Construct content to write
    lines_to_add = ['___', '\n', '### Links to this note\n']
    for link in backlinks:
        note_title = get_note_title(link)
        line = "* [{}]({{% link notes/{} %}})\n".format(note_title, link)
        lines_to_add.append(line)
    lines_to_add.extend(['\n\n___\n\n', '### Footnotes\n']) #TODO: find a way to not add the footnotes heading if it isn't needed

    with open(os.path.join(NOTES_DIR, note), 'w') as f:
        f.writelines(original_lines + lines_to_add)


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