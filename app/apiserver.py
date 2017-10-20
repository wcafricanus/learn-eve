import json

import requests
from eve import Eve
from app import app


def on_insert_testdata_callback(items):
    for item in items:
        test = item['test']
        patient_info = test['patientInfo']
        vas_cog_block = test['vasCogBlock']
        response = requests.post('http://127.0.0.1:5001/mark', json=vas_cog_block)
        item['result'] = json.loads(response.text)
        item['patient_id'] = patient_info['patientId']
        item['patient_name'] = patient_info['patientName']
    print(item['result'])


class ApiServer(Eve):
    def configure(self):
        self.on_insert_testdata += on_insert_testdata_callback


@app.route('/data_migration')
def data_migration():
    pass
