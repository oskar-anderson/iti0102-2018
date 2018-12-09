"""Retrieve stops and departures info from REST service."""
import requests

API_BASE = "https://public-transport-api.herokuapp.com"
REGION = "tallinn"


def get_nearby_stops(api_base, lat, lng):
    """
    Get nearby stops.

    :param api_base: Base URL that the endpoint gets appended to
    :param lat: Latitude
    :param lng: Longitude
    :return: List of all nearby stops
    """
    final_url = f"{api_base}/stops/{lat}/{lng}"
    list_of_stops = requests.get(final_url).json()
    return sorted(list_of_stops, key=lambda k: (len(k["distance"]), k["distance"]))


def get_nearest_stop(api_base, lat, lng):
    """
    Get nearest stop.

    :param api_base: Base URL that the endpoint gets appended to
    :param lat: Latitude
    :param lng: Longitude
    :return: Nearest stop
    """
    final_url = f"{api_base}/stops/{lat}/{lng}"
    list_of_stops = requests.get(final_url).json()
    try:
        return sorted(list_of_stops, key=lambda k: (len(k["distance"]), k["distance"]))[0]
    except IndexError:
        return None


def get_next_departures(api_base, region, stop_id):
    """
    Get next departures from stop.

    :param api_base: Base URL that the endpoint gets appended to
    :param region: Region
    :param stop_id: Stop ID
    :return: List of next departures from stop
    """
    final_url = f"{api_base}/departures/{region}/{stop_id}"
    list_of_stops = requests.get(final_url).json()["departures"]
    return list_of_stops


def get_next_departure(api_base, region, stop_id):
    """
    Get next departure from stop.

    :param api_base: Base URL that the endpoint gets appended to
    :param region: Region
    :param stop_id: Stop ID
    :return: Next departure from stop
    """
    final_url = f"{api_base}/departures/{region}/{stop_id}"
    list_of_stops = requests.get(final_url).json()["departures"]
    try:
        return sorted(list_of_stops, key=lambda k: k["remainingMinutes"])[0]
    except IndexError:
        return None


if __name__ == '__main__':
    print(get_nearest_stop(API_BASE, 59.3968083, 24.6625157))
    print(get_nearby_stops(API_BASE, 59.3977111, 24.660198))
    print(get_nearest_stop(API_BASE, 59.3977111, 24.660198))
    print(get_next_departures(API_BASE, REGION, get_nearest_stop(API_BASE, 59.3977111, 24.660198)["id"]))
    print(get_next_departure(API_BASE, REGION, get_nearest_stop(API_BASE, 59.3977111, 24.660198)["id"]))
