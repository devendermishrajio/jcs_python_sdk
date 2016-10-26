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

def attach_volume(url, verb, headers, version, auth_info, is_secure, instance_id, volume_id, device):
    params = {}
    params['Action'] = 'AttachVolume'
    params['Version'] = version
    params['InstanceId'] = instance_id
    params['VolumeId'] = volume_id
    params['Device'] = device
    return requestify.make_request(url, verb, headers, params, auth_info, is_secure)

def detach_volume(url, verb, headers, version, auth_info, is_secure, volume_id, instance_id = ""):
    params = {}
    params['Action'] = 'DetachVolume'
    params['Version'] = version
    params['VolumeId'] = volume_id
    if not instance_id == "" :
    	params['InstanceId'] = instance_id
    return requestify.make_request(url, verb, headers, params, auth_info, is_secure)

def show_delete_on_termination_flag(url, verb, headers, version, auth_info, is_secure, volume_id):
    params = {}
    params['Action'] = 'ShowDeleteOnTerminationFlag'
    params['Version'] = version
    params['VolumeId'] = volume_id
    return requestify.make_request(url, verb, headers, params, auth_info, is_secure)

def update_delete_on_termination_flag(url, verb, headers, version, auth_info, is_secure, volume_id, delete_on_termination):
    params = {}
    params['Action'] = 'UpdateDeleteOnTerminationFlag'
    params['Version'] = version
    params['VolumeId'] = volume_id
    params['DeleteOnTermination'] = str(delete_on_termination)
    return requestify.make_request(url, verb, headers, params, auth_info, is_secure)

def create_volume(url, verb, headers, version, auth_info, is_secure, snapshot_id = "", size = -1):
    params = {}
    params['Action'] = 'CreateVolume'
    params['Version'] = version
    if not snapshot_id == "" :
    	params['SnapshotId'] = snapshot_id

    if not size == -1 :
    	params['Size'] = str(size)

    return requestify.make_request(url, verb, headers, params, auth_info, is_secure)

def delete_volume(url, verb, headers, version, auth_info, is_secure, volume_id):
    params = {}
    params['Action'] = 'DeleteVolume'
    params['Version'] = version
    params['VolumeId'] = volume_id
    return requestify.make_request(url, verb, headers, params, auth_info, is_secure)

def describe_volumes(url, verb, headers, version, auth_info, is_secure, volume_ids = None, max_results = -1, next_token = "", detail = True):
    params = {}
    params['Action'] = 'DescribeVolumes'
    params['Version'] = version

    if not volume_ids == None :
        i=1
        for volume_id in volume_ids :
            params["VolumeId." + str(i)] = volume_id
            i+=1

    if not max_results == -1 :
    	params['MaxResults'] = max_results

    if not next_token == "" :
    	params['NextToken'] = next_token

   	params['Detail'] = str(detail)

    return requestify.make_request(url, verb, headers, params, auth_info, is_secure)

