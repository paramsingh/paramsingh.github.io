import json
import os
import time
import uuid

from mastodon import Mastodon
from datetime import datetime

INSTAGRAM_DIR = '/home/param/Downloads/instagram'

mastodon = None


def init_mastodon():
    Mastodon.create_app(f'paramsinstaimporter-{str(uuid.uuid4())}', api_base_url='https://mitron.social',
                        to_file='paramsinstaimporter.secret')
    global mastodon
    mastodon = Mastodon(client_id='paramsinstaimporter.secret',
                        api_base_url='https://mitron.social')
    mastodon.log_in(username='iliekcomputers@gmail.com',
                    password='justgoogleit', to_file='paramsusercred.secret')


def post_to_mastodon(caption: str, location: str, original_posted_at: datetime, filepath: str):
    new_caption = f'{caption}'
    if location:
        new_caption = f'{new_caption}\n\nLocation: {location}'
    new_caption = f'{new_caption}\n\nOriginally posted on Instagram on {original_posted_at.strftime("%Y/%m/%d")} at {original_posted_at.strftime("%H:%M")} UTC.'
    while True:
        try:
            print(f'Uploading file {filepath}...')
            photo = mastodon.media_post(filepath)
            print('Done!')
            break
        except Exception as e:
            print("Error %s" % str(e))
            print("trying again...")
            pass

    print('Posting toot...')
    toot = mastodon.status_post(new_caption, media_ids=[photo['id']])
    print('Done!')
    print(toot['uri'])
    time.sleep(60)


def main():
    init_mastodon()
    with open(os.path.join(INSTAGRAM_DIR, 'media.json')) as f:
        media_info = json.load(f)

    count = 1
    print(f"Total of {len(media_info['photos'])}!")
    found = False
    for photo in media_info['photos'][::-1]:
        if '0152cefbacb6771ce5d4e6c7990cd90b' in photo['path']:
            found = True
            continue
        if found:
            post_to_mastodon(
                caption=photo['caption'],
                location=photo.get('location', ''),
                original_posted_at=datetime.strptime(
                    photo['taken_at'], '%Y-%m-%dT%H:%M:%S+00:00'),
                filepath=os.path.join(INSTAGRAM_DIR, photo['path']),
            )
            print(f'Photo #{count} done, taken at {photo["taken_at"]}!')
        count += 1


if __name__ == '__main__':
    main()
