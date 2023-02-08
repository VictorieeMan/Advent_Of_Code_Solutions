Created: 2023-02-08

2023-02-08
#1 Hello World *<|:-)
Setting up the AOC_challenges as a hobby project. Will use python for these,
and organize all solutions within this repository. Version 1 of each solution
will be done under the focus of just getting it done. Possible follow-up
versions might optimize other things like faster runtime or more clever code.
Clean code is always important, so that's an "always focus". Maybe all the
(2022-2015)*25 = 200 challenges could be finnished before the end of 2023?
That would be an entertaining challenge.

#2 Started setting up the repository. Installed beautiful soup to help download
test data, but I think that this solution [GeeksForGeeks.com](https://www.geeksforgeeks.org/downloading-files-web-using-python/?ref=lbp)
solution might be moresuitable. Will therefor uninstall beautiful soup and
replace it with the requests module.

#3 The "aoc_test-data-extractor.py" has now solved the problem of collecting
user specific test data from the soc site. It prompts the user for a session
cookie string and then uses it for quthenticating and collecting the
individualized test data. The cookie data is easiest to collect from
your webrowsers inspect mode. Login to https://adventofcode.com/, "inspect"
the website using your browsers developer tools, find the session cookie, copy
its name and paste it into the program before the run. NEVER SHARE THIS COOKIE!
Anyone with your session cookie string can login to your AOC account as long
as it's valid.