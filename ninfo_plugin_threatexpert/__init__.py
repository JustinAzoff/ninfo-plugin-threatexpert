from ninfo import PluginBase

class threatexpert_plug(PluginBase):
    """ThreatExpert hash lookup"""
    name          = 'threatexpert'
    title         = 'Threatexpert'
    description   = 'ThreatExpert hash lookup'
    cache_timeout = 60*60
    types         = ['ip','ip6','cidr', 'cidr6', 'hostname','username']
    #local        = False
    #remove       = False

    def setup(self):
        pass

    def get_info(self, arg):
        return {}

plugin_class = threatexpert_plug
