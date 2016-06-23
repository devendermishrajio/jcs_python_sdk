import sys
from jcssdk import compute
from jcssdk.compute_api.model import describe_images_request

print "start"
compute_obj = compute.Controller()
describe_images_request_obj = describe_images_request.DescribeImagesRequest()
describe_images_request_obj.set_image_ids(["djkn","dc"])
compute_obj.describe_images(describe_images_request_obj)
