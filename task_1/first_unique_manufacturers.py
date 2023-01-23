#!/usr/bin/env python3
"""
Write a script to connect to the following API ["https://swapi.dev/api/vehicles/"].
Retrieve the JSON data, and list the first 5 unique manufacturers.
"""
from typing import List
import requests

ENDPOINT_URL = "https://swapi.dev/api/vehicles/?page={page_number}"


def first_unique_manufacturers(quantity: int = 5) -> List[str]:
    """
    Retrieve the JSON data, and list the first n unique manufacturers

    :param quantity: Number of unique manufacturers to retrieve

    :return: List of unique manufacturers

    :raises ValueError: If there are less than n unique manufacturers
    """
    page_number = 0
    data_in_page = True
    manufacturers = []

    while data_in_page:
        page_number += 1
        # Retrieve the JSON data from an specific page
        response = requests.get(ENDPOINT_URL.format(page_number=page_number))
        data = response.json()
        for vehicle in data["results"]:
            # Normalize the manufacturer name
            vehicle_manufacturer = vehicle["manufacturer"].title()
            if vehicle_manufacturer not in manufacturers:
                manufacturers.append(vehicle_manufacturer)
                if len(manufacturers) == quantity:
                    return manufacturers
        data_in_page = data["next"]
    # Could not retrieve the requested number of unique manufacturers
    raise ValueError(
        f"There are less than {quantity} unique manufacturers,"
        f" max unique manufacturers: {len(manufacturers)}"
    )


if __name__ == "__main__":
    """
    Main function
    """
    manufacturers = first_unique_manufacturers(5)
    print(manufacturers)
