import csv
import os
import frontmatter

CSV_DIR = './highlights/csv'
HIGHLIGHTS_DIR = './highlights'


def create_markdown_file(filename: str):
    content = ''
    title = ''
    with open(os.path.join(CSV_DIR, filename)) as f:
        filereader = csv.reader(f)
        for index, row in enumerate(filereader):
            if index == 1:
                title = row[0]
            if 'Highlight' in row[0]:
                content += '"{}"'.format(row[3])
                content += '\n\n'
                content += '---------'
                content += '\n\n'
    post = frontmatter.Post(content)
    post['layout'] = 'page'
    post['title'] = title.capitalize()
    with open(os.path.join(HIGHLIGHTS_DIR, filename + '.md'), 'w') as f:
        print(frontmatter.dumps(post), file=f)


def main():
    for csv_file in os.listdir(CSV_DIR):
        create_markdown_file(csv_file)


if __name__ == '__main__':
    main()
