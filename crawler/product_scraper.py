from .base_scraper import BaseScraper

class ProductScraper(BaseScraper):
    """
    Lớp cào dữ liệu chuyên dụng cho trang sản phẩm.
    """
    def __init__(self, headless: bool = True):
        super().__init__(headless=headless)

    async def scrape_product(self, url: str) -> dict:
        """
        Cào dữ liệu từ URL sản phẩm và trả về nội dung Markdown sạch.
        """
        async with self.get_crawler() as crawler:
            result = await crawler.arun(
                url=url,
                bypass_cache=True,
            )
            
            return {
                "url": url,
                "status_code": getattr(result, 'status_code', 200),
                "markdown_content": result.markdown,
                "success": result.success
            }
