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
	# Describe images
	elif i == 0:
		res = compute_obj.describe_images()

	# Describe instances
	elif i == 1:
		res = compute_obj.describe_instances()
		for instance in res.instances:
			print instance.instance_id
	# Describe instance types
	elif i == 2:
		res = compute_obj.describe_instance_types()
		for instance_type_id in res.instance_type_ids:
	# stop instances
	elif i == 3:
		res = compute_obj.stop_instances(instance_id = ['i-c85cf209'])
		for instance in res.instances:
			print instance.instance_id
	# start_instances
	elif i == 4:
		res = compute_obj.start_instances(instance_id = ['i-c85cf209'])
		for instance in res.instances:
			print instance.instance_id

	# reboot_instances
	elif i == 5:
		res = compute_obj.reboot_instances(instance_id = ['i-c85cf209'])
		for instance in res.instances:
			print instance.instance_id

	# terminate_instances
	elif i == 6:
		res = compute_obj.terminate_instances(instance_id = ['i-c85cf209'])
		for instance in res.instances:
			print instance.instance_id

	# run_instances
	elif i == 7:
		res = compute_obj.run_instances()
		for instance in res.instances:
			print instance.instance_id

	# describe_key_pairs
	elif i == 8:
		res = compute_obj.describe_key_pairs()
		for instance in res.instances:
			print instance.instance_id

	# create_key_pair
	elif i == 9:
		res = compute_obj.create_key_pair(key_name = 'test_pyth')
		for instance in res.instances:
			print instance.instance_id

	# delete_key_pair
	elif i == 10:
		res = compute_obj.delete_key_pair(key_name = 'test_pyth')
		for instance in res.instances:
			print instance.instance_id

	# create_snapshot
	elif i == 11:
		res = compute_obj.create_snapshot(volume_id = '91d82f45-6f08-407e-a46a-3e8b9ddb78b0')
		for instance in res.instances:
			print instance.instance_id

	# delete_snapshot
	elif i == 12:
		res = compute_obj.delete_snapshot(snapshot_id = '8b54ebed-484a-41b4-88ba-067798342902')
		for instance in res.instances:
			print instance.instance_id

	# describe_snapshots
	elif i == 13:
		res = compute_obj.describe_snapshots()
		for instance in res.instances:
			print instance.instance_id

	# create_volume
	elif i == 14:
		res = compute_obj.create_volume(size = 13)
		for instance in res.instances:
			print instance.instance_id

	# delete_volume
	elif i == 15:
		res = compute_obj.delete_volume(volume_id = '91d82f45-6f08-407e-a46a-3e8b9ddb78b0')
		for instance in res.instances:
			print instance.instance_id

	# attach_volume
	elif i == 16:
		res = compute_obj.attach_volume(volume_id = '91d82f45-6f08-407e-a46a-3e8b9ddb78b0', instance_id = 'i-c85cf209', device ='/dev/vdb')
		for instance in res.instances:
			print instance.instance_id

	# detach_volume
	elif i == 17:
		res = compute_obj.detach_volume(volume_id = '91d82f45-6f08-407e-a46a-3e8b9ddb78b0')
		for instance in res.instances:
			print instance.instance_id

	# describe_volumes
	elif i == 18:
		res = compute_obj.describe_volumes()
		for instance in res.instances:
			print instance.instance_id

	# show_delete_on_termination_flag
	elif i == 19:
		res = compute_obj.show_delete_on_termination_flag(volume_id = '91d82f45-6f08-407e-a46a-3e8b9ddb78b0')
		for instance in res.instances:
			print instance.instance_id

	# update_delete_on_termination_flag
	elif i == 20:
		res = compute_obj.update_delete_on_termination_flag(volume_id = '91d82f45-6f08-407e-a46a-3e8b9ddb78b0', delete_on_termination = True)
		for instance in res.instances:
			print instance.instance_id

	# import_key_pair
	elif i == 21:
		res = compute_obj.import_key_pair()
		for instance in res.instances:
			print instance.instance_id

	# get_password_data
	elif i == 22:
		res = compute_obj.get_password_data()
		for instance in res.instances:
			print instance.instance_id

	i = input()