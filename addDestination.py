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

# Function to add domains/IPs to a specific list
def add_destinations(access_token, list_id, destinations):
    url = f"https://api.umbrella.com/policies/v2/destinationlists/{list_id}/destinations"
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    payload = json.dumps([{"destination": destination} for destination in destinations])
    response = requests.post(url, headers=headers, data=payload)
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
            option = int(input("\nChoose the number of the list to which you want to add domains or IPs: ")) - 1
            if option < 0 or option >= len(lists):
                print("Invalid option.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue

        selected_list = lists[option]
        list_id = selected_list['id']
        print(f"\nYou have selected the list: {selected_list['name']} (ID: {list_id})")

        while True:
            # Step 4: Ask the user to input domains/IPs
            destinations = input("Enter the domains or IPs you want to add, separated by commas: ").split(',')

            # Clean the input
            destinations = [destination.strip() for destination in destinations if destination.strip()]
            if not destinations:
                print("You did not enter any valid domain or IP.")
                continue

            # Step 5: Send the domains/IPs to the API
            status_code, response_text = add_destinations(access_token, list_id, destinations)
            if status_code == 200 or status_code == 201:
                print("\nDomains/IPs successfully added!")
            else:
                print(f"\nError adding domains/IPs: {response_text}")

            # Ask if the user wants to add more or exit
            continue_option = input("\nDo you want to add more domains to this list? (yes/no): ").lower()
            if continue_option not in ['yes', 'y']:
                break

        # Ask if the user wants to choose another list or exit
        another_list_option = input("\nDo you want to select another list? (yes/no): ").lower()
        if another_list_option not in ['yes', 'y']:
            print("\nExiting the program. Goodbye!")
            break


if __name__ == "__main__":
    main()