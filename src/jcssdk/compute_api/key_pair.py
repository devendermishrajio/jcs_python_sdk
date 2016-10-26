# Copyright (c) 2016 Jiocloud.com, Inc. or its affiliates.  All Rights Reserved
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish, dis-
# tribute, sublicense, and/or sell copies of the Software, and to permi
# persons to whom the Software is furnished to do so, subject to the fol-
# lowing conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABIL-
# ITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT
# SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#

import argparse
from jcssdk import utils
from jcssdk import requestify

def create_key_pair(url, verb, headers, version, auth_info, is_secure, key_name ):
    params = {}
    params['Action'] = 'CreateKeyPair'
    params['Version'] = version
    params['KeyName'] = key_name
    return requestify.make_request(url, verb, headers, params, auth_info, is_secure)

def delete_key_pair(url, verb, headers, version, auth_info, is_secure, key_name):
    params = {}
    params['Action'] = 'DeleteKeyPair'
    params['Version'] = version
    params['KeyName'] = key_name
    return requestify.make_request(url, verb, headers, params, auth_info, is_secure)

def describe_key_pairs(url, verb, headers, version):
    params = {}
    params['Action'] = 'DescribeKeyPairs'
    params['Version'] = version
    return requestify.make_request(url, verb, headers, params, auth_info, is_secure)

def import_key_pair(url, verb, headers, version, auth_info, is_secure, key_name, public_key_material):
    params = {}
    params['Action'] = 'ImportKeyPair'
    params['Version'] = version
    params['KeyName'] = key_name
    params['PublicKeyMaterial'] = public_key_material
    return requestify.make_request(url, verb, headers, params, auth_info, is_secure)

