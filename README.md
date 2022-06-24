# clean_up_script

## Project description 
This project serves for cleaning the repository that have all needed files for academy(xml, images, exercises).

## Library installation 
In this project I am using pipenv package manager that creates Pipfile.lock file that contains all needed dependecies to set up the project. 
<p>Check pipenv manager: <code>pipenv --version</code><p>
<p>If you don't have pipenv you can install it via pip: <code>pip install pipenv</code></p>
<p>Before installation of dependecies don't forget to turn on virtual environment: <code>pipenv shell</code></p>
<p>To install all dependecies from Pipfile.lock: <code>pipenv install</code></p>

## Turn on script 
<p>To start the script go to the academy repo. <code>online-python-akademie</code> Script can be run via cli and requires three mandatory arguments.</p>
<p>1. arg: <strong>xml file</strong> that contains all information about academy</p>
<p>2. arg: choose operation 
    - you can use <strong>-s</strong> to get information about which files are used and which aren't.
    - you can use <strong>-d</strong> to delete unused files from repository
</p>
<p>3. arg: specify file
    <p><strong>png</strong> -> for images</p>
    <p><strong>src</strong> -> for exercises</p>
</p>
  
```$ python3 ../main.py <xml_file_name> <operation> <specify_file>```

## Script run examples

<p>Run script with -s option:</p>
<p><code>python3 ../main.py /course_online-python-akademie.xml -s png</code></p>

<p>Partial output: </p>
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

<p>Run script with -d option:</p>
<p><code>python3 ../main.py /course_online-python-akademie.xml -d src</code></p>

<p>Partial output: </p>
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

## Project structure 
<p>Script controlor is <code>main.py</code> there is a main in which are set up sys.argv and call the <code>main_parser</code> func and passed sys.args as arguments for the func.</p>

<p>In <code>parser.py</code> are all the functions to get needed information about pic and exer. + <code>main_parser</code> function that 
handles logic behind args. we can divide the file into 4 imaginary blocks:
</p>

<p>1. block is <code>main_parser</code>function with <code>parse_xml_file</code>function that handles parsing of xml file</p>
<p>2. block contains all function needed just for the images</p>
<p>3. block contains all function needed just for the exercises</p>
<p>4. contains only one function that is needed for <strong>-s</strong> option and can be used with images and exercises as well</p>
