# -*- coding: utf-8 -*-

from ..fetchers import NUDHCPOptionsFetcher
from ..fetchers import NUPolicyDecisionsFetcher
from ..fetchers import NUQosPrimitivesFetcher
from ..fetchers import NUStatisticssFetcher
from ..fetchers import NUTCAsFetcher
from ..fetchers import NUPolicyGroupsFetcher
from ..fetchers import NUVPortTagsFetcher

from restnuage import NURESTObject


class NUBridgeInterface(NURESTObject):
    """ Represents a BridgeInterface object """

    def __init__(self):
        """ Initializing object """

        super(NUBridgeInterface, self).__init__()

        # Read/Write Attributes
        
        self.associated_floating_ip_address = None
        self.name = None
        self.attached_network_id = None
        self.attached_network_type = None
        self.domain_id = None
        self.domain_name = None
        self.gateway = None
        self.netmask = None
        self.network_name = None
        self.policy_decision_id = None
        self.v_port_id = None
        self.v_port_name = None
        self.zone_id = None
        self.zone_name = None
        
        self.expose_attribute(local_name=u"associated_floating_ip_address", remote_name=u"associatedFloatingIPAddress", attribute_type=str)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=str)
        self.expose_attribute(local_name=u"attached_network_id", remote_name=u"attachedNetworkID", attribute_type=str)
        self.expose_attribute(local_name=u"attached_network_type", remote_name=u"attachedNetworkType", attribute_type=str)
        self.expose_attribute(local_name=u"domain_id", remote_name=u"domainID", attribute_type=str)
        self.expose_attribute(local_name=u"domain_name", remote_name=u"domainName", attribute_type=str)
        self.expose_attribute(local_name=u"gateway", remote_name=u"gateway", attribute_type=str)
        self.expose_attribute(local_name=u"netmask", remote_name=u"netmask", attribute_type=str)
        self.expose_attribute(local_name=u"network_name", remote_name=u"networkName", attribute_type=str)
        self.expose_attribute(local_name=u"policy_decision_id", remote_name=u"policyDecisionID", attribute_type=str)
        self.expose_attribute(local_name=u"v_port_id", remote_name=u"VPortID", attribute_type=str)
        self.expose_attribute(local_name=u"v_port_name", remote_name=u"VPortName", attribute_type=str)
        self.expose_attribute(local_name=u"zone_id", remote_name=u"zoneID", attribute_type=str)
        self.expose_attribute(local_name=u"zone_name", remote_name=u"zoneName", attribute_type=str)

        # Fetchers
        
        self.dhcpoptions = []
        self._dhcpoptions_fetcher = NUDHCPOptionsFetcher.fetcher_with_entity(entity=self, local_name=u"dhcpoptions")
        
        self.policydecisions = []
        self._policydecisions_fetcher = NUPolicyDecisionsFetcher.fetcher_with_entity(entity=self, local_name=u"policydecisions")
        
        self.qos = []
        self._qos_fetcher = NUQosPrimitivesFetcher.fetcher_with_entity(entity=self, local_name=u"qos")
        
        self.statistics = []
        self._statistics_fetcher = NUStatisticssFetcher.fetcher_with_entity(entity=self, local_name=u"statistics")
        
        self.tcas = []
        self._tcas_fetcher = NUTCAsFetcher.fetcher_with_entity(entity=self, local_name=u"tcas")
        
        self.policygroups = []
        self._policygroups_fetcher = NUPolicyGroupsFetcher.fetcher_with_entity(entity=self, local_name=u"policygroups")
        
        self.redirectiontargets = []
        self._redirectiontargets_fetcher = NUVPortTagsFetcher.fetcher_with_entity(entity=self, local_name=u"redirectiontargets")
        

    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"bridgeinterface"

    # REST methods
    
    def create_dhcpoption(self, dhcpoption, async=False, callback=None):
        """ Create a dhcpoption
            :param dhcpoption: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=dhcpoption, async=async, callback=callback)

    def delete_dhcpoption(self, dhcpoption, async=False, callback=None):
        """ Removes a dhcpoption
            :param dhcpoption: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=dhcpoption, async=async, callback=callback)

    def fetch_dhcpoptions(self, filter=None, page=None, order_by=None):
        """ Fetch DHCPOptions """

        if order_by:
            self._dhcpoptions_fetcher.order_by = order_by

        return self._dhcpoptions_fetcher.fetch_matching_entities(filter=filter, page=page)
    
    def create_policydecision(self, policydecision, async=False, callback=None):
        """ Create a policydecision
            :param policydecision: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=policydecision, async=async, callback=callback)

    def delete_policydecision(self, policydecision, async=False, callback=None):
        """ Removes a policydecision
            :param policydecision: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=policydecision, async=async, callback=callback)

    def fetch_policydecisions(self, filter=None, page=None, order_by=None):
        """ Fetch PolicyDecisions """

        if order_by:
            self._policydecisions_fetcher.order_by = order_by

        return self._policydecisions_fetcher.fetch_matching_entities(filter=filter, page=page)
    
    def create_qo(self, qo, async=False, callback=None):
        """ Create a qo
            :param qo: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=qo, async=async, callback=callback)

    def delete_qo(self, qo, async=False, callback=None):
        """ Removes a qo
            :param qo: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=qo, async=async, callback=callback)

    def fetch_qos(self, filter=None, page=None, order_by=None):
        """ Fetch QosPrimitives """

        if order_by:
            self._qos_fetcher.order_by = order_by

        return self._qos_fetcher.fetch_matching_entities(filter=filter, page=page)
    
    def create_statistic(self, statistic, async=False, callback=None):
        """ Create a statistic
            :param statistic: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=statistic, async=async, callback=callback)

    def delete_statistic(self, statistic, async=False, callback=None):
        """ Removes a statistic
            :param statistic: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=statistic, async=async, callback=callback)

    def fetch_statistics(self, filter=None, page=None, order_by=None):
        """ Fetch Statisticss """

        if order_by:
            self._statistics_fetcher.order_by = order_by

        return self._statistics_fetcher.fetch_matching_entities(filter=filter, page=page)
    
    def create_tca(self, tca, async=False, callback=None):
        """ Create a tca
            :param tca: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=tca, async=async, callback=callback)

    def delete_tca(self, tca, async=False, callback=None):
        """ Removes a tca
            :param tca: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=tca, async=async, callback=callback)

    def fetch_tcas(self, filter=None, page=None, order_by=None):
        """ Fetch TCAs """

        if order_by:
            self._tcas_fetcher.order_by = order_by

        return self._tcas_fetcher.fetch_matching_entities(filter=filter, page=page)
    
    def create_policygroup(self, policygroup, async=False, callback=None):
        """ Create a policygroup
            :param policygroup: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=policygroup, async=async, callback=callback)

    def delete_policygroup(self, policygroup, async=False, callback=None):
        """ Removes a policygroup
            :param policygroup: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=policygroup, async=async, callback=callback)

    def fetch_policygroups(self, filter=None, page=None, order_by=None):
        """ Fetch PolicyGroups """

        if order_by:
            self._policygroups_fetcher.order_by = order_by

        return self._policygroups_fetcher.fetch_matching_entities(filter=filter, page=page)
    
    def create_redirectiontarget(self, redirectiontarget, async=False, callback=None):
        """ Create a redirectiontarget
            :param redirectiontarget: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=redirectiontarget, async=async, callback=callback)

    def delete_redirectiontarget(self, redirectiontarget, async=False, callback=None):
        """ Removes a redirectiontarget
            :param redirectiontarget: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=redirectiontarget, async=async, callback=callback)

    def fetch_redirectiontargets(self, filter=None, page=None, order_by=None):
        """ Fetch VPortTags """

        if order_by:
            self._redirectiontargets_fetcher.order_by = order_by

        return self._redirectiontargets_fetcher.fetch_matching_entities(filter=filter, page=page)
    