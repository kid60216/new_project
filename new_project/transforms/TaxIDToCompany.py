#/usr/bin/env python
# -*- coding: UTF-8 -*-

import socket
import json
import requests
from maltego_trx.maltego import UIM_TYPES
from maltego_trx.entities import IPAddress

from maltego_trx.transform import DiscoverableTransform


class TaxIDToCompany(DiscoverableTransform):
    """
    Search TaxID and search the result of company.
    """

    @classmethod
    def create_entities(cls, request, response):
        taxid = request.Properties['properties.taxid']
        r = requests.get(f'http://company.g0v.ronny.tw/api/show/{taxid}')
        result = json.loads(r.text)
        response.addEntity('maltego.Company', result['data']['公司名稱'])