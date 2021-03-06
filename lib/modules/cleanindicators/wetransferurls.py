import logging
import re

logger = logging.getLogger()


def run(event_json):
    logger.debug('Running the WeTranser URL cleanup module.')

    for i in event_json['indicators']:
        if i['type'] == 'URI - URL' or i['type'] == 'URI - Path':
            
            # Make sure this is a Dropbox URL or path.
            if 'wetransfer.com' in i['value'] or any('wetransfer.com' in r for r in i['relationships']):

                # See if the regex matches.
                download_pattern = re.compile(r'(?<![a-zA-Z0-9\-_])wetransfer\.com/downloads/')
                if not download_pattern.search(i['value']) and not any(download_pattern.search(r) for r in i['relationships']):
                    logger.debug('Whitelisting non-download WeTransfer.com indicator: {}'.format(i['value']))
                    i['whitelisted'] = True
