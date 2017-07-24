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
        
class formatter:
    tableStarted = False
    output = ""

    def group(self, row):
        if self.tableStarted:
            # end table
            self.output = self.output + self._tableFooter()
            self.tableStarted = False
        
        self.output = self.output + "<h2>{}</h2>".format(row[0])  

    def ship(self, row):
        """
        create ship link, phone link and mail link from ship row
        """
        if not self.tableStarted:
            self.output = self.output + self._tableHeader()
            self.tableStarted = True
        
        shipname, number, mail, mmsi = row
        marine_traffic_link = "https://www.marinetraffic.com/en/ais/details/ships/mmsi:{}".format(mmsi)
        ship_button = "[button link=\"{}\" text=\"{}\"]".format(marine_traffic_link, shipname)
        phone_button = "[tel_res number=\"{}\"]".format(number)
        mail_button = "[mail_res address=\"{}\"]".format(mail)

        self.output = self.output + """<tr>
<td>{}</td>
<td>{}</td>
<td>{}</td>
</tr>""".format(ship_button, phone_button, mail_button)

    def _tableHeader(self):
        header = """<div class="tg-wrap">
<table>
<tbody>"""
        return header

    def _tableFooter(self):
        footer = """</tbody>
</table>
</div>"""
        return footer