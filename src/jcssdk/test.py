import sys
import os
from jcssdk import compute
import base64


compute_obj = compute.Controller()

i = input()
while not i == -1:
	if i == -1:
		break
	# Describe images
	elif i == 0:
		res = compute_obj.describe_images(image_ids = ['jmi-bc345d58','jmi-d523af5f'])
		if not res == None:
			for image in res.images:
				print image.image_id

	# Describe instances
	elif i == 1:
		res = compute_obj.describe_instances()
		if not res == None:
			for instance in res.instances:
				print instance.instance_id
				print instance.instance_state
	# Describe instance types
	elif i == 2:
		res = compute_obj.describe_instance_types(instance_type_ids = None)
		if not res == None:
			for instance_type in res.instances:
				print instance_type.vcpus
				print instance_type.ram
	# stop instances
	elif i == 3:
		res = compute_obj.stop_instances(instance_ids = ['i-c85cf209','i-21a763b1'])
		if not res == None:
			for instance in res.instances:
				print instance.current_state
				print instance.previous_state
	# start_instances
	elif i == 4:
		res = compute_obj.start_instances(instance_ids = ['i-c85cf209','i-21a763b1'])
		if not res == None:
			for instance in res.instances:
				print instance.current_state

	# reboot_instances
	elif i == 5:
		res = compute_obj.reboot_instances(instance_ids = ['i-c85cf209','i-21a763b1'])
		if not res == None:
			for instance in res.instances:
				print instance.current_state

	# terminate_instances
	elif i == 6:
		res = compute_obj.terminate_instances(instance_ids = ['i-56133bc7'])
		if not res == None:
			for instance in res.instances:
				print instance.current_state

	# run_instances
	elif i == 7:
		block = [{'device_name':'/dev/vdb', 'delete_on_termination':'true','volume_size':'17'},{'device_name':'/dev/vdc	', 'delete_on_termination':'true','volume_size':'18'}]
		res = compute_obj.run_instances(image_id = 'jmi-bc345d58', instance_type_id = "c1.small", key_name = 'intern', blocks = block)
		if not res == None:
			for instance in res.instances:
				print instance.instance_id

	# describe_key_pairs
	elif i == 8:
		res = compute_obj.describe_key_pairs()
		if not res == None:
			for key in res.key_pairs:
				print key.key_name

	# create_key_pair
	elif i == 9:
		res = compute_obj.create_key_pair(key_name = 'test_pyth1')
		if not res == None:
			print res.key_fingerprint

	# delete_key_pair
	elif i == 10:
		res = compute_obj.delete_key_pair(key_name = 'test_pyth1')
		if not res == None:
			print res.result

	# create_snapshot
	elif i == 11:
		res = compute_obj.create_snapshot(volume_id = '39668951-cd2e-4397-a48e-052a84647a11')
		if not res == None :
			print res.snapshot_id

	# delete_snapshot
	elif i == 12:
		res = compute_obj.delete_snapshot(snapshot_id = '58c84c92-e06a-43a4-8ffa-669799b10f6f')
		if not res == None:
			print res.result

	# describe_snapshots
	elif i == 13:
		res = compute_obj.describe_snapshots(snpashot_ids = ['54790b1f-0d24-4375-9d33-1437036ef877','60e015f7-0e77-4c26-84c2-5f01f4f4bfc7'])
		if not res == None:
			for snapshot in res.snapshots:
				print snapshot.snapshot_id
				print snapshot.size

	# create_volume
	elif i == 14:
		res = compute_obj.create_volume(size = 13,snapshot_id = '60e015f7-0e77-4c26-84c2-5f01f4f4bfc7')
		if not res == None:
			print res.volume_id

	# delete_volume
	elif i == 15:
		res = compute_obj.delete_volume(volume_id = '60d042b5-e682-4c3e-a546-401999a5ab85')
		if not res == None:
			print res.result

	# attach_volume
	elif i == 16:
		res = compute_obj.attach_volume(volume_id = '60d042b5-e682-4c3e-a546-401999a5ab85', instance_id = 'i-c85cf209', device ='/dev/vdb')
		if not res == None:
			print res.volume_id

	# detach_volume
	elif i == 17:
		res = compute_obj.detach_volume(volume_id = '60d042b5-e682-4c3e-a546-401999a5ab85',instance_id = 'i-c85cf209')
		if not res == None:
			print res.volume_id

	# describe_volumes
	elif i == 18:
		res = compute_obj.describe_volumes()
		if not res == None:
			for volume in res.volumes:
				print volume.volume_id

	# show_delete_on_termination_flag
	elif i == 19:
		res = compute_obj.show_delete_on_termination_flag(volume_id = '60d042b5-e682-4c3e-a546-401999a5ab85')
		if not res == None:
			print res.delete_on_termination
			print res.volume_id

	# update_delete_on_termination_flag
	elif i == 20:
		res = compute_obj.update_delete_on_termination_flag(volume_id = '60d042b5-e682-4c3e-a546-401999a5ab85', delete_on_termination = False)
		if not res == None:
			print res.delete_on_termination
			print res.volume_id

	# import_key_pair
	elif i == 21:
		file = open('/home/gowtham/Desktop/reliance/jcs_python_sdk/import_key.pub','r')
		key = file.readline()
		file.close()
		key = base64.b64encode(key)
		res = compute_obj.import_key_pair(key_name = 'import_test', public_key_material = key)
		if not res == None:
			print res.key_material

	# get_password_data
	elif i == 22:
		res = compute_obj.get_password_data(instance_id = 'i-c85cf209' ,private_key_file = "/home/gowtham/Desktop/reliance/jcs_python_sdk/key.pem")
		if not res == None:
			print res.password_data

	i = input()