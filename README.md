# avoin
Python code for data scraping

    pip install avoin
    pip install git+https://github.com/ypcs/avoin.git#egg=avoin
    
    >>> from avoin.scraper.scraper import DefaultScraper, html_title_parser
    >>> scraper = DefaultScraper()
    >>> url = 'http://www.google.com/'
    
    >>> result = scraper.parse(url, parser=html_title_parser)
    >>> print result
    Google
    
    >>> result = scraper.parse(url, parser=html_title_parser, format='json')
    >>> print result
    "Google"
    

(c) 2012 Ville Korhonen <ville@xd.fi>
