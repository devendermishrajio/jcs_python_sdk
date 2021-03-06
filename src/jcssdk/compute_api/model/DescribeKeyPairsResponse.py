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
## This Class handle Describe Key Pair Request's Response
class DescribeKeyPairsResponse(ContentHandler):
	def __init__(self):
		self.CurrentData = ""
		## @var key_pairs
		# List of Key Pairs
		self.key_pairs = []
		self.key_pair = None
	#Override ContentHandler method for XML Parsing 
	def startElement(self, tag, attributes):
		self.CurrentData = tag
		if tag =="item":
			self.key_pair = KeyPair()

	def endElement(self, tag):
		if tag == "item":
			self.key_pairs.append(self.key_pair)


	def characters(self, content):
		if self.CurrentData == "keyName":
			self.key_pair.key_name = content
		elif self.CurrentData == "keyFingerprint":
			self.key_pair.key_fingerprint = content
		self.CurrentData = ""

class KeyPair:
	def __init__(self):
		## @var Key_fingerprint
		self.key_fingerprint = ""
		## @var key_material
		self.key_name  = ""