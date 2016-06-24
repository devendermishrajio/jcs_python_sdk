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
class DescribeSnapshotsResponse(ContentHandler):
	def __init__(self):
		self.CurrentData = ""
		self.snapshots= []
		
		self.snapshot = None
		self.insideA = False
		self.attachment = None

	def startElement(self, tag, attributes):
		self.CurrentData = tag
		if tag == "attachmentSet":
			insideA = True
		elif insideA and tag == "item":
			self.attachment = Attachment()
		elif tag == "item":
			self.snapshot = Snapshot()


	def endElement(self, tag):
		if insideA and tag == "item":
			self.snapshot.attachment_set.append(self.attachment)
		elif tag == "attachmentSet":
			self.insideA = False
		elif tag == "item":
			self.snapshots.append(self.snapshot)

	def characters(self, content):
		if self.CurrentData == "status":
			self.snapshot.status = content
		elif self.CurrentData == "volumeId":
			self.snapshot.volume_id = content
		elif self.CurrentData == "volumeSize":
			self.snapshot.size = float(content)
		elif self.CurrentData == "createTime":
			self.snapshot.create_time = content
		elif self.CurrentData == "snapshot_id":
			self.snapshot.snapshot_id = content
		elif self.CurrentData == "device":
			self.attachment.device = content
		elif self.CurrentData == "instanceId":
			self.attachment.instance_id = content

		self.CurrentData = ""


class Volume:
	def __init__(self):
		self.status = ""
		self.volume_id = ""
		self.size = None
		self.create_time = ""
		self.snapshot_id = ""
		self.attachment_set = []
		

class Attachment:
	def __init__(self):
		self.device = ""
		self.instance_id = ""
