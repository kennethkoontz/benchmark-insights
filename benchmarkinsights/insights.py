import numpy as np


class Stats(object):
    def __init__(self, data):
        self.data = data


class FacebookStats(Stats):
    @property
    def likes(self):
        likes = [i.likes for i in self.data]
        return {'average': round(np.average(likes), 1),
                'total': np.sum(likes)}

    @property
    def checkin_count(self):
        checkin_count = [i.checkin_count for i in self.data]
        return {'average': round(np.average(checkin_count), 1),
                'total': np.sum(checkin_count)}

    @property
    def people_talking(self):
        people_talking = [i.people_talking for i in self.data]
        return {'average': round(np.average(people_talking), 1),
                'total': np.sum(people_talking)}


class YelpStats(Stats):
    @property
    def rating(self):
        rating = [i.rating for i in self.data]
        return {'average': np.average(rating)}

    @property
    def rating_count(self):
        rating_count = [i.rating_count for i in self.data]
        return {'average': round(np.average(rating_count), 1),
                'total': np.sum(rating_count)}


class GoogleStats(Stats):
    @property
    def rating(self):
        rating = [i.rating for i in self.data]
        return {'average': round(np.average(rating), 1)}

    @property
    def rating_count(self):
        rating_count = [i.rating_count for i in self.data]
        return {'average': round(np.average(rating_count), 1),
                'total': np.sum(rating_count)}


class FoursquareStats(Stats):
    @property
    def rating(self):
        rating = [i.rating for i in self.data]
        return {'average': round(np.average(rating), 1)}

    @property
    def checkin_count(self):
        checkin_count = [i.checkin_count for i in self.data]
        return {'average': round(np.average(checkin_count), 1),
                'total': np.sum(checkin_count)}

    @property
    def likes(self):
        likes = [i.likes for i in self.data]
        return {'average': round(np.average(likes), 1),
                'total': np.sum(likes)}

    @property
    def user_count(self):
        user_count = [i.user_count for i in self.data]
        return {'average': round(np.average(user_count), 1),
                'total': np.sum(user_count)}

    @property
    def tip_count(self):
        tip_count = [i.tip_count for i in self.data]
        return {'average': round(np.average(tip_count), 1),
                'total': np.sum(tip_count)}
