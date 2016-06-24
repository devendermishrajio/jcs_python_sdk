from xml.sax import parseString

def parse(response_object, xml_doc):
	parseString(xml_doc, response_object)