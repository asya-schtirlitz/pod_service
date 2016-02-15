
from feedgen.feed import FeedGenerator
fg = FeedGenerator()
fg.title('test_feed')
fg.link(href='https://homb.it/podcasts/')
fg.description('enjoy')
rssfeed=fg.rss_str(pretty=True)
fg.rss_file('test.xml')
