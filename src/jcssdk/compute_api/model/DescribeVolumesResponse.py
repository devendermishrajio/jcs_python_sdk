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
##This Class handles Describe Volume Request's Response
class DescribeVolumesResponse(ContentHandler):
	def __init__(self):
		self.CurrentData = ""
		## @var volumes
		# List of volume class object
		self.volumes = []
		
		self.volume = None
		self.insideA = False
		self.attachment = None
	
	#Override ContentHandler method for XML Parsing 
	def startElement(self, tag, attributes):
		self.CurrentData = tag
		if tag == "attachmentSet":
			self.insideA = True
		elif self.insideA and tag == "item":
			self.attachment = Attachment()
		elif tag == "item":
			self.volume = Volume()


	def endElement(self, tag):
		if self.insideA and tag == "item":
			self.volume.attachment_set.append(self.attachment)
		elif tag == "attachmentSet":
			self.insideA = False
		elif tag == "item":
			self.volumes.append(self.volume)

	def characters(self, content):
		if self.CurrentData == "status":
			self.volume.status = content
		elif self.CurrentData == "volumeId":
			self.volume.volume_id = content
		elif self.CurrentData == "size":
			self.volume.size = float(content)
		elif self.CurrentData == "createTime":
			self.volume.create_time = content
		elif self.CurrentData == "snapshot_id":
			self.volume.snapshot_id = content
		elif self.CurrentData == "device":
			self.attachment.device = content
		elif self.CurrentData == "instanceId":
			self.attachment.instance_id = content

		self.CurrentData = ""








## Class Volume
class Volume:
	def __init__(self):
		## @var status
		# Current Status of the volume
		self.status = ""
		## @var volume_id
		self.volume_id = ""
		## @var size
		self.size = None
		## @var create_time
		self.create_time = ""
		## @var snapshot_id
		self.snapshot_id = ""
		## @var attachment_set
		# List of objects of class Attachment
		self.attachment_set = []
		

## Class Attachment
class Attachment:
	def __init__(self):
		## @var device
		self.device = ""
		## @var instance_id
		self.instance_id = ""
