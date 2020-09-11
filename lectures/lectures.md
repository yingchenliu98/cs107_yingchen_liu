# cs107

View the book with "<i class="fa fa-book fa-fw"></i> Book Mode".
[ToC]

Lecture 1 Unix
---
[UNIX/LINUX cheat sheet](http://cheatsheetworld.com/programming/unix-linux-cheat-sheet/)

### Essential Commands
![](https://i.imgur.com/IYeWM6R.png)

- `man` and more information
    - display a manual page: `man`
    - request pages from specific sections
    `man 3 printf`
- `find`
**`find <target_dir_path> <-options> <pattern>`**
    - searches the filesystem for files whose name matches a specific pattern
    - `find` works recursively, go through all the ==files and subdirectory== of the target dir 
        - set levels at the end
        `-maxdepth 2` will search for file only at the target directory and the next level directories
        
```bash
# scan for name
find . -name name_you_want
# . is current dir
# can specify a path of directory

# scan for certain file types
find . -type d
find . -type f
# use exec to perform operations 
find . -type f -exec wc -l {} \;
# -type f: find files (-type d): find dir
# . current directory
# execute(-exec) word count(wc) with line count option(-l)
# the current file gets pur into the {}
# ; terminate the command invoked by -exec
# need \ in front of ; to tell the shell to interpret ; correctly
```
- `grep`
**grep [options] STRING FILE_LIST**
    - search for occurrences of the string 
    - extracts lines from a file that match a given string or pattern
    - use regular expression
    - `-i` : ignore case
    - `-c` : report only a count of the number of lines containing matches
    - `-v` : invert the search, displaying only lines that do not match
    - `-n` : display the line number along with the line on which a match was found
    - `-l` : list filenames, but not lines, in which matches were found
### Unix Pipes
- A pipe is a holder for a stream of data
- A Unix pipeline is a set of processes chained by their standard streams
    -  The output of each process (stdout) feeds directly as input (stdin) to the next one
- use | to pipe two commands together
---

### Regular Expressions
General search pattern characters
- Any character
- `.` matches any character except a newline
- `*` any pattern matches zero or more occurrences of the single preceding character
- `+` matches one or more of the proceeding character
- `?` matches zero or one of the proceeding character
- `()` quantify a sequence of characters
- `|` functions as an OR operator
- `{}` indicate ranges in the number of occurrences
- `[]` or

To match a special character, you should use the backslash `\`
- To match a period do `\.`
- `a\.b` matches `a.b` because `.` is special
- use `[]` to match any character in it
- `-` to give a range of characters
- `^` negate the class
    - match any character that is not in `[]`

Some shorthand character classes are available for convenience
- `\d` a digit, e.g. [0-9]
- `\D` a non-digit, e.g. [^0-9]
- `\w` a word character, matches letters and digits
- `\W` a non-word character
- `\s` a whitespace character
- `\S` a non-whitespace character

Some shorthand classes are available for matching boundaries
- `^` anchor occurance at the very beginning, put before the literal string
- `$` anchor occurance at the very end, put after the the literal string
- `\b` a word boundary
- `\B` a non-word boundary

---
### File Permissions
![](https://i.imgur.com/OlE5lMp.png)
change file permissions
`chmod <mode> <file>` 
- Mode type 1: Symbolic representation
```
[ugoa] [+-=] [rwxX]
# u=user g=group o=other a=all
# + add permission - remove permission = set permission
# r=read w=write x=execute
```
X sets to execute only if the file is a directory or already has execute
permission
- Mode type 2: Octal Representation
    -  uses a single-argument string which describes the permissions for a file (3 digits)
    -  Each digit is a code for each of the three permission levels
    -  `read=4 write=2 execute=1`
    -  Sum the individual permissions to get the desired combination
---
### vim
**`vim <filename>`**
1.insert mode 2. command mode
```
# Press i to enable insert mode
# Type text (use arrow keys to move around)
# Press Esc to enable command mode
# Press :w (followed by return) to save the file
# Press :q (followed by return) to exit vim
```
---
Lecture 2
---
### Shell customization
- Each shell supports some customization
    - user prompt settings
    - environment variable settings
    - aliases
- The customization takes place in **startup files**, which are read by the shell when it starts up
    - Gloabal files are read first - these are provided by the system administrators(e.g. `/etc/profile`)
    - Local files are then read the user's `HOME` directory to allow for additional customization
    
Shell startup files(I)
[Shell configuration Files](https://en.wikipedia.org/wiki/Unix_shell#Configuration_files)
- The bash shell has two configuration files:
    - `~/.bash_profile `- Read at login
    - `~/.bashrc`- Read at login and when a new window is opened
    - put environment variables in bash_profile and any others in bashrc
- The zsh shell uses:
    - `~/.zprofile` - Read at login
    - `~/.zshrc` - Read at login and when a new window is opened
[Moving to zsh – Scripting OS X](https://scriptingosx.com/2019/06/moving-to-zsh/)
[About bash_profile and bashrc on macOS](https://scriptingosx.com/2017/04/about-bash_profile-and-bashrc-on-macos/)

### I/O
|3 I/O streams|File descriptors|where|
|-------------|----------------|-----|
|standard input|0 = STDIN|keyboard|
|standard output|1 = STDOUT|screen|
|standard error|2 = STDERR| screen|
To end the input, press Ctrl-D on a line; this ends the input stream
### Shell Stream Redirection
The shell can attach things other than the keyboard to standard input or
output
 e.g. a file or a pipe
- Use > to tell the shell to store the output of your program in a file
 `ls > ls_out`
- Use < to tell the shell to get standard input from a file
 `sort < nums`
- combine both forms together
 `sort < nums > sortednums`
- two modes of output redirection
    - `> - create mode`
        - only applies to stdour not stderr
    - `>> - append mode`

To redirect stderr to a file, you must specify the request directly
- `2>` redirects stderr (e.g. `ls foo 2> err`)
- `&>` redirects stdout and stderr (e.g. `ls foo &> /dev/null` )
- `ls foo > out 2> err` redirects `stdout` to `out` and `stderr` to `err`
### Job control
### Environment Vairables
### Bash scripting
Shell scripts must begin with a specific line to indicate which shell should be
used to execute the remaining commands in the file
- Use `#!/bin/bash` in Bash
- Use `#!/bin/zsh` in Zsh
- Comment out lines with `#`
[Moving to zsh](https://scriptingosx.com/2019/08/moving-to-zsh-part-8-scripting-zsh/)
#### Conditionals
```bash
if [ condition_A]; then
# code to run if condition_A true
elif [ condition_B ]; then
# code to run if condition_A false and condition_B true
else
# code to run if both conditions false
fi
```
#### String comparisons
```bash
# test identity
string1=string2
# test inequality
string1!=string2
# the length of string is nonzero
-n string
# the length of string is zero
-z string
```
#### integer comparisons
```bash
# test identity
int1 -eq int2
# test inequality
int1 -ne int2
# less than
int1 -lt int2
# greater than
int1 -gt int2
# less than or equal
int1 -le int2
# greater than or equal
int1 -ge int2
```
#### common file test
check the state of files and directories
```bash
# test if the file is a directory
-d file
# test if the file is not a directory
-f file
# test if the file has nonzero length
-s file
# test if the file is readable
-r file
# test if the file is writable
-w file
# test if the file is executable
-x file
# test is the file is owned by the user
-o file
# test if the file exists
-e file
```