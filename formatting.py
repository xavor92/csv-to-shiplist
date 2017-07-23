import re

class validator:
    """
    Validate the various inputs
    """

    phone_regex = re.compile("^[\d -]+$")
    mail_regex = re.compile("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
    mmsi_regex = re.compile("^\d+$")

    def checkPhone(self, number):
        if self.phone_regex.match(number):
            return True
        else:
            print "Invalid Phone Number:", number
            return False

    def checkMail(self, mail_addr): 
        if self.mail_regex.match(mail_addr):
            return True
        else:
            print "Invalid Mail Address Number:", mail_addr
            return False

    def checkMmsi(self, mmsi_num):
        if self.mmsi_regex.match(mmsi_num):
            return True
        else:
            print "Invalid MMSI:", mmsi_num
            return False

    def checkShip(self, row):
        shipname, number, mail, mmsi = row
        if self.checkPhone(number) and self.checkMail(mail) and self.checkMmsi(mmsi):
            return True
        return False
        
        