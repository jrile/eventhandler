# Firebird Event Listener
## Listens for user-specified events on Fishbowl inventory system and sends email alerts.


"Listen host" is the host that the program "listens" for. (Where the Fishbowl database is located.)
"Event host" refers to the database containing the events and email addresses.

By default, the program will attempt to create a configuration file at the point where it is run at called "CONFIG.properties".
If there is an error it is run with the default settings listed below.

Default settings:
- listenHost=localhost
- listenPort=3050
- listenUser=sysdba
- listenPass=masterkey
- listenDatabase=C:\\listen.fdb
- eventHost=localhost
- eventPort=3050
- eventUser=sysdba
- eventPass=masterkey
- eventDatabase=C:\\events.fdb
- mail.smtp.host=localhost
- mail.smtp.port=25
- poreportpath=C:\\Program Files (x86)\\Fishbowl\\server\\reports\\Custom\\POReport.jasper