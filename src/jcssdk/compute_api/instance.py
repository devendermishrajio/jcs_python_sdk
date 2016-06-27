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

import base64
import binascii
import requests
from jcssdk import utils
from jcssdk import requestify
# from jcssdk.compute_api.model import BlockDeviceMapping

def describe_instances(url, verb, headers, version, instance_ids = None):
    params = {}
    params['Action'] = 'DescribeInstances'
    params['Version'] = version

    if not instance_ids == None:
    	i=1
        for instance_id in instance_ids:
            params['InstanceId.' + str(i)] = instance_id
            i+=1
    return requestify.make_request(url, verb, headers, params)

def start_instances(url, verb, headers, version, instance_ids):
    params = {}
    params['Action'] = 'StartInstances'
    params['Version'] = version

    if not instance_ids == None :
    	i=1
        for instance_id in instance_ids:
	        params['InstanceId.' + str(i)] = instance_id
	        i+=1
    return requestify.make_request(url, verb, headers, params)

def stop_instances(url, verb, headers, version, instance_ids):
    params = {}
    params['Action'] = 'StopInstances'
    params['Version'] = version

    if not instance_ids == None:
    	i=1
        for instance_id in instance_ids:
	        params['InstanceId.' + str(i)] = instance_id
	        i+=1
    return requestify.make_request(url, verb, headers, params)

def reboot_instances(url, verb, headers, version, instance_ids):
    params = {}
    params['Action'] = 'RebootInstances'
    params['Version'] = version
    if not instance_ids == None:
    	i=1
        for instance_id in instance_ids:
	        params['InstanceId.' + str(i)] = instance_id
	        i+=1
    return requestify.make_request(url, verb, headers, params)
 
def terminate_instances(url, verb, headers, version, instance_ids):
    params = {}
    params['Action'] = 'TerminateInstances'
    params['Version'] = version
    if instance_ids != None:
    	i=1
        for instance_id in instance_ids:
	        params['InstanceId.' + str(i)] = instance_id
	        i+=1
    return requestify.make_request(url, verb, headers, params)

def describe_instance_types(url, verb, headers, version, instance_type_ids = None):
    params = {}
    params['Action'] = 'DescribeInstanceTypes'
    params['Version'] = version

    if not instance_type_ids == None:
        i=1
        for instance_type_id in instance_type_ids:
            params['InstanceTypeId.' + str(i)] = instance_type_id
            i+=1
    return requestify.make_request(url, verb, headers, params)

def run_instances(url, verb, headers, version, image_id, instance_type_id, blocks = None, instance_count = -1, subnet_id = "", 
	private_ip_address = "", security_group_ids = None, key_name = ""):
    params = {}
    params['Action'] = 'RunInstances'
    params['Version'] = version
    params['ImageId'] = image_id
    params['InstanceTypeId'] = instance_type_id
    if not blocks == None:
    	i=1
        for block in blocks :
    		if not block == None :
    			params['BlockDeviceMapping.' + str(i) + '.DeviceName'] = block.device_name
    			params['BlockDeviceMapping.' + str(i) + '.DeleteOnTermiantion'] = str(block.delete_on_termination)
    			params['BlockDeviceMapping.' + str(i) + '.VolumeSize'] = str(block.volume_size)
    		i+=1


    if not instance_count == -1 :
    	params['InstanceCount'] = instance_count

    if not subnet_id == "" :
    	params['SubnetId'] = subnet_id

    if not private_ip_address == "":
    	params['PrivateIpAddress'] = private_ip_address

    if not security_group_ids == None :
    	i=1
    	for security_group_id in security_group_ids :
    		params['SecurityGroupId.' + str(i)] = security_group_id
    		i+=1
    if not key_name == "" :
    	params['KeyName'] = key_name

    return requestify.make_request(url, verb, headers, params)

def decrypt_instance_password(password, private_key_file, passphrase):
    key = utils.import_ssh_key(private_key_file, passphrase)
    encrypted_data = base64.b64decode(base64.b64decode(password))
    print "encrypted_data :"
    print encrypted_data
    print ":end"
    print [ord(c) for c in encrypted_data]
    ciphertext = int(binascii.hexlify(encrypted_data), 16)
    plaintext = key.decrypt(ciphertext)
    print"cipher :"
    print ciphertext
    print ": end"
    decrypted_data = utils.long_to_bytes(plaintext)
    unpadded_data = utils.pkcs1_unpad(decrypted_data)
    return unpadded_data 

def get_password_data(url, verb, headers, version, args):
    params = {}
    params['Action'] = 'GetPasswordData'
    params['Version'] = version
    parser.add_argument('--instance-id', required=True)
    processed, remaining = parser.parse_known_args(args)
    utils.populate_params_from_cli_args(params, processed)
    response = requestify.make_request(url, verb, headers, params)
    parser = utils.get_argument_parser()
    parser.add_argument('--private-key-file', required=False, default=None)
    parser.add_argument('--key-passphrase', required=False, default=None)
    processed = parser.parse_args(remaining)
    processed = vars(processed)
    private_key_file = processed.get('private_key_file')
    passphrase = processed.get('key_passphrase')
    response_json = utils.web_response_to_json(response)
    try:
        response_body = response_json['GetPasswordDataResponse']
        encrypted_password = response_body['passwordData']
        if not private_key_file or not encrypted_password:
            return response
        decrypted_password = decrypt_instance_password(encrypted_password,
                                                       private_key_file,
                                                       passphrase)
        response_json['GetPasswordDataResponse']['passwordData'] = \
                                                  decrypted_password
        return response_json
    except KeyError as ke:
        raise exception.UnknownOutputFormat()
    
