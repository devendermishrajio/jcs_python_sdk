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

from jcssdk import config
from jcssdk import utils
from jcssdk.compute_api import image
from jcssdk.compute_api import key_pair
from jcssdk.compute_api import instance
from jcssdk.compute_api import volume
from jcssdk.compute_api import snapshot
from jcssdk.compute_api.model import DescribeInstancesResponse
from jcssdk.compute_api.model import DescribeInstanceTypesResponse
from jcssdk.compute_api.model import DescribeImagesResponse
from jcssdk.compute_api.model import DescribeVolumesResponse
from jcssdk.compute_api.model import DescribeSnapshotsResponse
from jcssdk.compute_api.model import DescribeKeyPairsResponse
from jcssdk.compute_api.model import AttachVolumeResponse
from jcssdk.compute_api.model import CreateKeyPairResponse
from jcssdk.compute_api.model import CreateSnapshotResponse
from jcssdk.compute_api.model import CreateVolumeResponse
from jcssdk.compute_api.model import DeleteKeyPairResponse
from jcssdk.compute_api.model import DeleteSnapshotResponse
from jcssdk.compute_api.model import DeleteVolumeResponse
from jcssdk.compute_api.model import DetachVolumeResponse
from jcssdk.compute_api.model import GetPasswordDataResponse
from jcssdk.compute_api.model import ImportKeyPairsResponse
from jcssdk.compute_api.model import RebootInstancesResponse
from jcssdk.compute_api.model import RunInstancesResponse
from jcssdk.compute_api.model import ShowDeleteOnTerminationResponse
from jcssdk.compute_api.model import UpdateDeleteOnTerminationResponse
from jcssdk.compute_api.model import StopInstancesResponse
from jcssdk.compute_api.model import StartInstancesResponse
from jcssdk.compute_api.model import TerminateInstancesResponse
from xml.sax import parseString

