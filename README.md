#Advanced Software Engineering HW1

##Setup
IMPORTANT: the requirements.txt has too many things. Delete them all until your just left with the following so pip install works:
numpy==2.5.3
pytest==9.1.1
wonderwords==3.0.1

-create SSH key and add to Github repository

-create a venv: "python3 -m venv your_custom_env_name_here --system-site-packages"

-source a venv: "source your_custom_env_name_here / bin / activate"

-install pytest: "python3 -m pip install pytest"

-download github cs4300: https://github.com/sswan3/cs4300 into DevEdu

-install dependencies from from requirements.txt


##Running Tests

-navigate to homework1 directory

-run "pytest" to go through all the tests for each task

-pytest.ini handles the paths to different folders. pytest alone is sufficient to use

##Running a Task

-navigate to src folder
-"python3 task1.py" will run task1

##Running a Test

-navigate to test folder
-"pytest test_task1.py" runs test for task1.py



