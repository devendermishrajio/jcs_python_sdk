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
from DescribeInstancesResponse import Instance
from DescribeInstancesResponse import Group
from DescribeInstancesResponse import BlockDevice
class RunInstancesResponse(ContentHandler):
	def __init__(self):
		self.CurrentData = ""
		self.instances = []
		
		self.instance = None
		self.insideB = False
		self.insideG = False
		self.block_device = None
		self.group = None

	def startElement(self, tag, attributes):
		self.CurrentData = tag
		if tag == "blockDeviceMapping":
			insideB = True
		elif tag == "groupSet":
			insideG = True
		elif insideB and tag == "item":
			self.block_device = BlockDevice()
		elif insideG and tag == "item":
			self.group = Group()
		elif tag == "item":
			self.instance = instance()


	def endElement(self, tag):
		if insideB and tag == "item":
			self.instance.block_device_mapping.append(block_device)
		elif insideG and tag == "item":
			self.instance.groupset.append(group)
		elif tag == "blockDeviceMapping":
			self.insideB = False
		elif tag == "groupSet":
			self.insideG = False
		elif tag == "item":
			self.instances.append(instance)

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

