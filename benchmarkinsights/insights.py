class FacebookInsight(object):
    def __init__(self, data):
        self.data = data

    @property
    def likes(self):
        return {'average': 0,
                'total': 0}

    @property
    def checkins(self):
        return {'average': 0,
                'total': 0}

    @property
    def talking_about(self):
        return {'average': 0,
                'total': 0}
