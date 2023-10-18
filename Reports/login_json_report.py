[
{
  "elements": [
    {
      "keyword": "Scenario",
      "location": "behave_BDD/loginsteps26/BDD_login.feature:8",
      "name": "Log in with the correct Email and Password",
      "status": "passed",
      "steps": [
        {
          "keyword": "Given",
          "location": "behave_BDD/loginsteps26/BDD_login.feature:10",
          "match": {
            "arguments": [],
            "location": "behave_BDD/loginsteps26/steps/loginsteps1.py:19"
          },
          "name": "user is not logged in",
          "result": {
            "duration": 0.4270768165588379,
            "status": "passed"
          },
          "step_type": "given"
        },
        {
          "keyword": "When",
          "location": "behave_BDD/loginsteps26/BDD_login.feature:11",
          "match": {
            "arguments": [],
            "location": "behave_BDD/loginsteps26/steps/loginsteps1.py:27"
          },
          "name": "user enters correct Email and Password",
          "result": {
            "duration": 0.9083960056304932,
            "status": "passed"
          },
          "step_type": "when"
        },
        {
          "keyword": "And",
          "location": "behave_BDD/loginsteps26/BDD_login.feature:12",
          "match": {
            "arguments": [],
            "location": "behave_BDD/loginsteps26/steps/loginsteps1.py:40"
          },
          "name": "user clicks Login button",
          "result": {
            "duration": 1.1159861087799072,
            "status": "passed"
          },
          "step_type": "when"
        },
        {
          "keyword": "Then",
          "location": "behave_BDD/loginsteps26/BDD_login.feature:13",
          "match": {
            "arguments": [],
            "location": "behave_BDD/loginsteps26/steps/loginsteps1.py:46"
          },
          "name": "user profile is launched",
          "result": {
            "duration": 0.2047591209411621,
            "status": "passed"
          },
          "step_type": "then"
        }
      ],
      "tags": [
        "positive",
        "critical"
      ],
      "type": "scenario"
    },
    {
      "keyword": "Scenario",
      "location": "behave_BDD/loginsteps26/BDD_login.feature:17",
      "name": "Login without entering a Email and Password",
      "status": "passed",
      "steps": [
        {
          "keyword": "Given",
          "location": "behave_BDD/loginsteps26/BDD_login.feature:19",
          "match": {
            "arguments": [],
            "location": "behave_BDD/loginsteps26/steps/loginsteps1.py:19"
          },
          "name": "user is not logged in",
          "result": {
            "duration": 0.41649484634399414,
            "status": "passed"
          },
          "step_type": "given"
        },
        {
          "keyword": "When",
          "location": "behave_BDD/loginsteps26/BDD_login.feature:20",
          "match": {
            "arguments": [],
            "location": "behave_BDD/loginsteps26/steps/loginsteps1.py:40"
          },
          "name": "user clicks Login button",
          "result": {
            "duration": 0.6735379695892334,
            "status": "passed"
          },
          "step_type": "when"
        },
        {
          "keyword": "Then",
          "location": "behave_BDD/loginsteps26/BDD_login.feature:21",
          "match": {
            "arguments": [],
            "location": "behave_BDD/loginsteps26/steps/loginsteps1.py:55"
          },
          "name": "warning shown about 'No match for E-Mail Address and/or Password'",
          "result": {
            "duration": 0.049944162368774414,
            "status": "passed"
          },
          "step_type": "then"
        }
      ],
      "tags": [
        "negative",
        "major"
      ],
      "type": "scenario"
    },
    {
      "keyword": "Scenario",
      "location": "behave_BDD/loginsteps26/BDD_login.feature:24",
      "name": "Login without entering a Password",
      "status": "passed",
      "steps": [
        {
          "keyword": "Given",
          "location": "behave_BDD/loginsteps26/BDD_login.feature:26",
          "match": {
            "arguments": [],
            "location": "behave_BDD/loginsteps26/steps/loginsteps1.py:19"
          },
          "name": "user is not logged in",
          "result": {
            "duration": 0.4235877990722656,
            "status": "passed"
          },
          "step_type": "given"
        },
        {
          "keyword": "When",
          "location": "behave_BDD/loginsteps26/BDD_login.feature:27",
          "match": {
            "arguments": [],
            "location": "behave_BDD/loginsteps26/steps/loginsteps1.py:60"
          },
          "name": "user enters correct Email",
          "result": {
            "duration": 0.6237530708312988,
            "status": "passed"
          },
          "step_type": "when"
        },
        {
          "keyword": "And",
          "location": "behave_BDD/loginsteps26/BDD_login.feature:28",
          "match": {
            "arguments": [],
            "location": "behave_BDD/loginsteps26/steps/loginsteps1.py:40"
          },
          "name": "user clicks Login button",
          "result": {
            "duration": 1.473404884338379,
            "status": "passed"
          },
          "step_type": "when"
        },
        {
          "keyword": "Then",
          "location": "behave_BDD/loginsteps26/BDD_login.feature:29",
          "match": {
            "arguments": [],
            "location": "behave_BDD/loginsteps26/steps/loginsteps1.py:55"
          },
          "name": "warning shown about 'No match for E-Mail Address and/or Password'",
          "result": {
            "duration": 0.07201004028320312,
            "status": "passed"
          },
          "step_type": "then"
        }
      ],
      "tags": [
        "negative",
        "skip"
      ],
      "type": "scenario"
    },
    {
      "keyword": "Scenario",
      "location": "behave_BDD/loginsteps26/BDD_login.feature:32",
      "name": "Log in with the incorrect Password",
      "status": "passed",
      "steps": [
        {
          "keyword": "Given",
          "location": "behave_BDD/loginsteps26/BDD_login.feature:34",
          "match": {
            "arguments": [],
            "location": "behave_BDD/loginsteps26/steps/loginsteps1.py:19"
          },
          "name": "user is not logged in",
          "result": {
            "duration": 0.41695380210876465,
            "status": "passed"
          },
          "step_type": "given"
        },
        {
          "keyword": "When",
          "location": "behave_BDD/loginsteps26/BDD_login.feature:35",
          "match": {
            "arguments": [],
            "location": "behave_BDD/loginsteps26/steps/loginsteps1.py:66"
          },
          "name": "user enters correct Email and incorrect Password",
          "result": {
            "duration": 0.9356317520141602,
            "status": "passed"
          },
          "step_type": "when"
        },
        {
          "keyword": "And",
          "location": "behave_BDD/loginsteps26/BDD_login.feature:36",
          "match": {
            "arguments": [],
            "location": "behave_BDD/loginsteps26/steps/loginsteps1.py:40"
          },
          "name": "user clicks Login button",
          "result": {
            "duration": 1.134523868560791,
            "status": "passed"
          },
          "step_type": "when"
        },
        {
          "keyword": "Then",
          "location": "behave_BDD/loginsteps26/BDD_login.feature:37",
          "match": {
            "arguments": [],
            "location": "behave_BDD/loginsteps26/steps/loginsteps1.py:55"
          },
          "name": "warning shown about 'No match for E-Mail Address and/or Password'",
          "result": {
            "duration": 0.06474018096923828,
            "status": "passed"
          },
          "step_type": "then"
        }
      ],
      "tags": [
        "negative",
        "skip",
        "wip"
      ],
      "type": "scenario"
    },
    {
      "keyword": "Scenario",
      "location": "behave_BDD/loginsteps26/BDD_login.feature:41",
      "name": "Log in with the incorrect Email",
      "status": "failed",
      "steps": [
        {
          "keyword": "Given",
          "location": "behave_BDD/loginsteps26/BDD_login.feature:43",
          "match": {
            "arguments": [],
            "location": "behave_BDD/loginsteps26/steps/loginsteps1.py:19"
          },
          "name": "user is not logged in",
          "result": {
            "duration": 0.43926191329956055,
            "status": "passed"
          },
          "step_type": "given"
        },
        {
          "keyword": "When",
          "location": "behave_BDD/loginsteps26/BDD_login.feature:44",
          "match": {
            "arguments": [],
            "location": "behave_BDD/loginsteps26/steps/loginsteps1.py:73"
          },
          "name": "user enters incorrect Email",
          "result": {
            "duration": 0.5465543270111084,
            "status": "passed"
          },
          "step_type": "when"
        },
        {
          "keyword": "And",
          "location": "behave_BDD/loginsteps26/BDD_login.feature:45",
          "match": {
            "arguments": [],
            "location": "behave_BDD/loginsteps26/steps/loginsteps1.py:80"
          },
          "name": "user enters correct Password",
          "result": {
            "duration": 0.35488200187683105,
            "status": "passed"
          },
          "step_type": "when"
        },
        {
          "keyword": "And",
          "location": "behave_BDD/loginsteps26/BDD_login.feature:46",
          "match": {
            "arguments": [],
            "location": "behave_BDD/loginsteps26/steps/loginsteps1.py:40"
          },
          "name": "user clicks Login button",
          "result": {
            "duration": 1.0222997665405273,
            "status": "passed"
          },
          "step_type": "when"
        },
        {
          "keyword": "Then",
          "location": "behave_BDD/loginsteps26/BDD_login.feature:47",
          "match": {
            "arguments": [],
            "location": "behave_BDD/loginsteps26/steps/loginsteps1.py:55"
          },
          "name": "warning shown about 'No match for E-Mail Address and/or Password'",
          "result": {
            "duration": 0.0684669017791748,
            "error_message": [
              "Traceback (most recent call last):",
              "  File \"/Users/iuliia603/PycharmProjects/pythonProject/venv/lib/python3.9/site-packages/behave/model.py\", line 1329, in run",
              "    match.run(runner.context)",
              "  File \"/Users/iuliia603/PycharmProjects/pythonProject/venv/lib/python3.9/site-packages/behave/matchers.py\", line 98, in run",
              "    self.func(context, *args, **kwargs)",
              "  File \"behave_BDD/loginsteps26/steps/loginsteps1.py\", line 58, in check_login_error_warning",
              "    assert login_page.check_login_error_warning() == \"Warning: No match for E-Mail Address and/or Password.\"",
              "AssertionError"
            ],
            "status": "failed"
          },
          "step_type": "then"
        }
      ],
      "tags": [
        "negative",
        "wip"
      ],
      "type": "scenario"
    }
  ],
  "keyword": "Feature",
  "location": "behave_BDD/loginsteps26/BDD_login.feature:2",
  "name": "Login functionality",
  "status": "failed",
  "tags": []
}
]
