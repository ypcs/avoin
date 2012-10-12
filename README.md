# avoin
Python code for data scraping  
(c) 2012 Ville Korhonen (ville@xd.fi), GPLv3

## Installation
You may install directly from PyPI using:

    pip install avoin

or latest HEAD via git:

    pip install git+https://github.com/ypcs/avoin.git#egg=avoin
    
## Using (via Python Shell)
```python
    >>> from avoin.scraper.scraper import DefaultScraper, html_title_parser
    >>> scraper = DefaultScraper()
    >>> url = 'http://www.google.com/'
    
    >>> result = scraper.parse(url, parser=html_title_parser)
    >>> print result
    Google
    
    >>> result = scraper.parse(url, parser=html_title_parser, format='json')
    >>> print result
    "Google"
```


## Using (via command line)
Fetch all URLs from webpage as plaintext

    avoin xpath --url 'http://ypcs.fi/' --xpath '//a/@href' --format text
    
