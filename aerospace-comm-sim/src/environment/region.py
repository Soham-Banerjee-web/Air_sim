class Region:
    def __init__(self, name, boundaries):
        self.name = name
        self.boundaries = boundaries  # boundaries should be defined as a tuple (min_lat, max_lat, min_lon, max_lon)

    def is_within_bounds(self, latitude, longitude):
        min_lat, max_lat, min_lon, max_lon = self.boundaries
        return min_lat <= latitude <= max_lat and min_lon <= longitude <= max_lon

    def __repr__(self):
        return f"Region(name={self.name}, boundaries={self.boundaries})"