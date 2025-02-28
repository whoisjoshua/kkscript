#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
kkengine.py

This script fearlessly navigates the chaotic digital jungle of restaurant reservations,  
battling captchas, dodging 404 errors, and securing that sacred dinner spot  
before Karen from accounting takes the last table. 

Note that this is not used for any distribution of service denial of any kind and is only 
used to run locally on one machine. If anyone chooses to use this, please be considerate 
of businesses. Any improper use of this script is not our responsibility.

Authors: Joshua Zeng; Ethan Lowe
Version: 1.0.0
"""

import argparse
from selenium import webdriver

VERBOSE = False

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
    parser.add_argument("-v", "--VERBOSE", type=str, dest="verbose", action="store_true",
                        help="Optional: Run with VERBOSE debug setting")
    args = parser.parse_args()

    # Update VERBOSE
    if args.verbose:
        VERBOSE = True

    # Get the appropriate WebDriver
    driver = get_webdriver(args.browser)

    # Open the specified website
    driver.get(args.url)
    print(f"Opened {args.url} in {args.browser.capitalize()}")
    print("Page Title:", driver.title)

    # TODO: We need to find the HTML 

    # Page front

    # Page reservation form

    # Submission (this is unknown)

    # Exit
    #driver.quit()

if __name__ == "__main__":
    main()