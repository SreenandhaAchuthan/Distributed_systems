import xmlrpc.client
from datetime import datetime, timezone

# Connect to RPC server
proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

# Get service input
dob = input("Enter your Date of Birth (YYYY-MM-DD): ")

# Intentionally incorrect dummy timestamp
client_time = 946684800.0

print("\nSending request with incorrect client time...")

while True:

    # Send RPC request
    response = proxy.calculate_age(dob, client_time)

    if response["status"] == "REJECTED":

        print("\nSERVER NOTIFICATION:")
        print(response["message"])

        # Receive correct server time
        server_time = response["server_time"]

        correct_time = datetime.fromtimestamp(
            server_time, timezone.utc
        )

        print("Correct Server Time:", correct_time)

        # Update client timestamp
        client_time = server_time

        print("\nClient time updated successfully.")
        print("Resending request...")

    elif response["status"] == "SUCCESS":

        print("\nSERVER RESPONSE:")
        print(response["message"])
        print("Calculated Age:", response["age"])
        break

    else:
        print("\nError:", response["message"])
        break