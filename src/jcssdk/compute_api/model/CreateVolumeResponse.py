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
## This Class Object handles the response of Create Snapshot Response
class CreateVolumeResponse(ContentHandler):
	
	def __init__(self):
		self.CurrentData = ""
		## @var status
		# Status of the Volume Created
		self.status = ""
		## @var snapshot_id
		# Snapshot ID linked with the Volume
		self.snapshot_id = ""
		## @var size
		# volume size
		self.size = None
		## @var volume_id
		self.volume_id = ""
		## @var create_time
		self.create_time = ""
	#Override ContentHandler method for XML Parsing 
	def startElement(self, tag, attributes):
		self.CurrentData = tag

	def characters(self, content):
		if self.CurrentData == "status":
			self.status = content
		elif self.CurrentData == "snapshotId":
			self.snapshot_id = content
		elif self.CurrentData == "size":
			self.size = float(content)
		elif self.CurrentData == "volumeId":
			self.volume_id = content
		elif self.CurrentData == "createTime":
			self.create_time = content
		self.CurrentData = ""
