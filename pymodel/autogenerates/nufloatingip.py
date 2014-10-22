# -*- coding: utf-8 -*-

from ..fetchers import NUVPortsFetcher

from bambou import NURESTObject


class NUFloatingIp(NURESTObject):
    """ Represents a FloatingIp object """

    def __init__(self):
        """ Initializing object """

        super(NUFloatingIp, self).__init__()

        # Read/Write Attributes

        self.address = None
        self.assigned = None
        self.associated_shared_network_resource_id = None

        self.expose_attribute(local_name=u"address", remote_name=u"address", attribute_type=str)
        self.expose_attribute(local_name=u"assigned", remote_name=u"assigned", attribute_type=bool)
        self.expose_attribute(local_name=u"associated_shared_network_resource_id", remote_name=u"associatedSharedNetworkResourceID", attribute_type=str)

        # Fetchers

        self.vports = []
        self._vports_fetcher = NUVPortsFetcher.fetcher_with_entity(entity=self, local_name=u"vports")


    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"floatingip"

    # REST methods

    def create_vport(self, vport, async=False, callback=None):
        """ Create a vport
            :param vport: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=vport, async=async, callback=callback)

    def delete_vport(self, vport, async=False, callback=None):
        """ Removes a vport
            :param vport: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=vport, async=async, callback=callback)

    def fetch_vports(self, filter=None, page=None, order_by=None):
        """ Fetch VPorts """

        if order_by:
            self._vports_fetcher.order_by = order_by

        return self._vports_fetcher.fetch_matching_entities(filter=filter, page=page)