import requests
import json

# Function to get available lists
def get_lists(access_token):
    url = "https://api.umbrella.com/policies/v2/destinationlists"
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()['data']
    else:
        print(f"Error retrieving lists: {response.status_code}")
        return []

# Function to get domains/URLs in a specific list
def get_destinations(access_token, list_id):
    url = f"https://api.umbrella.com/policies/v2/destinationlists/{list_id}/destinations"
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()['data']
    else:
        print(f"Error retrieving destinations for list {list_id}: {response.status_code}")
        return []

# Function to delete domains/URLs from a specific list
def delete_destinations(access_token, list_id, destination_ids):
    url = f"https://api.umbrella.com/policies/v2/destinationlists/{list_id}/destinations/remove"
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    payload = json.dumps(destination_ids)
    response = requests.request("DELETE", url, headers=headers, data=payload)
    return response.status_code, response.text

def main():
    # Import your token from another file
    from adminToken import access_token

    # Step 1: Retrieve lists
    lists = get_lists(access_token)
    if not lists:
        print("No lists were found.")
        return

    while True:
        # Step 2: Display the lists to the user
        print("\nAvailable lists:")
        for i, lst in enumerate(lists, start=1):
            print(f"{i}. {lst['name']} (ID: {lst['id']})")

        # Step 3: Ask the user to select a list
        try:
            option = int(input("\nChoose the number of the list from which you want to delete domains or IPs: ")) - 1
            if option < 0 or option >= len(lists):
                print("Invalid option.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue

        selected_list = lists[option]
        list_id = selected_list['id']
        print(f"\nYou have selected the list: {selected_list['name']} (ID: {list_id})")

        # Step 4: Retrieve destinations from the selected list
        destinations = get_destinations(access_token, list_id)
        if not destinations:
            print(f"No domains or IPs found in the list {selected_list['name']}.")
            continue

        print("\nDomains/URLs in the selected list:")
        for i, destination in enumerate(destinations, start=1):
            print(f"{i}. {destination['destination']} (ID: {destination['id']})")

        while True:
            # Step 5: Ask the user to select domains/URLs to delete
            ids_to_delete = input("\nEnter the IDs of the domains/URLs you want to delete, separated by commas: ").split(',')
            try:
                ids_to_delete = [int(id.strip()) for id in ids_to_delete if id.strip()]
                if not ids_to_delete:
                    print("You did not enter any valid IDs.")
                    continue
            except ValueError:
                print("Please enter valid numeric IDs.")
                continue

            # Step 6: Delete the selected domains/URLs
            status_code, response_text = delete_destinations(access_token, list_id, ids_to_delete)
            if status_code == 200 or status_code == 204:
                print("\nDomains/URLs successfully deleted!")
            else:
                print(f"\nError deleting domains/URLs: {response_text}")

            # Ask if the user wants to delete more from this list
            continue_option = input("\nDo you want to delete more domains from this list? (yes/no): ").lower()
            if continue_option not in ['yes', 'y']:
                break

        # Ask if the user wants to select another list or exit
        another_list_option = input("\nDo you want to select another list? (yes/no): ").lower()
        if another_list_option not in ['yes', 'y']:
            print("\nExiting the program. Goodbye!")
            break

if __name__ == "__main__":
    main()
