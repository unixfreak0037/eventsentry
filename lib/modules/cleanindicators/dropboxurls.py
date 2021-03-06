import logging
import re

logger = logging.getLogger()


def run(event_json):
    logger.debug('Running the Dropbox URL cleanup module.')

    for i in event_json['indicators']:
        if i['type'] == 'URI - URL' or i['type'] == 'URI - Path':
            
            # Make sure this is a Dropbox URL or path.
            if 'dropbox.com' in i['value'] or any('dropbox.com' in r for r in i['relationships']):

                # See if the regex matches.
                download_pattern = re.compile(r'(?<![a-zA-Z0-9\-_])dropbox\.com/s/')
                if not download_pattern.search(i['value']) and not any(download_pattern.search(r) for r in i['relationships']):
                    logger.debug('Whitelisting non-download Dropbox.com indicator: {}'.format(i['value']))
                    i['whitelisted'] = True
