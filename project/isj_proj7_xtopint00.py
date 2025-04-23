from collections import UserDict
import bisect

class TimeSeriesDB(UserDict):

    def __init__(self):

        super().__init__()

    def __setitem__(self, key, data):

        if isinstance(key, str) and isinstance(data, tuple):

            timestamp, value = data

            if key not in self.data:

                self.data[key] = []

            self.data[key].append((timestamp, value))

        else:

            raise ValueError("ERROR: Invalid format for data insertion")

    def __getitem__(self, key):

        if isinstance(key, tuple) and len(key) == 2:

            key_name, timestamp = key

            if key_name not in self.data:

                return None

            records = self.data[key_name]

            timestamps = [ts for ts, _ in records]

            index = bisect.bisect_right(timestamps, timestamp) - 1

            if index >= 0:

                return records[index][1]

            else:

                return None

        elif isinstance(key, str):

            if key not in self.data or not self.data[key]:

                return None

            return self.data[key][-1][1]

        else:

            raise ValueError("ERROR: Invalid format for data getting")

def test():

    time_db = TimeSeriesDB()

    time_db['vibr'] = (1, 'low')

    time_db['vibr'] = (5, 'mid')

    time_db['vibr'] = (8, 'low')

    time_db['vibr'] = (12, 'high')

    time_db['temp'] = (2, 37.6)

    time_db['temp'] = (4, 37.2)

    time_db['temp'] = (17, 37.7)


    assert time_db[('vibr', 1)] == 'low'

    assert time_db[('vibr', 4)] == 'low'

    assert time_db[('vibr', 7)] == 'mid'

    assert time_db['temp'] == 37.7


if __name__ == '__main__':
    test()