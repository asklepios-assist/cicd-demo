"""
Unit tests for the Flask API.
CI will run these automatically on every push.
"""

import pytest
from app import app


@pytest.fixture
def client():
    """Create a test client."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home(client):
    """Test the home endpoint."""
    response = client.get("/")
    data = response.get_json()
    assert response.status_code == 200
    assert data["message"] == "Hello from CI/CD demo!"
    assert data["status"] == "running"


def test_health(client):
    """Test the health endpoint."""
    response = client.get("/health")
    data = response.get_json()
    assert response.status_code == 200
    assert data["status"] == "healthy"


def test_add(client):
    """Test the add endpoint."""
    response = client.get("/add/3/5")
    data = response.get_json()
    assert response.status_code == 200
    assert data["result"] == 8


def test_add_zero(client):
    """Test add with zero."""
    response = client.get("/add/0/7")
    data = response.get_json()
    assert response.status_code == 200
    assert data["result"] == 7


def test_add_large(client):
    """Test add with large numbers."""
    response = client.get("/add/999/1")
    data = response.get_json()
    assert response.status_code == 200
    assert data["result"] == 1000
