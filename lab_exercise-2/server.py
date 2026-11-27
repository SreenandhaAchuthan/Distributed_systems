from xmlrpc.server import SimpleXMLRPCServer
from datetime import datetime, timezone

# Server time validation
def validate_time(client_time):
    server_time = datetime.now(timezone.utc).timestamp()

    # Allow 10 seconds of clock difference
    if abs(server_time - client_time) > 10:
        return {
            "status": "REJECTED",
            "message": "Client system time is incorrect!",
            "server_time": server_time
        }

    return {
        "status": "ACCEPTED",
        "message": "Client time is valid."
    }


# Remote service: Calculate age
def calculate_age(dob, client_time):
    validation = validate_time(client_time)

    if validation["status"] == "REJECTED":
        return validation

    try:
        birth_date = datetime.strptime(dob, "%Y-%m-%d").date()
        today = datetime.now(timezone.utc).date()

        if birth_date > today:
            return {
                "status": "ERROR",
                "message": "Date of birth cannot be in the future."
            }

        age = today.year - birth_date.year

        if (today.month, today.day) < (birth_date.month,
                                       birth_date.day):
            age -= 1

        return {
            "status": "SUCCESS",
            "message": "Age calculated successfully.",
            "age": age
        }

    except ValueError:
        return {
            "status": "ERROR",
            "message": "Invalid DOB format. Use YYYY-MM-DD."
        }


# Create RPC server
server = SimpleXMLRPCServer(
    ("localhost", 8000),
    allow_none=True
)

server.register_function(calculate_age, "calculate_age")

print("RPC Server is running on port 8000...")

server.serve_forever()