from jcsclient import compute
from jcsclient.compute_api.model import describe_images_request

def main():
	compute_obj = Controller()
	describe_images_request_obj = DescribeImagesRequest()
	describe_images_request_obj.set(["djkn","dc"])
	compute_obj.describe_images()
