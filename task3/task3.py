import json
import sys

def load_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        return data

def update_values(tests, values):

    for test in tests:
        test_id = None
        test_id = test['id']
        for v in values['values']:
            if v['id'] == test_id:
                test['value'] = v['value']
        if 'values' in test:
            update_values(test['values'], values)

def write_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

if __name__ == "__main__":
    if len(sys.argv) != 4:
            print("Usage: python program.py values_file_path tests_file_path report_file_path")
            sys.exit(1)

    values_file_path = sys.argv[1]
    tests_file_path = sys.argv[2]
    report_file_path = sys.argv[3]
    # values_file_path = 'values.json'
    # tests_file_path = 'tests.json'
    # report_file_path = 'report.json'

    values_data = load_json(values_file_path)
    tests_data = load_json(tests_file_path)

    update_values(tests_data['tests'], values_data)

    write_json(tests_data, report_file_path)