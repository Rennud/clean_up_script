# clean_up_script

## Project description
This project serves for cleaning the repository that have all needed files for academy. Script verify that xml with all academy info contains exercises and images that are in the repo as well. You can get just the information which files are correct and which files are redundant. Also you can just delete the redunant file.

## Project licence
The project is licensed under the MIT license. It is permissive free software license.

## Project demo
<pre><code>INFO: Checking the available pictures...
TO REMOVE: 'pycharm-create-python-file.png'..
TO REMOVE: 'Subset.jpg'..
TO REMOVE: 'promenne_prostredi.jpg'..
TO REMOVE: 'promenne_prostredi_ok.jpg'..
TO REMOVE: 'call-stack-python-online.png'..
CORRECT: '20_project_layout.png'..
CORRECT: '17_quick_setup.png'..
...
</code></pre>

<p>Run script with s option:</p>
<p><code>python3 ../main.py /course_online-python-akademie.xml s png</code></p>

<pre><code>INFO: Removing the redundant exercises...
sum deleting...
all_any deleting...
find deleting...
count deleting...
reversed deleting...
string_length deleting...
horizontal_histogram deleting...
roman_arab deleting...
vertikalni_histogram deleting...
...
</code></pre>

<p>Run script with -d option:</p>
<p><code>python3 ../main.py /course_online-python-akademie.xml d src</code></p>

## Library installation
In this project I am using <code>setup.cfg</code> and <code>setup.py</code> in <code>setup.cfg</code> are all needed dependencies. <code>setup.py</code> is just for starting the installation.
<p>Before installation of dependencies don't forget to create and activate virtual environment: <code>python3 -m venv venv</code></p>
<p>To install all dependencies from setup.cfg: <code>python3 setup.py install</code></p>

## Run script
```$ python3 ../main.py <xml_file_name> <operation> <specify_file>```

<p>To start the script go to the academy repo. <code>online-python-akademie</code> Script can be run via cli and requires three mandatory arguments.</p>
<p>1. arg: <strong>xml file</strong> that contains all information about academy</p>
<p>2. arg: choose operation
    - you can use <strong>s</strong> to get information about which files are used and which aren't.
    - you can use <strong>d</strong> to delete unused files from repository
</p>
<p>3. arg: specify file
    <p><strong>png</strong> -> for images</p>
    <p><strong>src</strong> -> for exercises</p>
</p>

## Community and support
<p>If you have any issue or question please let us know via creating a new issue [here](https://github.com/Rennud/clean_up_script/issues)</p>

