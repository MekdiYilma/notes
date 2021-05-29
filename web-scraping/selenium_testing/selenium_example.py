from selenium import webdriver
import selenium
import time


def scrape():

    browser = webdriver.Firefox()
    browser.get("http://www.amazon.com/")
    search_box = browser.find_element_by_css_selector("input#twotabsearchtextbox")
    search_box.click()
    search_box.send_keys("alexa")
    search_button = browser.find_element_by_css_selector("div.nav-search-submit input")

    search_button.click()
    time.sleep(3)

    products = browser.find_elements_by_css_selector("div.a-section.a-spacing-medium")

    titles_prices = []
    for i,p in enumerate(products):
        try:
            title_element = p.find_element_by_css_selector("span.a-size-medium.a-color-base.a-text-normal")
            title = title_element.text

            price_whole_element = p.find_element_by_css_selector("span.a-price-whole")
            price = price_whole_element.text

            price_fractional_element = p.find_element_by_css_selector(
                "span.a-price-fraction")
            price += ("." + price_fractional_element.text)

        except selenium.common.exceptions.NoSuchElementException:
            continue
        titles_prices.append((title, price))
        driver.execute_script("window.scrollTo(0, {}})".format(i))

        
    return titles_prices


if __name__ == "__main__":
    print(scrape())
