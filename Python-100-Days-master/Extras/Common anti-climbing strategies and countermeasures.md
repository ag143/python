## Common anti-crawling strategies and countermeasures

1. Construct reasonable HTTP request headers.
   -Accept

   - User-Agent

   - Referer
   
   -Accept-Encoding
   
   -Accept-Language
2. Check the cookies generated by the website.
   - Useful plugin: [EditThisCookie](http://www.editthiscookie.com/)
   - How to handle cookies dynamically generated by scripts
3. Crawl dynamic content.
   -Selenium + WebDriver
   - Chrome / Firefox - Driver
4. Limit the speed of crawling.
5. Handle hidden fields in the form.
   - don't submit the form until the hidden field is read
   - Use tools like RoboBrowser to assist in submitting forms
6. Process the captcha in the form.
   - OCR (Tesseract) - generally not considered for commercial projects

   - Professional identification platform - Super Eagle / Cloud coding

     ````Python
     from hashlib import md5
     
     class ChaoClient(object):
     
         def __init__(self, username, password, soft_id):
             self.username = username
             password = password.encode('utf-8')
             self.password = md5(password).hexdigest()
             self.soft_id = soft_id
             self.base_params = {
                 'user': self.username,
                 'pass2': self.password,
                 'softid': self.soft_id,
             }
             self.headers = {
                 'Connection': 'Keep-Alive',
                 'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
             }
     
         def post_pic(self, im, codetype):
             params = {
                 'codetype': codetype,
             }
             params.update(self.base_params)
             files = {'userfile': ('captcha.jpg', im)}
             r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, files=files, headers=self.headers)
             return r.json()
     
     
     if __name__ == '__main__':
         client = ChaoClient('username', 'password', 'software ID')
         with open('captcha.jpg', 'rb') as file:
             print(client.post_pic(file, 1902))
     ````

7. Avoid "gotchas."
   - There are hidden links to crawling (traps or honeypots) on the page that lure crawlers into crawling
   - Determine whether the link is visible or in the visible area through Selenium+WebDriver+Chrome
8. Hide your identity.
   - Agency Service - Express Agency / News Agency / Sesame Agency / Mushroom Agency / Cloud Agency

     ["Which reptile agent is stronger? The detailed comparison and evaluation of the top ten paid agents is released! 》](https://cuiqingcai.com/5094.html)

   - Onion routing - domestic need to overturn the wall to use

     ```Shell
     yum -y install tor
     useradd admin -d /home/admin
     passwd admin
     chown -R admin:admin /home/admin
     chown -R admin:admin /var/run/tor
     tor
     ````