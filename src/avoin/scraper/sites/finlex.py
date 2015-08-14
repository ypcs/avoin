# -*- coding: utf-8 -*-

# Fetch data from finlex.fi

from ..scraper import DefaultScraper

class FinlexScraper(DefaultScraper):
    pass

def main():
    scraper = FinlexScraper()
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main())
