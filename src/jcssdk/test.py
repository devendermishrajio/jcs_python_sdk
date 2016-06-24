import sys
from jcssdk import compute

compute_obj = compute.Controller()
# function_caller={
# 	"0" : compute_obj.describe_images(),
# 	"1" : compute_obj.describe_instances(),
# 	"2" : compute_obj.describe_instance_types()
# }

i = input()
while not i == -1:
	if i == -1:
		break
	elif i == 0:
		res = compute_obj.describe_images()
		# print res.image_ids[0]

	elif i == 1:
		res = compute_obj.describe_instances()
		for instance in res.instances:
			print instance.instance_id
	elif i == 2:
		res = compute_obj.describe_instance_types()
		for instance_id in res.instance_type_ids:
			print instance_id

	i = input()