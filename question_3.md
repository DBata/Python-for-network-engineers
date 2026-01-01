Write a Python program that stays in a while loop until a timeout expires.

Your program should set the timeout to be five seconds. Additionally, you should use "time.sleep(1)" to sleep for one second inside your while loop. You will need to "import time" to be able to call time.sleep().

You can create a start_time variable using "start_time=time.time()".

Once you have captured the start time, then you should be able to compare the start time to the current time. This will allow you to determine whether you have exceeded the five second timeout or not.

While inside of your loop, print out a message indicating the amount of time elapsed since the start time (print this out each time through the loop).

Additionally, print out a message indicating that you have exited the loop and also the total elapsed time (elapsed time since the start time).

