import pytest
import unittest
import requests

url = "https:/todo.pixegami.io"

paylod = {
  "content": "Get you supplies",
  "user_id": "GT_89",
  "is_done": True
}
response = requests.get(url)

def test_status_code():
    assert response.status_code == 200

def test_create(create_task):
    create_task_response = requests.put(url + "/create-task", json=create_task())
    assert create_task_response.status_code == 200 
    create_json =  create_task_response.json()
    print(create_json)
    assert paylod["content"] == create_task_response.json()["content"]

def test_get_task():
    task_id = ""
    get_task_response = requests.get(url + f"/get-task/{task_id}")
    assert get_task_response.status_code == 200

def create_task():
    return paylod