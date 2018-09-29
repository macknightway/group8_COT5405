# group8_COT5405
Algorithms and Analysis Group Projects

Cloning Section

$ git clone https://github.com/macknightway/group8_COT5405.git
$ cd group8_COT5405

Confirming Python Dependencies

confirm you are using at least python 3.6 with the command
python3 --version
If you are using a version lower than 3.6 but higher than 3.0 then use the following two commands
$ sudo apt-get update
$ sudo apt-get install python3.6
Now to download pip for python 3 if you don't have for memory profiler and xml spreadsheet use
$ sudo apt install python3-pip
$ python3.6 -m pip install -U memory_profiler
$ python3.6 -m pip install xlwt

Running Section
Now you can choose to run either the divide function or the test.py
Running divide won't show any input but will compile and complete while the test function will test 200 functions. Do not make it test more than that though! If you want to change how many the tests to run to see the results then change the number inside main at line 88.

$ python3.6 test.py

To run a divide with fresh inputs
$ python 3.6 random_input_generator.py
$ python3.6 divide.py

If you want to see how much memory is taken up then use the next command shown, but be warned that it will take significantly longer than normal so be patient!
$ python3.6 -m memory_profiler divide.py




