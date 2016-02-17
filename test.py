
from feedgen.feed import FeedGenerator
fg = FeedGenerator()
fg.title('test_feed')
fg.link(href='https://homb.it/podcasts/')
fg.description('enjoy')

fg.load_extension('podcast')
fg.podcast.itunes_explicit('no')
fg.podcast.itunes_author('Иван Иванов')
fg.podcast.itunes_subtitle('Иваново детство')
fg.podcast.itunes_summary('Детство Ивана')
fg.podcast.itunes_owner(name='Anastasia M.', email='i@homb.it')

rssfeed=fg.rss_str(pretty=True)
fg.rss_file('test.xml')

