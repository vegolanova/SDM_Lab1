# SDM_Lab1

This program is intended to solve quadratic equations with Python.

##Installation
1. Make sure you have Python3 and git installed.
2. Clone the repository
```bash
  git clone https://github.com/vegolanova/SDM_Lab1
```
3. Open directory
```bash
  cd SDM_Lab1
```
4. Run the script
```bash
  python3 main.py
```

## How to use

The program offers two modes:
1. Interactive
 *Input the parameters' values manually.*
3. Non-interactive (Script)
 *Get values from a text file.*

In interactive mode you will be directly asked to input the values:

```
Input paramenter "a":
 3 
Input paramenter "b":
 2
Input paramenter "c":
 -5
The equation looks like this: 3.0*x^2 + (2.0)*x + (-5.0') = 0. Checking distcriminant...

Two roots exist. Calculating...

roots are: root #1:  1.0 root #2:  -1.6666666666666667
```

In script mode you will need to provide a file which contains the values following such regular expression: "\d\s\d\s\d\n". 
*For example: 2 -32 7*

```
Input file name: 
test_vals
The equation looks like this: 4.0*x^2 + (-11.0)*x + (3.0') = 0. Checking distcriminant...

Two roots exist. Calculating...

roots are: root #1:  2.4430004681646915 root #2:  0.3069995318353087
```

[Revert commit](https://github.com/vegolanova/SDM_Lab1/commit/cafc37ae5cd52b720604a2e92fb56139f3b23b00)
