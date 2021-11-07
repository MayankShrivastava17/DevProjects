print('------------------------------------------------------------------------------')
print(' ____    _____ _____   ______            _   _____                _           ')
print('|  __ \ / ____/ ____| |  ____|          | | |  __ \              | |          ')
print('| |__) | (___| (___   | |__ ___  ___  __| | | |__) |___  __ _  __| | ___ _ __ ')
print('|  _  / \___ \'\'___ \  |  __/ _ \/ _ \/ _` | |  _  // _ \/ _` |/ _` |/ _ \ __|')
print('| | \ \ ____) |___) | | | |  __/  __/ (_| | | | \ \  __/ (_| | (_| |  __/ |   ')
print('|_|  \_\_____/_____/  |_|  \___|\___|\__,_| |_|  \_\___|\__,_|\__,_|\___|_| ')
print('------------------------------------------------------------------------------')

print('\n')


def rssReader(rss=None):
    if rss is not None:
        import feedparser
        blog_feed = blog_feed = feedparser.parse(rss)
        posts = blog_feed.entries
        details = {
            "Blog Title": blog_feed.feed.title,
            "Blog Link": blog_feed.feed.link
        }
        post_list = []
        for post in posts:
            temp = dict()
            try:
                temp["title"] = post.title
                from bs4 import BeautifulSoup
                soup = BeautifulSoup(post.description, features='html.parser')
                temp["description"] = soup.get_text()
                temp["link"] = post.link
                temp["author"] = post.author
                temp["time_published"] = post.published
                temp["tags"] = [tag.term for tag in post.tags]
                temp["authors"] = [author.name for author in post.authors]
                temp["summary"] = post.summary
            except:
                pass
            post_list.append(temp)
        details["posts"] = post_list
        return details
    else:
        return None

def validURL(url):
    import re
    regex = (
            "((http|https)://)(www.)?" + "[a-zA-Z0-9@:%._\\+~#?&//=]" +
            "{2,256}\\.[a-z]" + "{2,6}\\b([-a-zA-Z0-9@:%" + "._\\+~#?&//=]*)"
    )
    chk = re.compile(regex)
    if (url == None):
        return False
    if (re.search(chk, url)):
        return True
    else:
        return False

if __name__ == '__main__':
    import json
    url = input("Enter the rss url :: ")
    if validURL(url):
        data = rssReader(rss=url)
        if data:
            print('\n')
            print('RSS Feed')
            print('\n')
            print(json.dumps(data, indent=2))
        else:
            print('Please enter a valid url.')
    else:
        print('Enter a valid url.')
