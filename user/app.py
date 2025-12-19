import json

USERS = [
    {"id": 1, "name": "Rengaraj"},
    {"id": 2, "name": "Sachin"},
    {"id": 3, "name": "Dharshika"},
    {"id": 4, "name": "Surya"},
    {"id": 5, "name": "Harish"},
    {"id": 6, "name": "Akshaya"},
    {"id": 7, "name": "Kanchana"},
    {"id": 8, "name": "Sangeetha"},
    {"id": 9, "name": "Arjun"},
    {"id": 10, "name": "Deva"},
]


def lambda_handler(event, context):
    path = event.get("path")
    params = event.get("pathParameters") or {}

    # GET /users
    if path == "/users":
        return response(200, USERS)

    # GET /users/{id}
    if path.startswith("/users/"):
        user_id = int(params.get("id"))
        user = next((u for u in USERS if u["id"] == user_id), None)

        if not user:
            return response(404, {"message": "User not found"})

        return response(200, user)

    return response(404, {"message": "Not Found"})


def response(status, body):
    return {
        "statusCode": status,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(body)
    }
