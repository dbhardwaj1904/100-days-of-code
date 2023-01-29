from selenium import webdriver
import time

chrome_driver_path = "CHROME_DRIVER_PATH"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

url = "https://orteil.dashnet.org/experiments/cookie/"
driver.get(url)

# Get cookie
cookie = driver.find_element_by_id("cookie")

# Get upgrade
items = driver.find_elements_by_css_selector("#store div")
items_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 5
five_min = time.time() + 60*5

while True:
    cookie.click()

    if time.time() > timeout:
        all_prices = driver.find_elements_by_css_selector("#store b")
        item_prices = []

        # Convert to integer
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        # Create dict. for store items and prices
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = items_ids[n]

        # Get current cookie count
        money_element = driver.find_element_by_id("money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        # Upgrades to done
        upgrades = {}
        for cost, i_id in cookie_upgrades.items():
            if cookie_count > cost:
                upgrades[cost] = i_id

        # Purchase expensive upgrade
        expensive_upgrade = max(upgrades)
        purchase_id = upgrades[expensive_upgrade]
        driver.find_element_by_id(purchase_id).click()

        timeout = time.time() + 5

    if time.time() > five_min:
        cookie_time = driver.find_element_by_id("cps").text
        print(cookie_time)
        break


# Close single tab
# driver.close()

# Close browser
# driver.quit()
