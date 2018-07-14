#!/usr/bin/env python2

from requests import get
import click , bs4

URL = 'http://0se.ir/'
PATH = 'tools.php'
_OUT_MESSAGE = 'Short URL is: {}'

@click.command('lazyShortURL')
@click.option('--url','-u','url',prompt='Enter URL to Short it Please',help='Enter URL to Short it')
def __lazyShortURL(url):
    """ Lazy Method to Short a URL """
    PARAMS = {
        'tid' : 1,
        'full': url
    }
    # Send Request to Short Link
    response = get('{}{}'.format(URL,PATH),params=PARAMS)
    # Parse Response !
    bs = bs4.BeautifulSoup(response.content,'html.parser')
    # Find Result in Response
    result = bs.findAll("div", {"class": "messagesentok"})
    if(len(result) != 0):
        out = result[0].get_text()
        click.echo(_OUT_MESSAGE.format(out))
        return out
    else:
        click.echo('Cant Convert it.')
        return None

if __name__ == '__main__':
    __lazyShortURL()