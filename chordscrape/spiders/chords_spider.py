import scrapy
import urllib


class ChordSpider(scrapy.Spider):
    name = 'chords'

    start_urls = [
        'https://www.cifraclub.com.br/the-tallest-man-on-earth/'
    ]

    def parse(self, response):
        for song in response.css('.art_musics li'):
            if song.css('a::attr(title)').get() != None:
                link_prefix = song.css('a::attr(href)').get()
                url = 'https://www.cifraclub.com.br' + link_prefix

                response = urllib.request.urlopen(url)
                webContent = response.read()
                
                with open(f'chords/{song.css("a::attr(title)").get()}.html', 'wb') as f:
                    f.write(webContent)
