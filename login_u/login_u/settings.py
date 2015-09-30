# -*- coding: utf-8 -*-

# Scrapy settings for login_u project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'login_u'

SPIDER_MODULES = ['login_u.spiders']
NEWSPIDER_MODULE = 'login_u.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'login_u (+http://www.yourdomain.com)'
DOWNLOADER_MIDDLEWARE = [ 'scrapy.contrib.downloadermiddleware.httpauth.HttpAuthMiddleware']

http_user = "username"
http_pass = "password"

COOKIES_ENABLED = True
# COOKIES_DEBUG = True
