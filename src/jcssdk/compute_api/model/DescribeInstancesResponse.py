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

from xml.sax import ContentHandler
## Class to handle Describe instances request's 
class DescribeInstancesResponse(ContentHandler):
	def __init__(self):
		self.CurrentData = ""
		## @var instances
		# A list of instances
		self.instances = []
		
		self.instance = None
		self.insideB = False
		self.insideG = False
		self.block_device = None
		self.group = None

	def startElement(self, tag, attributes):
		self.CurrentData = tag
		if tag == "blockDeviceMapping":
			self.insideB = True
		elif tag == "groupSet":
			self.insideG = True
		elif self.insideB and tag == "item":
			self.block_device = BlockDevice()
		elif self.insideG and tag == "item":
			self.group = Group()
		elif tag == "item":
			self.instance = Instance()


	def endElement(self, tag):
		if self.insideB and tag == "item":
			self.instance.block_device_mapping.append(self.block_device)
		elif self.insideG and tag == "item":
			self.instance.group_set.append(self.group)
		elif tag == "blockDeviceMapping":
			self.insideB = False
		elif tag == "groupSet":
			self.insideG = False
		elif tag == "item":
			self.instances.append(self.instance)

	def characters(self, content):
		if self.CurrentData == "status":
			self.block_device.status = content
		elif self.CurrentData == "deviceName":
			self.block_device.device_name = content
		elif self.CurrentData == "deleteOnTermination":
			self.block_device.delete_on_termination = bool(content)
		elif self.CurrentData == "volumeId":
			self.block_device.volume_id = content
		elif self.CurrentData == "dnsName":
			self.instance.dns_name = content
		elif self.CurrentData == "instanceId":
			self.instance.instance_id = content
		elif self.CurrentData == "instanceState":
			self.instance.instance_state = content
		elif self.CurrentData == "imageId":
			self.instance.image_id = content
		elif self.CurrentData == "privateDnsName":
			self.instance.private_dns_name = content
		elif self.CurrentData == "keyName":
			self.instance.key_name = content
		elif self.CurrentData == "launchTime":
			self.instance.launch_time = content
		elif self.CurrentData == "subnetId":
			self.instance.subnet_id = content
		elif self.CurrentData == "groupName":
			self.group.group_name = content
		elif self.CurrentData == "groupId":
			self.group.group_id = content
		elif self.CurrentData == "vpcId":
			self.instance.vpc_id = content
		elif self.CurrentData == "instanceType":
			self.instance.instance_type = content
		elif self.CurrentData == "privateIpAddress":
			self.instance.private_ip_address = content
		
		self.CurrentData = ""

## Class Instance
class Instance:
	def __init__(self):
		## @var dns_name
		self.dns_name = ""
		## @var instance_id
		# Instance ID of the Instance
		self.instance_id = ""
		## @var instance_state
		# Instance State of the instance 
		self.instance_state = ""
		## @var image_id
		# Image ID of the image
		self.image_id = ""
		## @var private_dns_name
		self.private_dns_name = ""
		## @var key_name
		self.key_name = ""
		## @var launch_time
		self.launch_time = ""
		## @var subnet_id
		# Subnet Id to which the image belongs
		self.subnet_id = ""
		## @var vpc_id
		# Virtual CPU ID 
		self.vpc_id = ""
		## @var instance_type
		self.instance_type = ""
		## @var private_ip_address
		self.private_ip_address = ""
		## @var group_set
		# List of Group associated with the image
		self.group_set = []
		## @var block_device_mapping
		# List of BlockDevice 
		self.block_device_mapping = []

## Class Group
class Group:
	def __init__(self):
		## @var group_name
		self.group_name = ""
		## @var group_id
		self.group_id = ""

## Class BlockDevice
class BlockDevice:
	def __init__(self):
		## @var status
		self.status = ""
		## @var device_name
		self.device_name = ""
		## @var delete_on_termination
		self.delete_on_termination = None
		## @var volume_id
		self.volume_id = ""
