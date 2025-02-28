#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
kkengine.py



Author: Joshua Zeng; Ethan Lowe
Version: 1.0.0
"""

import argparse
from selenium import webdriver

VERBOSE = false

def get_webdriver(browser):
    """Returns the appropriate WebDriver based on the selected browser."""
    if browser.lower() == "chrome":
        return webdriver.Chrome()  # Ensure chromedriver is in PATH
    elif browser.lower() == "firefox":
        return webdriver.Firefox()  # Ensure geckodriver is in PATH
    else:
        raise ValueError("Unsupported browser. Choose 'chrome' or 'firefox'.")

def main():
    # Argument parser setup
    parser = argparse.ArgumentParser(description="Selenium script to open a website.")
    parser.add_argument("--browser", type=str, choices=["chrome", "firefox"], default="chrome",
                        help="Choose the browser: 'chrome' or 'firefox'")
    parser.add_argument("--url", type=str, default="https://kichikichi.com/kichikichi-reservation/",
                        help="Specify the website URL to open")
    args = parser.parse_args()

    # Get the appropriate WebDriver
    driver = get_webdriver(args.browser)

    # Open the specified website
    driver.get(args.url)
    print(f"Opened {args.url} in {args.browser.capitalize()}")
    print("Page Title:", driver.title)

    # Exit
    #driver.quit()

if __name__ == "__main__":
    main()