import pytest
import requests
from unittest.mock import patch



url = "http://127.0.0.1:5000/expenses"

def fetch_data(url):
	response = requests.get(url)
	response.raise_for_status()
	return response.json()


def test_fetch_data():

	url = "http://127.0.0.1:5000/expenses"
	data =  fetch_data(url)
	
	assert data['expenses'][0]["amount"] == 10.5


@patch('requests.get')
def test_fetch_data_mocked(mock_get):
	"""Test the fetch_data function with mocking"""
	mock_get.return_value.json.return_value = {"amount":10.5,"date":"2023-11-01","description":"Lunch"}

	url = "http://127.0.0.1:5000/expenses"
	data = fetch_data(url)
	assert data["description"] == "Lunch"
	assert data["date"] == "2023-11-01"
	mock_get.assert_called_once_with(url)

