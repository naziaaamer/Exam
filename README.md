# Python with Playwright Exam
 

- Requirements.txt includes all the packets which needs to be imported.

- To run frontend tests, write python -m behave src/features in terminal. 

- Project structure

Exam/
├ .GitHub/
| ├─ workflows/
| | ├─ python-ci.yml/
├─ src/
| ├─ features/
| | ├─ pages/
| | | └─ page_files.py
| | ├─ steps/
| | | └─ step_files.py
| | ├─ feature_files.feature
| | └─ environment.py
├─ tests/
| ├─ unit/
| | └─ test_example.py
| └─ integration/
|   └─ test_example.py
├─ .gitignore
├─ behave.ini
├─ README.md
└─ requirements.txt