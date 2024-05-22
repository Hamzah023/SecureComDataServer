# httpProtocolRESTfulAPI
HTTP protocol based RESTful protocol that has versioning, throttling/rate limiting using limiters, Oauth setup but mainly Key based authentication

# Flask API with API Key Authentication and Rate Limiting

This project is a Flask-based web API that includes API key authentication and rate limiting features. The API has protected routes that require a valid API key for access and public routes that do not require any authentication. Additionally, rate limiting is applied to the protected routes to prevent abuse and ensure fair usage.

## Features

- **API Key Authentication**: Ensures that only requests with a valid API key can access protected routes.
- **Rate Limiting**: Limits the number of requests a client can make to the API within a specified timeframe to prevent abuse.
- **Versioned Routes**: Supports versioned API routes (v1, v2, etc.) for better API management and versioning.

## Prerequisites

- Python 3.x
- Flask
- Flask-Limiter for throttling
- Marshmallow for data validation
- Flask-OAuthLib for OAuth (Open Authorization)

## Installation

1. **Clone the Repository**:
    ```bash ( i like zsh more)
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2. **Create a Virtual Environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**:
    ```bash
    pip install Flask Flask-Limiter
    ```

## Project Structure
│
├── app/
│ ├── resources/
│     └── get_request_v1.py (has post request too tho)
│     └── get_request_v2.py (has post request too tho)
│ └── __init__.py
│ └── oauth.py
│ └── auth.py
│ └── limiter.py
│ └── schemas.py
├── run.py
└── README.md


