import requests


def test_simple_benefit_plan():
    endpoint = 'https://boosttest.rxnxt.com/switch-node/json/benefit.get'
    headers = {"Authorization": "Basic d0tvOVhIMjhJOCN0T01xaQ=="}
    params= {
        "test_mode_indicator": "true",
        "bin_number" : "024368",
        "policy_number" : "E51000072",
        "date_of_birth" : "1989-02-24",
        "first_name" : "PATRICK",
        "ncpdp_number": "1140677",
        "package_number": "64380071207",
        "quantity" : "45",
        "days_supply": "7",
        "ingredient_cost": "$102.13",
        "customary_cost" : "$20.89",
        "gross_amount_due_cost": "$104.13",
       }
    response = requests.get(endpoint, headers=headers, params=params)
    resp_json = response.json()
    assert(response.status_code == 200)
    assert(resp_json['result']['costResult']['isPaid'] == True)
    # add assert for amount and message
