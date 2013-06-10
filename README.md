Copy Station
v 1.0.1
(c) 2013 Eastcor Engineering

ADDING:
"Add hard drive" simply adds the hard drive and it's contents to the database.
If you're backing up a drive, there's no need to do this because it will be automatically added.
After adding a hard drive, you can also add details on it's location by simply going into the drive's information dialog
(by double clicking it in the main window) and clicking "View/update location."

BACKING UP:
After a drive has been backed up, the destination drive as well as the source drive are added to the database.
The database keeps track of specific drive's backups as well. You can also edit the location once the drive has been backed 
up as mentioned above.

While backing up, progress is printed on the command line.

ADDING USER:
'Name' field is not required. Regular user (no admin features) level = 1. Administrator = 3. 

EDITING USER:
First checks to see if the username you're editing exists. If it does, it will populate the dialog with the information
in the database already and you can change what you want.

DELETING USER:
This completely deletes the user from the database, however, if this user has added anything to the database in the past
their username will still be stored in those tables.

