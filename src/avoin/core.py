#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import argparse

from __future__ import print_function

from avoin.scraper.scraper import DefaultScraper, xpath_parser, ScraperMissingElementError
from avoin.data.utils import read, write


def main(args):
    if args.command == 'xpath':
        scraper = DefaultScraper()
        xpath = args.xpath
        url = args.url

        format = args.format.lower()

        try:
            result = scraper.parse(url, parser=xpath_parser, format=format, xpath=xpath)

            if args.outfile:
                write(args.outfile, result)
            else:
                print(result)

        except ScraperMissingElementError:
            print("Element w/ XPath %s not found".format(xpath))



    return 0


def run():
    parser = argparse.ArgumentParser()

    parser.add_argument('command')
    parser.add_argument('--xpath', dest='xpath')
    parser.add_argument('--url', dest='url')
    parser.add_argument('--format', dest='format', default='text')
    parser.add_argument('--outfile', dest='outfile')
    parser.add_argument('--infile', dest='infile')

    args = parser.parse_args()
    sys.exit(main(args) or 0)


if __name__ == "__main__":
    run()
