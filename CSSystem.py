import commands

class CSSystem():
    
    def findHardDrives(self):
        unparsed = commands.getoutput("fdisk -l").split("\n")
        drives = [line[5:13] for line in unparsed if line.startswith("Disk /") and not line.startswith("Disk /dev/sda")]
        if not drives:
            raise SystemException("Can't get any information from fdisk. Please make sure you are running as root user and there is more than one hard drive mounted.")
        return drives
        
    def getSerial(self, drive):
        try:
            return commands.getoutput("smartctl -i " + drive + " | grep \"Serial Number:\"").split()[2]
        except IndexError:
            raise SystemException("Can't get serial number from hard drive " + drive)
            
            
    def getMountPoint(self, drive):
        unparsed = commands.getoutput("mount").split('\n')
        for line in unparsed:
            if line.startswith(drive):
                return line.split(' ')[2]
        raise SystemException(drive + " is not mounted!")
        
    def getName(self, mount_point):
        temp = mount_point.split("/")
        return temp[-1]
        
    def getDirSize(self, path):
        return int(commands.getoutput('du -bs ' + path).split()[0])
        
            
class SystemException(Exception):
    pass
