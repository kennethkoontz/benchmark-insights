import numpy as np

STAT_ATTRS = ['likes',
              'checkin_count',
              'people_talking',
              'rating',
              'rating_count',
              'user_count',
              'tip_count']


class Stats(object):
    def __init__(self, data):
        self.data = data

    @property
    def stats(self):
        stats = {}
        for attr in dir(self):
            if attr in STAT_ATTRS:
                stats[attr] = getattr(self, attr)
        return stats


class FacebookStats(Stats):
    @property
    def likes(self):
        likes = [i.get('likes') for i in self.data]
        return {'average': round(np.average(likes), 1),
                'total': np.sum(likes)}

    @property
    def checkin_count(self):
        checkin_count = [i.get('checkin_count') for i in self.data]
        return {'average': round(np.average(checkin_count), 1),
                'total': np.sum(checkin_count)}

    @property
    def people_talking(self):
        people_talking = [i.get('people_talking') for i in self.data]
        return {'average': round(np.average(people_talking), 1),
                'total': np.sum(people_talking)}


class YelpStats(Stats):
    @property
    def rating(self):
        rating = [i.get('rating') for i in self.data]
        return {'average': round(np.average(rating), 1)}

    @property
    def rating_count(self):
        rating_count = [i.get('rating_count') for i in self.data]
        return {'average': round(np.average(rating_count), 1),
                'total': np.sum(rating_count)}


class GoogleStats(Stats):
    @property
    def rating(self):
        rating = [i.get('rating') for i in self.data]
        return {'average': round(np.average(rating), 1)}

    @property
    def rating_count(self):
        rating_count = [i.get('rating_count') for i in self.data]
        return {'average': round(np.average(rating_count), 1),
                'total': np.sum(rating_count)}


class FoursquareStats(Stats):
    @property
    def rating(self):
        rating = [i.get('rating') for i in self.data]
        return {'average': round(np.average(rating), 1)}

    @property
    def checkin_count(self):
        checkin_count = [i.get('checkin_count') for i in self.data]
        return {'average': round(np.average(checkin_count), 1),
                'total': np.sum(checkin_count)}

    @property
    def likes(self):
        likes = [i.get('likes') for i in self.data]
        return {'average': round(np.average(likes), 1),
                'total': np.sum(likes)}

    @property
    def user_count(self):
        user_count = [i.get('user_count') for i in self.data]
        return {'average': round(np.average(user_count), 1),
                'total': np.sum(user_count)}

    @property
    def tip_count(self):
        tip_count = [i.get('tip_count') for i in self.data]
        return {'average': round(np.average(tip_count), 1),
                'total': np.sum(tip_count)}
