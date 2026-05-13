from crawl4ai import AsyncWebCrawler

class BaseScraper:
    """
    Lớp cơ sở cấu hình cho Crawler.
    Ở đây chúng ta có thể mở rộng để cấu hình proxy, headers, 
    hoặc stealth mode.
    """
    def __init__(self, headless: bool = True):
        self.headless = headless
        
    def get_crawler(self) -> AsyncWebCrawler:
        return AsyncWebCrawler(headless=self.headless)
