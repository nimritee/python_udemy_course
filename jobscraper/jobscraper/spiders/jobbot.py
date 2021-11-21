import scrapy

class JobbotScraper(scrapy.Spider):
    name = 'jobbot'
    allowed_domains=['https://www.glassdoor.de/Job/working-student-jobs-SRCH_KO0,15.htm']
    start_urls=['https://www.glassdoor.de/Job/working-student-jobs-SRCH_KO0,15.htm']

    def parse(self, response):
        #Extracting the content using css selectors
        role = response.css('li.job-search-key-nhtksm::attr(data-normalize-job-title)').extract()
        location = response.css('li.job-search-key-nhtksm::attr(data-job-loc)').extract()

        row_data = zip(role,location)

        #Give the extracted content row wise
        scraped_info ={}
        for item in row_data:
            #create a dictionary to store the scraped info
            scraped_info = {
                'role' : item[0],
                'location' : item[1],
            }
        yield scraped_info