#!/usr/bin/env python
# -*- coding: utf-8 -*-

# (c) 2012 Ville Korhonen <ville@xd.fi>

from scraper import *
scrapers = []


def register_scraper(scraper):
    scrapers.append(scraper)


def list_scrapers():
    return [x.name for x in scrapers]
