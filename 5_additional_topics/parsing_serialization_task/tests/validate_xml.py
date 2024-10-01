from statistics import mean
from lxml import etree
def check_result(xml_path: str, expected_country: str, expected_cities: int):
    """Function to check weather XML file for a given country and date"""
    tree = etree.parse(xml_path)
    root = tree.getroot()
    assert root.tag == 'weather', "Root tag is not 'weather'"
    assert root.attrib.get('country') == expected_country, f"Expected country '{expected_country}', found '{root.attrib.get('country')}'"
    assert not set(root.attrib.keys()).difference({'country', 'date'}), \
        "No 'country' or 'date' attrib in 'weather' root"
    children = root.getchildren()
    assert set([child.tag for child in children]) == {'summary', 'cities'}, \
        f'Invalid elements in "weather" root'
    summary = None
    cities_summary = {}
    for child in children:
        if child.tag == 'summary':
            summary_attribs = {'mean_temp', 'mean_wind_speed', 'coldest_place', 'warmest_place', 'windiest_place'}
            assert set(child.attrib.keys()) == summary_attribs, \
                f'Invalid attributes list in "summary" element: {set(child.attrib.keys()).difference(summary_attribs)}'
            summary = child.attrib
        if child.tag == 'cities':
            assert len(child) == expected_cities, f"Invalid number of cities in XML: {len(child)}, expected {expected_cities}"
            for city in child:
                city_attribs = {'mean_temp', 'mean_wind_speed',
                                'min_temp', 'min_wind_speed',
                                'max_temp', 'max_wind_speed'}
                assert set(city.attrib.keys()) == city_attribs, \
                    f"Invalid attributes in element {city.tag}: {set(city.attrib.keys()).difference(city_attribs)}"
                cities_summary[city.tag] = city.attrib
    # check results in summary
    mean_temp = round(mean([float(values['mean_temp']) for values in cities_summary.values()]), 2)
    assert float(summary['mean_temp']) == mean_temp, "Incorrect mean temperature in summary."
    warmest_city = max(cities_summary.items(), key=lambda item: float(item[1].get('mean_temp')))[0]
    assert summary.get('warmest_place') == warmest_city, f"The warmest place is incorrect. Expected '{warmest_city}'"
    coldest_city = min(cities_summary.items(), key=lambda item: float(item[1].get('mean_temp')))[0]
    assert summary.get('coldest_place') == coldest_city, f"The coldest place is incorrect. Expected '{coldest_city}'"
    windiest_city = max(cities_summary.items(), key=lambda item: float(item[1].get('mean_wind_speed')))[0]
    assert summary.get('windiest_place') == windiest_city, f"The windiest place is incorrect. Expected '{windiest_city}'"
    print("Success!")
    
if __name__ == '__main__':
    # Example usage: provide the correct country and city count
    check_result(xml_path='/Users/vganesan/Documents/PYTHON/PYTHON-BASIC/practice/5_additional_topics/parsing_serialization_task/tests/example_result.xml', expected_country='Belarus', expected_cities=6)












