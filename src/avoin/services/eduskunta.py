# -*- coding: utf-8 -*-

import logging
import sys

import requests
import requests_cache


EDUSKUNTA_API_URL = 'https://avoindata.eduskunta.fi'

# <https://avoindata.eduskunta.fi/api/v1/tables/>
EDUSKUNTA_API_TABLES = (
    'Attachment',
    'AttachmentGroup',
    'HetekaData',
    'PrimaryKeys',
    'SaliDBAanestys',
    'SaliDBAanestysAsiakirja',
    'SaliDBAanestysEdustaja',
    'SaliDBAanestysJakauma',
    'SaliDBAanestysKieli',
    'SaliDBIstunto',
    'SaliDBKohta',
    'SaliDBKohtaAanestys',
    'SaliDBKohtaAsiakirja',
    'SaliDBMessageLog',
    'SaliDBPuheenvuoro',
    'SaliDBTiedote',
    'VaskiData',
)




class EduskuntaAPI(object):
    def __init__(self, url=EDUSKUNTA_API_URL):
        self.url = url

    def get(self, table, **params):
        if table not in EDUSKUNTA_API_TABLES:
            raise KeyError
        headers = {
            'User-Agent': 'avoin/0.1',
            'Accept': 'application/json',
        }
        query_params = {
            'page': 0,
            'perPage': 100,
        }
        query_params.update(params)
        results = []

        url = '{url}/api/v1/tables/{table}/rows'.format(url=self.url, table=table)
        i = 0
        while True:
            i += 1
            # FIXME: stop ignoring cert errors after EK has fixed their stuff...
            res = requests.get(url, headers=headers, params=query_params, verify=False)
            if res.status_code == requests.codes.ok:
                #print(res.text)
                data = res.json()
                #print(data)
                #results.append(data)
                print(i)
                if not data.get('hasMore', False):
                    break
                query_params['page'] += 1
            else:
                raise IOError
        return results


def main():
    requests_cache.install_cache(expire_after=8640000)

    api = EduskuntaAPI()
    for table in EDUSKUNTA_API_TABLES:
        if table.startswith('SaliDB'):
            api.get(table=table)



if __name__ == '__main__':
    sys.exit(main())
