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
#This Class handles Describe Snapshot Request's Response
class DescribeSnapshotsResponse(ContentHandler):
	def __init__(self):
		self.CurrentData = ""
		## @var snapshots
		# List of Class Snapshot Objects
		self.snapshots= []
		
		self.snapshot = None
	#Override ContentHandler method for XML Parsing 
	def startElement(self, tag, attributes):
		self.CurrentData = tag
		if tag == "item":
			self.snapshot = Snapshot()


	def endElement(self, tag):
		if tag == "item":
			self.snapshots.append(self.snapshot)

	def characters(self, content):
		if self.CurrentData == "status":
			self.snapshot.status = content
		elif self.CurrentData == "volumeId":
			self.snapshot.volume_id = content
		elif self.CurrentData == "volumeSize":
			self.snapshot.size = float(content)
		elif self.CurrentData == "startTime":
			self.snapshot.start_time = content
		elif self.CurrentData == "snapshotId":
			self.snapshot.snapshot_id = content
		self.CurrentData = ""


# Class Snapshot
class Snapshot:
	def __init__(self):
		## @var status
		self.status = ""
		## @var volume_id
		self.volume_id = ""
		## @var size
		self.size = None
		## @var start_time
		self.start_time = ""
		## @var snapshot_id
		self.snapshot_id = ""