# Scrapy settings for yaofangwang project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'yaofangwang'

SPIDER_MODULES = ['yaofangwang.spiders']
NEWSPIDER_MODULE = 'yaofangwang.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'yaofangwang (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False
IMG_PATH = "./药品"

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    "Cookie": "real_ip=110.53.5.214; HMF_CI=305fa4becf245ee0462355fe863222af2669e9249292de9ccbf3ef49d2ea6766a6bd8c39455f43c8c7d7236a7c4327e92416e4b05c092de71ad8c9ed3743632228; HMY_JC=e9ba9575380ccca1a5771d94ff4efc66195344c93000691cd3c7cd254e06537517,; Hm_lvt_e5f454eb1aa8e839f8845470af4667eb=1665642139; historysearch=; hotkeywords=%E9%98%BF%E8%83%B6%23%231%23%231%23%2311442%40%40%E5%AE%89%E5%AE%AB%E7%89%9B%E9%BB%84%E4%B8%B8%23%230%23%231%23%2310799%40%40%E9%BE%9F%E9%BE%84%E9%9B%86%23%230%23%231%23%2325686%40%40%E6%8B%9C%E6%96%B0%E5%90%8C%23%230%23%231%23%2310189%40%40%E6%8B%9C%E5%94%90%E8%8B%B9%23%230%23%231%23%2314441; ASP.NET_SessionId=kwvto0ywwvw4fnm3ppi24ozh; __RequestVerificationToken=qmp1VmjdlWi0N1VkWgFq16LyWlz6Sfk_1R--tuWQ1D-QrmZ3qYhgACxd_2iMO-QRjJd2lc3HHR4Fk-09kaCX8xc1R122q8uO01C4R70xPtQ1; Hm_lpvt_e5f454eb1aa8e839f8845470af4667eb=1665642155",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36",
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'yaofangwang.middlewares.YaofangwangSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'yaofangwang.middlewares.YaofangwangDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'yaofangwang.pipelines.YaofangwangPipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
