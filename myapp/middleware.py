from django.http import JsonResponse
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class GraphQLTokenMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # Read from environment variable
        self.secret_token = os.getenv("GRAPHQL_SECRET_TOKEN")
        
        # Add a check so you don't accidentally run without the secret
        if not self.secret_token:
            raise ValueError("GRAPHQL_SECRET_TOKEN environment variable is not set!")

    def __call__(self, request):
        if request.path == "/graphql/":
            auth = request.headers.get("Authorization", "")
            if auth != f"Bearer {self.secret_token}":
                return JsonResponse({"error": "Unauthorized"}, status=401)

        return self.get_response(request)