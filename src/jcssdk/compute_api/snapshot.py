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

from jcssdk import utils
from jcssdk import requestify


def create_snapshot(url, verb, headers, version, auth_info, is_secure, volume_id):
    params = {}
    params['Action'] = 'CreateSnapshot'
    params['Version'] = version
    params['VolumeId'] = volume_id
    return requestify.make_request(url, verb, headers, params, auth_info, is_secure)

def delete_snapshot(url, verb, headers, version, auth_info, is_secure, snapshot_id):
    params = {}
    params['Action'] = 'DeleteSnapshot'
    params['Version'] = version
    params['SnapshotId'] = snapshot_id
    return requestify.make_request(url, verb, headers, params, auth_info, is_secure)

def describe_snapshots(url, verb, headers, version, auth_info, is_secure, snpashot_ids = None, max_results = -1, next_token = "", detail = True):
    params = {}
    params['Action'] = 'DescribeSnapshots'
    params['Version'] = version

    if not snpashot_ids == None :
        i=1
        for snapshot_id in snpashot_ids :
            params["SnapshotId." + str(i)] = snapshot_id
            i+=1

    if not max_results == -1 :
    	params['MaxResults'] = max_results

    if not next_token == "" :
    	params['NextToken'] = next_token

   	params['Detail'] = str(detail)

    return requestify.make_request(url, verb, headers, params, auth_info, is_secure)


