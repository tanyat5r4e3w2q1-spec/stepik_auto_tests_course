<input class="check-input" type="radio" name="ruler" id="peopleRule" value="people" checked>


people_radio = browser.find_element(By.ID, "peopleRule")

people_checked = people_radio.get_attribute("checked")
print("value of people radio: ", people_checked)
assert people_checked is not None, "People radio is not selected by default"

assert people_checked == "true", "People radio is not selected by default"

robots_radio = browser.find_element(By.ID, "robotsRule")
robots_checked = robots_radio.get_attribute("checked")
assert robots_checked is None

robots_radio = browser.find_element(By.ID, "robotsRule")
robots_checked = robots_radio.get_attribute("checked")
assert robots_checked is None

robots_radio = browser.find_element(By.ID, "robotsRule")
robots_checked = robots_radio.get_attribute("checked")
assert robots_checked is None

