#!/usr/bin/env python3
import tests.main_test as main_test
import time

print("Welcome to Kanji's OnlyFans Scraper!")
time.sleep(3)

print("If you encounter an error saying 'Access Denied', go into /.settings and delete your config file and relaunch the script.")
time.sleep(5)

main_test.version_check()
main_test.check_config()

if __name__ == "__main__":
    import datascraper.main_datascraper as main_datascraper
    main_datascraper.start_datascraper()
