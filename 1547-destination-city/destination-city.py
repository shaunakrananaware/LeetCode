class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        outgoing = set()
        all_cities = set()

        for cities in paths:
            outgoing.add(cities[0])
            for city in cities: all_cities.add(city)

        return all_cities.difference(outgoing).pop()
        