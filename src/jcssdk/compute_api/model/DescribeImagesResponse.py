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
from jcssdk.utils import str2bool
class DescribeImagesResponse(ContentHandler):
	def __init__(self):
		self.CurrentData = ""
		self.images = []
		self.image = None
	
	def startElement(self, tag, attributes):
		self.CurrentData = tag
		if tag == "item":
			self.image = Image()
	
	def endElement(self, tag):
		if tag == "item":
			self.images.append(self.image) 

	def characters(self, content):
		if self.CurrentData == "deviceName":
			self.image.device_name = content
		elif self.CurrentData == "delete_on_termination":
			self.image.delete_on_termination = content
		elif self.CurrentData == "volumeSize":
			self.image.volume_size = content
		elif self.CurrentData == "snapshotId":
			self.image.snapshot_id = content
		elif self.CurrentData == "name":
			self.image.name = content
		elif self.CurrentData == "isPublice":
			self.image.is_public = str2bool(content)
		elif self.CurrentData == "imageId":
			self.image.image_id = content
		elif self.CurrentData == "imageState":
			self.image.image_state = content
		elif self.CurrentData == "architecture":
			self.image.architecture = content
		elif self.CurrentData == "imageType":
			self.image.image_type = content
		self.CurrentData = ""



class Image:
	def __init__(self):
		self.device_name = ""
		self.delete_on_termination = ""
		self.volume_size = 0.0
		self.snapshot_id = ""
		self.name = ""
		self.is_public = 0;
		self.image_id = ""
		self.image_state = "" 
		self.architecture = ""
		self.image_type = ""