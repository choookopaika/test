import sys
import json

values_file, tests_file, report_file = sys.argv[1:4]

def fill_values(tests, values_map):
  for test in tests:
    test_id = test.get("id")
    if test_id in values_map:
      test["value"] = values_map[test_id]
    if "values" in test:
      fill_values(test["values"], values_map)

with open(values_file, "r") as values_f:
  values_data = json.load(values_f)

with open(tests_file, "r") as tests_f:
  tests_data = json.load(tests_f)

values_map = {item["id"]: item["value"] for item in values_data["values"]}

fill_values(tests_data["tests"], values_map)

with open(report_file, "w") as report_f:
  json.dump(tests_data, report_f, indent=2, ensure_ascii=False)