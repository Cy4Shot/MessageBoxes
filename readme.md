# Message Boxes
 
MessageBoxes is a library for python that allows you to create windows style message boxes in python!

## Installation

You can install MessageBoxes with <a href="https://pip.pypa.io/en/stable/installing/">pip</a>! Once you have installed pip, open Command Prompt, Terminal or Powershell and type:
```
pip install messageboxes
```

## Message Boxes Module
The Message Boxes module allows you to create a windows message box using VB overloads! It creates a temporary vbscript and executes it to create a message box.
To begin, you need to import the message boxes module:
```python
from message_boxes import message_box
```
This package will allow you to create a message box with a simple `message_box()` function.
> **NOTE: THIS FUNCTION WILL ONLY WORK ON WINDOWS OPERATING SYSTEMS**

```python
from message_boxes import message_box

result = message_box("<Window Title>", "<Box Contents>", <args>)
print(result) # Prints the ID of the button pressed.
```
For the args, get the sum of the overloads that you want from the table below:

Constant | Value | Description
--- | --- | ---
vbOKOnly | 0 | Display OK button only.
vbOKCancel | 1 | Display OK and Cancel buttons.
vbAbortRetryIgnore | 2 | Display Abort, Retry, and Ignore buttons.
vbYesNoCancel | 3 | Display Yes, No, and Cancel buttons.
vbYesNo | 4 | Display Yes and No buttons.
vbRetryCancel | 5 | Display Retry and Cancel buttons.
vbCritical | 16 | Display Critical Message icon.
vbQuestion | 32 | Display Warning Query icon.
vbExclamation | 48 | Display Warning Message icon.
vbInformation | 64 | Display Information Message icon.
vbDefaultButton2 | 256 | Second button is default.
vbDefaultButton3 | 512 | Third button is default.
vbDefaultButton4 | 768 | Fourth button is default.
vbSystemModal | 4096 | System modal; all applications are suspended until the user responds to the message box.
vbMsgBoxHelpButton | 16384 | Adds Help button to the message box.
vbMsgBoxSetForeground | 65536 | Specifies the message box window as the foreground window.
vbMsgBoxRight | 524288 | Text is right-aligned.
vbMsgBoxRtlReading | 1048576 | Specifies text should appear as right-to-left reading on Hebrew and Arabic systems.
