import numpy as np

STAT_ATTRS = ['likes',
              'checkin_count',
              'people_talking',
              'rating',
              'rating_count',
              'user_count',
              'tip_count',
              'checkins_per_user']


def remove_none_values(l):
    return [i for i in l if i is not None]


def get_quality_score(loc):
    """
    G = Google Rating
    FS = Foursquare Rating
    Y = Yelp Rating

    (((G * 2) + FS + (Y * 2)) / 3) * 10

    If source doesn't have a rating, we don't ding the quality score.
    """
    google = (loc.get('latest_summaries', {})
              .get('google', {})
              .get('rating'))
    yelp = (loc.get('latest_summaries', {})
            .get('yelp', {})
            .get('rating'))
    foursquare = (loc.get('latest_summaries', {})
                  .get('foursquare', {})
                  .get('rating'))
    if not google:
        google = 5
    if not yelp:
        yelp = 5
    if not foursquare:
        foursquare = 10

    google *= 2
    yelp *= 2

    return round(((google + yelp + foursquare) / 3) * 10, 2)


def get_location_quality_score(loc):
    """
    G = Google Rating
    FS = Foursquare Rating
    Y = Yelp Rating

    (((G * 2) + FS + (Y * 2)) / 3) * 10
    """
    google = loc.get('google')
    yelp = loc.get('yelp')
    foursquare = loc.get('foursquare')

    if not google:
        google = 5
    if not yelp:
        yelp = 5
    if not foursquare:
        foursquare = 10

    google *= 2
    yelp *= 2

    return round(((google + yelp + foursquare) / 3) * 10, 2)


def get_average_quality_score(locs):
    pass


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

    def sort(self, stat, **kwargs):
        return sorted(self.data, key=lambda item: item[stat], **kwargs)


class FacebookStats(Stats):
    @property
    def likes(self):
        likes = [i.get('likes') for i in self.data]
        likes = remove_none_values(likes)
        return {'average': round(np.average(likes), 1),
                'total': np.sum(likes)}

    @property
    def checkin_count(self):
        checkin_count = [i.get('checkin_count') for i in self.data]
        checkin_count = remove_none_values(checkin_count)
        return {'average': round(np.average(checkin_count), 1),
                'total': np.sum(checkin_count)}

    @property
    def people_talking(self):
        people_talking = [i.get('people_talking') for i in self.data]
        people_talking = remove_none_values(people_talking)
        return {'average': round(np.average(people_talking), 1),
                'total': np.sum(people_talking)}

    @property
    def top_3(self):
        return self.sort('likes', reverse=True)[:3]

    @property
    def bottom_3(self):
        return self.sort('likes')[:3]


class YelpStats(Stats):
    @property
    def rating(self):
        rating = [i.get('rating') for i in self.data]
        rating = remove_none_values(rating)
        return {'average': round(np.average(rating), 1)}

    @property
    def rating_count(self):
        rating_count = [i.get('rating_count') for i in self.data]
        rating_count = remove_none_values(rating_count)
        return {'average': round(np.average(rating_count), 1),
                'total': np.sum(rating_count)}

    @property
    def top_3(self):
        return self.sort('rating', reverse=True)[:3]

    @property
    def bottom_3(self):
        return self.sort('rating')[:3]


class GoogleStats(Stats):
    @property
    def rating(self):
        rating = [i.get('rating') for i in self.data]
        rating = remove_none_values(rating)
        return {'average': round(np.average(rating), 1)}

    @property
    def rating_count(self):
        rating_count = [i.get('rating_count') for i in self.data]
        rating_count = remove_none_values(rating_count)
        return {'average': round(np.average(rating_count), 1),
                'total': np.sum(rating_count)}

    @property
    def top_3(self):
        return self.sort('rating', reverse=True)[:3]

    @property
    def bottom_3(self):
        return self.sort('rating')[:3]


class FoursquareStats(Stats):
    @property
    def rating(self):
        rating = [i.get('rating') for i in self.data]
        rating = remove_none_values(rating)
        return {'average': round(np.average(rating), 1)}

    @property
    def checkin_count(self):
        checkin_count = [i.get('checkin_count') for i in self.data]
        checkin_count = remove_none_values(checkin_count)
        return {'average': round(np.average(checkin_count), 1),
                'total': np.sum(checkin_count)}

    @property
    def likes(self):
        likes = [i.get('likes') for i in self.data]
        likes = remove_none_values(likes)
        return {'average': round(np.average(likes), 1),
                'total': np.sum(likes)}

    @property
    def user_count(self):
        user_count = [i.get('user_count') for i in self.data]
        user_count = remove_none_values(user_count)
        return {'average': round(np.average(user_count), 1),
                'total': np.sum(user_count)}

    @property
    def tip_count(self):
        tip_count = [i.get('tip_count') for i in self.data]
        tip_count = remove_none_values(tip_count)
        return {'average': round(np.average(tip_count), 1),
                'total': np.sum(tip_count)}

    @property
    def checkins_per_user(self):
        checkin_count = self.checkin_count['total']
        user_count = self.user_count['total']
        checkins_per_user = checkin_count / user_count
        return {'average': round(checkins_per_user, 1)}

    @property
    def top_3(self):
        return self.sort('rating', reverse=True)[:3]

    @property
    def bottom_3(self):
        return self.sort('rating')[:3]