class Controller(object):
    """Compute Controller class

    This class has all the functions for compute

    It acts as a wrapper over how the calls are
    internally handled

    In the controller methods, first argument passed
    in list of args is the Action name
    """

    def __init__(self):
        self.url = config.get_service_url('compute')
        self.headers = {}
        self.version = '2016-03-01'
        self.verb = 'GET'

    def describe_images(self, image_ids = None):
        """
        Gives a detailed list of all images visible in
        the account

        param args: Arguments passed to the function

        The function expects either no input or a list of 
        specific images to describe
        """
        response = image.describe_images(self.url, self.verb, self.headers,
                                     self.version, image_ids)
        if response is not None :
            res = DescribeImagesResponse.DescribeImagesResponse()
            parseString(str(response.text), res)
            return res
        else :
            return None


    def create_key_pair(self, key_name):
        """
        Create a key pair to be used during instance
        creation

        param args: Arguments passed to the function

        The function expects a key-name as necessary
        input
        """
        response = key_pair.create_key_pair(self.url, self.verb, self.headers,
                                        self.version, key_name)
        if response is not None :
            res = CreateKeyPairResponse.CreateKeyPairResponse()
            parseString(str(response.text), res)
            return res
        else :
            return None
 
    def delete_key_pair(self, key_name):
        """
        Delete a key pair from your account

        param args: Arguments passed to the function

        The function expects a key-name as necessary
        input
        """
        response = key_pair.delete_key_pair(self.url, self.verb, self.headers,
                                        self.version, key_name)
        if response is not None :
            res = DeleteKeyPairResponse.DeleteKeyPairResponse()
            parseString(str(response.text), res)
            return res
        else :
            return None

    def describe_key_pairs(self):
        """
        Describes all key pair in your account

        param args: Arguments passed to the function

        The function expects no arguments
        """
        response = key_pair.describe_key_pairs(self.url, self.verb,
                                           self.headers, self.version)
        if response is not None :
            res = DescribeKeyPairsResponse.DescribeKeyPairsResponse()
            parseString(str(response.text), res)
            return res
        else :
            return None

    def import_key_pair(self, key_name, public_key_material):
        """
        Import the public key from an RSA keypair that was
        created using a third-party application

        param args: Arguments passed to the function

        The function expects the following arguments -
        1. Unique name of Key Pair to import
        2. Public Key Material in base64 encoded form
        """
        response = key_pair.import_key_pair(self.url, self.verb, self.headers,
                                        self.version, key_name, public_key_material)
        if response is not None :
            res = ImportKeyPairsResponse.ImportKeyPairsResponse()
            parseString(str(response.text), res)
            return res
        else :
            return None

    def describe_instances(self, instance_ids = None):
        """
        Describes instances in your account

        param args: Arguments passed to the function

        The function expects either of the following:
        1. No argument
        2. List of instances to be described
        3. List of filters from which instances would
           be selected.
        """
        response = instance.describe_instances(self.url, self.verb,
                                           self.headers, self.version, instance_ids)
        if response is not None :
            res = DescribeInstancesResponse.DescribeInstancesResponse()
            parseString(str(response.text), res)
            return res
        else :
            return None

    def stop_instances(self, instance_ids):
        """
        Stop instances in your account

        param args: Arguments passed to the function

        The function expects one or more instances to
        be stopped.
        """
        response = instance.stop_instances(self.url, self.verb,
                                       self.headers, self.version, instance_ids)
        if response is not None :
            res = StopInstancesResponse.StopInstancesResponse()
            parseString(str(response.text), res)
            return res
        else :
            return None

    def start_instances(self, instance_ids):
        """
        Start instances in your account

        param args: Arguments passed to the function

        The function expects one or more instances to
        be started.
        """
        response = instance.start_instances(self.url, self.verb,
                                        self.headers, self.version, instance_ids)
        if response is not None :
            res = StartInstancesResponse.StartInstancesResponse()
            parseString(str(response.text), res)
            return res
        else :
            return None

    def reboot_instances(self, instance_ids):
        """
        Reboot instances in your account

        param args: Arguments passed to the function

        The function expects one or more instances to
        be rebooted.
        """
        response = instance.reboot_instances(self.url, self.verb,
                                         self.headers, self.version, instance_ids)
        if response is not None :
            res = RebootInstancesResponse.RebootInstancesResponse()
            parseString(str(response.text), res)
            return res
        else :
            return None

    def terminate_instances(self, instance_ids):
        """
        Terminate instances in your account

        param args: Arguments passed to the function

        The function expects one or more instances to
        be terminated.
        """
        response = instance.terminate_instances(self.url, self.verb,
                                            self.headers, self.version,
                                            args)
        if response is not None :
            res = TerminateInstancesResponse.TerminateInstancesResponse()
            parseString(str(response.text), res)
            return res
        else :
            return None

    def get_password_data(self, instance_id, private_key_file = None, passphrase = None):
        """
        Get password for instance in your account. You 
        need to also provide the private key file to 
        get unencrypted password data.

        param args: Arguments passed to the function

        The function expects the following as input 
        1. Instance id
        2. Private key file path (Optional)
        3. Passphrase (incase one is set for the key file)
        """
        response = instance.get_password_data(self.url, self.verb,
                                          self.headers, self.version,
                                          instance_id)
        if response is not None :
            res = GetPasswordDataResponse.GetPasswordDataResponse()
            parseString(str(response.text), res)
            if not private_key_file == None :
                res.password_data = utils.decrypt_instance_password(res.password_data, private_key_file, passphrase)
            return res
        else :
            return None

    def describe_instance_types(self, instance_type_ids = None):
        """
        Gives a description of instance types present.

        param args: Arguments passed to the function

        The function expects either no input or a list of 
        specific instance types to describe
        """
        response = instance.describe_instance_types(self.url, self.verb,
                                                self.headers,
                                                self.version, instance_type_ids)
        if response is not None :
            res = DescribeInstanceTypesResponse.DescribeInstanceTypesResponse()
            parseString(str(response.text), res)
            return res
        else :
            return None

    def run_instances(self, image_id, instance_type_id, blocks = None, instance_count = -1, subnet_id = "", 
    private_ip_address = "", security_group_ids = None, key_name = ""):
        """
        Launch specified number of instances in your
        account.

        param args: Arguments passed to the function

        The function expects following arguments -
        1. image id
        2. instance type id
        3. subnet id (optional)
        4. security group id (optional)
        5. key name (optional, but needed to access machine)
        6. instance count (optional)
        7. private ip address (optional)
        8. block device mapping (optional)
        """
        response = instance.run_instances(self.url, self.verb, self.headers,
                                      self.version, image_id, instance_type_id, blocks, instance_count, subnet_id, private_ip_address, security_group_ids, key_name)
        if response is not None :
            res = RunInstancesResponse.RunInstancesResponse()
            parseString(str(response.text), res)
            return res
        else :
            return None

    def attach_volume(self, instance_id, volume_id, device):
        """
        Attach volume to given instance using particular device name
        to be used by the instance.

        param args: Arguments passed to the function

        The functions expects the following arguments -
        1. Instance Id
        2. Volume Id
        3. Device name
        """
        response = volume.attach_volume(self.url, self.verb, self.headers,
                                    self.version, instance_id, volume_id, device)
        if response is not None :
            res = AttachVolumeResponse.AttachVolumeResponse()
            parseString(str(response.text), res)
            return res
        else :
            return None

    def detach_volume(self, volume_id, instance_id = ""):
        """
        Detach volume from given instance.

        param args: Arguments passed to the function

        The functions expects the following arguments -
        1. Volume Id
        2. Instance Id (optional)
        3. Force (optional)
        """
        response = volume.detach_volume(self.url, self.verb, self.headers,
                                    self.version, volume_id, instance_id)
        if response is not None :
            res = DetachVolumeResponse.DetachVolumeResponse()
            parseString(str(response.text), res)
            return res
        else :
            return None

    def show_delete_on_termination_flag(self, volume_id):
        """
        View the status of the DeleteOnTermination property for a volume
        that is attached to an instance.

        param args: Arguments passed to the function

        The functions expects the Volume Id in arguments
        """
        response = volume.show_delete_on_termination_flag(self.url,
                                       self.verb, self.headers,
                                       self.version, volume_id)
        if response is not None :
            res = ShowDeleteOnTerminationFlagResponse.ShowDeleteOnTerminationFlagResponse()
            parseString(str(response.text), res)
            return res
        else :
            return None

    def update_delete_on_termination_flag(self, volume_id, delete_on_termination):
        """
        Update the status of the DeleteOnTermination property for a
        volume that is attached to an instance.

        param args: Arguments passed to the function

        The functions expects the following arguments -
        1. Volume Id
        2. Delete on termination flag as bool
        """
        response = volume.update_delete_on_termination_flag(self.url,
                                         self.verb, self.headers,
                                         self.version, volume_id, delete_on_termination)
        if response is not None :
            res = UpdateDeleteOnTerminationFlagResponse.UpdateDeleteOnTerminationFlagResponse()
            parseString(str(response.text), res)
            return res
        else :
            return None

    def create_volume(self, snapshot_id = "", size = -1):
        """
        Create a new volume which can be attached to an instance.
        This volume can be created empty or from an existing 
        snapshot.

        param args: Arguments passed to the function

        The function expects either of the following -
        1. Size as integer (for empty volume)
        2. Snapshot Id
        """
        response = volume.create_volume(self.url, self.verb,
                                    self.headers, self.version,
                                    snapshot_id, size)
        if response is not None :
            res = CreateVolumeResponse.CreateVolumeResponse()
            parseString(str(response.text), res)
            return res
        else :
            return None

    def delete_volume(self, volume_id):
        """
        Delete an existing and available volume. The volume
        should be in 'available' state to delete.

        param args: Arguments passed to the function

        The function expects volume id to be deleted
        """
        response = volume.delete_volume(self.url, self.verb,
                                    self.headers, self.version,
                                    volume_id)
        if response is not None :
            res = DeleteVolumeResponse.DeleteVolumeResponse()
            parseString(str(response.text), res)
            return res
        else :
            return None

    def describe_volumes(self, volume_ids = None, max_results = -1, next_token = "", detail = True):
        """
        Get a detailed list of volumes in your account

        param args: Arguments passed to the function

        The function can take following as optional args -
        1. List of volume ids to be described
        2. MaxResults - Max number of results to be shown
        3. NextToken - Id of last volume seen if max number of results
           is less than total volumes.
        4. Detail - by default this is true. Set to false to
           suppress detail
        """
        response = volume.describe_volumes(self.url, self.verb, self.headers, self.version, 
                                volume_ids, max_results, next_token, detail)
        if response is not None :
            res = DescribeVolumesResponse.DescribeVolumesResponse()
            parseString(str(response.text), res)
            return res
        else :
            return None

    def create_snapshot(self, volume_id):
        """
        Create a new snapshot from a existing volume.

        param args: Arguments passed to the function

        The function expects either of the following -
        Volume Id 
        """
        response = snapshot.create_snapshot(self.url, self.verb,
                                    self.headers, self.version,
                                    volume_id)
        
        if response is not None :
            res = CreateSnapshotResponse.CreateSnapshotResponse()
            parseString(str(response.text), res)
            return res
        else :
            return None

    def delete_snapshot(self, snapshot_id):
        """
        Delete an existing and completed snapshot. The snapshot
        should be in 'completed' state to delete.

        param args: Arguments passed to the function

        The function expects snapshot id to be deleted
        """
        response = snapshot.delete_snapshot(self.url, self.verb,
                                    self.headers, self.version,
                                    snapshot_id)
        if response is not None :
            res = DeleteSnapshotResponse.DeleteSnapshotResponse()
            parseString(str(response.text), res)
            return res
        else :
            return None

    def describe_snapshots(self, snpashot_ids = None, max_results = -1, next_token = "", detail = True):
        """
        Get a detailed list of snapshots in your account

        param args: Arguments passed to the function

        The function can take following as optional args -
        1. List of snapshot ids to be described
        2. MaxResults - Max number of results to be shown
        3. NextToken - Id of last snapshot seen if max number of results
           is less than total volumes.
        4. Detail - by default this is true. Set to false to
           suppress detail
        """
        response = snapshot.describe_snapshots(self.url, self.verb, self.headers, self.version,
                                    snpashot_ids, max_results, next_token, detail)
        if response is not None :
            res = DescribeSnapshotsResponse.DescribeSnapshotsResponse() 
            parseString(str(response.text), res)
            return res
        else :
            return None