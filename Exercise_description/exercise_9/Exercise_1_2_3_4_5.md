QUESTION ONE
A)  Create a short Python script where you "import sys" and then print out your sys.path variable. Manually inspect your sys.path output and determine which locations Python uses for libraries (on your system). Note, do not use "IPython" for this exercise (as it modifies the standard sys.path).

B) Modify your system's $PYTHONPATH environment variable to include the "bin" directory in the base of this course's repository. Modify the script from exercise1a such that you also "import my_lib" which is a simple Python module (located here). Verify the import works properly and visually check that your printed sys.path includes the new directory. You should see "Hello world" on standard out (as my_lib.py prints out this message when imported).



QUESTION TWO
A) Relying on the $PYTHONPATH export specified in exercise1b, create a script that imports "func1" and "func2" from "my_lib2" (my_lib2 is also located in "{ github_repo }/bin"). Note, your script should directly call func1() and func2() without needing to specify the library name in the function call. Make sure your script executes properly--func1() should print out "Hello" and func2() should print out "World".

B) Repeat exercise2a except your calls should now be of the form my_lib2.func1() and my_lib2.func2(). Make sure your script executes properly.

C) Repeat exercise2b except use "as test_lib" and change the name of library (in other words, instead of using my_lib2.func1() and my_lib2.func2() to call func1 and func2, your function calls should be test_lib.func1() and test_lib.func2(). Make sure your script executes properly.



QUESTION THREE
A) [200~Create a new virtual environment named "my_venv". Pick a convenient directory on your system to contain this virtual environment (for example, ~/CODE or ~/VENV).
B) Activate your new virtual environment.
C) Execute "pip list" on the virtual environment and verify that you only have "pip" and "setuptools" installed.
D) Upgrade pip to the latest version of pip.
E) Re-run pip list and verify your version of pip has been upgraded.
F) Use pip to install the rich library. Use pip list to see which libraries were installed in addition to rich.G) Execute "pip freeze" and look at the pip freeze output.
H) Deactivate your virtual environment.



QUESTION FOUR
A) Using your my_venv from exercise3, pip install the Netmiko library from GitHub.
B) pip install the Netmiko master branch from github.
C) pip install the Netmiko 4.1.2 tag.
D) pip install the Netmiko code from Github using this specific commit: 679be2be58a975e874fd97616c7014f0726460c1
E)  Use "pip freeze" and from this output create a requirements.txt file (using the current state of your environment from step 4d).



QUESTION  FIVE
A) Create a new virtual environment named "test1_venv". Activate this new virtual environment.
B) pip install all of the libraries using the requirements.txt file created in Exercise 4e.


