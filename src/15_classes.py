# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE

class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    def latty(self):
        print(self.lat, self.lon)

foo = LatLon("IT", "WORKED")
foo.latty()


# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE


class WayPoint(LatLon):
    def __init__(self, name, lat, lon):
        super().__init__(lat, lon)
        self.name = name

    def called(self):
        print(self.name, self.lat, self.lon)
    
    def __str__(self):
        return f'{self.name}, {self.lat}, {self.lon}'

bar = WayPoint(123, 123, 'name')
bar.called()



# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE

class Geocache(WayPoint):
    def __init__(self, difficulty, size, lat, lon, name):
        super().__init__(lat, lon, name)
        self.difficulty = difficulty
        self.size = size

    def callgeo(self):
        print(self.lat, self.lon, self.name, self.difficulty, self.size)

geo = Geocache('difficulty', 'size', 'lat', 'lon', 'name')


# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE

newWay = WayPoint("Catacombs", 41.70505, -121.51521)

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method

print(newWay)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE

geo = Geocache('diff 1.5', 'size 2', '2, 44.052137', '-121.41556', '"Newberry Views"')

# Print it--also make this print more nicely

print(geo)
