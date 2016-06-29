# Copyright (c) 2016 Jiocloud.com, Inc. or its affiliates.  All Rights Reserved
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish, dis-
# tribute, sublicense, and/or sell copies of the Software, and to permit
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

import sys
import requests
from jcssdk import config
from jcssdk.compute_api.model import ErrorResponse
from xml.sax import parseString
from jcssdk import auth_handler

common_headers = {
    'Content-Type': 'application/json',
    'Accept-Encoding': 'identity',
}

def make_request(url, verb, headers, params, path=None, data=None):
    """
    This method makes the actual request to JCS services. 
    The steps are:
        1. Create an AuthHandler object to add signature to the request.
        2. Add any common headers to request like Content.
        3. Use requests library to send the requests to JCS service.

    Benefit ot AuthHandler class is that we can modify the Signature
    generation mechanism under the hood.

    """
    try :
        access_key = config.get_access_key()
        secret_key = config.get_secret_key()
        # Always calculate signature without trailing '/' in url
        if url.endswith('/'):
            url = url[:-1]
        auth_obj = auth_handler.Authorization(url, verb, access_key, 
                                              secret_key, headers)
        auth_obj.add_authorization(params)

        # Now restore the trailing '/' in url
        url += '/?'
        request_string = url
        for key, val in params.items():
            request_string += str(key) + '=' + str(val) + '&'
        request_string = request_string[:-1]
        global common_headers
        headers.update(common_headers)
        # print request_string
        response = requests.request(verb, request_string, data=data, 
                                verify=config.check_secure(),
                                headers=headers)

        if response.status_code == 200:
            return response
        else:
            error_res = ErrorResponse.ErrorResponse()
            parseString(str(response.text), error_res)
            print error_res.code
            print error_res.message
            return None
    except Exception as e:
        sys.stderr.write('Connection unsuccessful...!!\n')
        sys.stderr.write(str(e))
        sys.stderr.write("\n")
        if config.check_debug():
            raise
        sys.exit(1)