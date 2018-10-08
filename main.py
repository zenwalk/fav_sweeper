
import os
import io
from requests_html import HTML
from glob import glob


def handle(filename):
    print(filename)
    
    with io.open(filename, encoding='utf-8') as f:
        s = f.read()
    if len(s) == 0:
        return
    html = HTML(html=s)
    script_list = html.find('script')
    if len(script_list) != 2:
        return
    script = script_list[1]
    s = script.text.replace('parent.FM.view', 'feed_data=')
    with io.open('temp.py', 'w', encoding='utf-8') as f:
        f.write(s)
    temp = __import__('temp')
    html = temp.feed_data['html']
    html = HTML(html=html)
    feeds = html.find('[node-type="feed_list_content"]')
    for feed in feeds:
        if '抱歉，此条微博已经被作者删除，取消收藏' in feed.text: 
            print(dir(feed))
    



def main():
    html_list = glob('data/fav102.html')
    for f in html_list:
        handle(f)
        

if __name__ == '__main__':
    main()


