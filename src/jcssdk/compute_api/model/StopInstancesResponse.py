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
from RebootInstancesResponse import InstanceState
## This Class handles Stop Instance's Request Response
class StopInstancesResponse(ContentHandler):
	def __init__(self):
		self.CurrentData = ""
		## @var instances
		# List of Objects of Class Instance
		self.instances = []
		self.instance = None
		
	def startElement(self, tag, attributes):
		self.CurrentData = tag
		if tag =="item":
			self.instance = InstanceState()

	def endElement(self, tag):
		if tag == "item":
			self.instances.append(self.instance)


	def characters(self, content):
		if self.CurrentData == "instanceId":
			self.instance.instance_id = content
		elif self.CurrentData == "previousState":
			self.instance.previous_state = content
		elif self.CurrentData == "currentState":
			self.instance.current_state = content
		self.CurrentData = ""
