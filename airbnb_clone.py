"""
This module defines functions for managing listings in a basic Airbnb clone.

It provides functionalities for creating, viewing, updating, and deleting listings.
"""


def create_listing(title, description, price, location):
    """
    Creates a new listing with the specified details.

    Args:
        title (str): The title of the listing.
        description (str): A description of the listing.
        price (float): The price of the listing per night.
        location (str): The location of the listing.

    Returns:
        dict: A dictionary containing the listing details.
    """

    listing = {
        "title": title,
        "description": description,
        "price": price,
        "location": location,
    }
    return listing


def show_listing(listings, listing_id):
    """
    Retrieves and displays information about a specific listing by its ID.

    Args:
        listings (list): A list of dictionaries representing listings.
        listing_id (int): The ID of the listing to display.

    Returns:
        None
    """

    for listing in listings:
        if listing["id"] == listing_id:
            print(f"Title: {listing['title']}")
            print(f"Description: {listing['description']}")
            print(f"Price: ${listing['price']:.2f} per night")
            print(f"Location: {listing['location']}")
            return

    print(f"Listing with ID {listing_id} not found.")


def main():
    """
    The main function serves as the entry point for the application.

    It creates a sample list of listings and provides a menu for interaction.
    """

    listings = [
        create_listing("Cozy Beachfront Apartment", "...", 100.00, "Miami, FL"),
        create_listing("Spacious City Loft", "...", 150.00, "New York, NY"),
    ]

    while True:
        print("\nAirbnb Clone (Command Menu):")
        print("1. Create Listing")
        print("2. Show Listing")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            title = input("Enter listing title: ")
            description = input("Enter listing description: ")
            price = float(input("Enter listing price per night: "))
            location = input("Enter listing location: ")
            new_listing = create_listing(title, description, price, location)
            listings.append(new_listing)
            print("Listing created successfully!")

        elif choice == "2":
            listing_id = int(input("Enter listing ID: "))
            show_listing(listings, listing_id)

        elif choice == "3":
            print("Exiting application...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

