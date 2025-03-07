# Description: This file contains the integration tests for the todo app.
import unittest
import requests

url = "https://todo.pixegami.io/"


##########################################
def test_status_code():
   response = requests.get(url)
   assert response.status_code == 200

############################################
def test_create_task():
    paylod = {
        "content": "Get you supplies",
        "user_id": "GT_89",
        "is_done": True
}
    create_task_response = requests.put(url + "/create-task", json=paylod)
    assert create_task_response.status_code == 200 

    new_task = create_task_response.json()
    print(new_task)
    print(paylod["content"])
    print(new_task['task']['content'])
    assert paylod['content'] == new_task['task']['content']


##############################################
def test_find_task():
    task_id = 'task_9f8052c693f049ab8e7a8dd3079d6eaf'
    get_task_response = requests.get(url + f'/get-task/{task_id}')
    assert get_task_response.status_code == 200
    print(get_task_response.json())



#####################################################
def test_update_task():
    
    payload1 = {
        "content": "Get your yesterday supplies",
        "user_id": "ABSDC_89",
        "is_done": True
    }
    create_task_response = requests.put(url + "/create-task", json=payload1)
    assert create_task_response.status_code == 200
    new_task = create_task_response.json()
    print(new_task)

    task_id1 = new_task['task']['task_id']
    user_id1 = new_task['task']['user_id']
    print(task_id1)
    payload2 = {
        "content": "Get youres",
        "user_id": "HAHSJ_89",
        "task_id": task_id1,
        "is_done": True
    }
    test_update_response = requests.put(url + '/update-task', json=payload2)
    assert test_update_response.status_code == 200
    updated  = test_update_response.json()
    print(updated)
    new_task_id = updated['updated_task_id']
    get_task_response = requests.get(url + f'/get-task/{new_task_id}')
    assert get_task_response.status_code == 200
    print(get_task_response.json())





