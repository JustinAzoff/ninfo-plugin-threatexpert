from ninfo import PluginBase

class threatexpert_plug(PluginBase):
    """ThreatExpert hash lookup"""
    name          = 'threatexpert'
    title         = 'Threatexpert'
    description   = 'ThreatExpert hash lookup'
    cache_timeout = 60*60
    types         = ['hash']

    def setup(self):
        import requests
        self.get = requests.get

    def get_info(self, arg):
        url = "http://www.threatexpert.com/report.aspx?md5=%s" % arg
        r = self.get(url, allow_redirects=False)

        hit = r.status_code == 200

        return {
            "hit": hit,
            "url": url
        }

plugin_class = threatexpert_plug
