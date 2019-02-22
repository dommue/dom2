import requests
import urlparse
from bs4 import BeautifulSoup

class Craw:
    url="error"
    main_url="error"
    params="error"
    res_cont="error"
    soup="error"
    
    def __init__(self,url):
        self.url=url
        self.get_main_url()
        self.get_url_params()
        self.get_requests()
        self.get_soup()
        
    def get_requests(self):
        res = requests.get(self.url)
        self.res_cont = res.content
    def get_main_url(self):
        main_url = self.url.split("?")[0]
        self.main_url = main_url
    def get_url_params(self):
        params = dict( urlparse.parse_qsl( urlparse.urlsplit( self.url ).query ) )
        self.params = params
    def get_soup(self):
        self.soup = BeautifulSoup( self.res_cont,"html.parser" )
        
    def error_test(self):
        print self.url
        print self.main_url
        print self.params
        print self.res_cont[0]
        print type(self.soup)
              
    def find_soup_tag(self,tag):
        tag = self.soup.find(tag)
        return tag
    
    def findall_soup_tags(self,tags):
        all_tags = self.soup.find_all(tags)
        return all_tags

    def find_class_soup(self,classname):
        clist = self.soup.find_all(class_=classname)
        return clist

    def add_params(self,params,key,value):
        params[key] = value
        return params
    
    def new_url(self,param):
        new_url = self.main_url +"?"
        for i in param.keys():
            new_url = new_url + i + "=" + param[i] +"&"  
        return new_url
