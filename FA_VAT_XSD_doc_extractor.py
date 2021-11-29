
import xml.dom.minidom as mnd

class TesterAplikacjiKSEF:
    
    def __init__(self, xml_path):
        self.xml_path = xml_path
        self.xml_file = mnd.parse(self.xml_path)
        self.zebrana_dokumentacja = {}

    def wyciagnij_elementy_schematu_z_dokumentacja(self,element):
        for node in element.childNodes:
            if node.hasChildNodes():
                if node.nodeName == "xsd:element": 
                    nazwa_elementu = node.attributes.item(0).value 
                    dokumentacja_elementu = node.childNodes.item(1).childNodes.item(1).childNodes.item(0).data
                    if nazwa_elementu != "":
                        self.zebrana_dokumentacja[nazwa_elementu] = [dokumentacja_elementu]
                self.wyciagnij_elementy_schematu_z_dokumentacja(node)
