# import sched
# import time
#
# def scrape_data():
#     ## ** Put the scraping data from app or webcrawler here**
#     print("Scraping data...")
# s = sched.scheduler(time.time, time.sleep)
# def schedule_scraping(sc):
#     scrape_data()
#     s.enter(3600, 1, schedule_scraping, (sc,))
# s.enter(3600, 1, schedule_scraping, (s,))
# s.run()








#
# import time
#
# def scrape_data():
#     # Your web scraping code here
#     print("Scraping data...")
# while True:
#     scrape_data()
#     time.sleep(3600)