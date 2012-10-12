#!/usr/bin/env python
# -*- coding: utf-8 -*-

# (c) 2012 Ville Korhonen <ville@xd.fi>

scrapers = []

def register_scraper(scraper):
    scrapers.append(scraper)

def list_scrapers():
    return [x.name for x in scrapers]
