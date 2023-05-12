from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import pandas as pd 
import numpy as np 
import requests
from bs4 import BeautifulSoup
import lxml
import re

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///Reviews.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Reviews(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    reviews = db.Column(db.String(1000), nullable=True)

    def __repr__(self) -> str:
      return f"{self.sno} - {self.reviews}"

# sub_reviews
def sub_reviews(lnk):
  reviews_ls = []
  html1 = requests.get(lnk)
  if html1.status_code == 200:
    soup1 = BeautifulSoup(html1.text, 'lxml')
    rvws = soup1.findAll('div', attrs={'class': '_27M-vq'})
    
    for rvw  in rvws:
      r = str(rvw.find('div', attrs={'class': ''}))
      r  = ' / '.join([w for w in r[19:-63].split('<br/>')])
      reviews_ls.append(r)
    
    return reviews_ls

# get_reviews
def get_reviews(lnk):
  reviews_ls = []
  link = 'https://www.flipkart.com' + lnk
  html1 = requests.get(link)
  if html1.status_code == 200:
    soup1 = BeautifulSoup(html1.text, 'lxml')
    rvws = soup1.findAll('div', attrs={'class': '_27M-vq'})

    for rvw  in rvws:
      r = str(rvw.find('div', attrs={'class': ''}))
      r  = ' / '.join([w for w in r[19:-63].split('<br/>')])
      reviews_ls.append(r)
    
    navs =  soup1.find('div', attrs={'class':'_2MImiq _1Qnn1K'})
    str_num = navs.find('span').text[10:]
    str_num = str_num.replace(',', '')
    nums = 5 if int(str_num) > 5 else int(str_num)
    for num in range(2, nums+1):
      hrf = 'https://www.flipkart.com' + lnk+ '&page='+ str(num)
      ls = sub_reviews(hrf)
      reviews_ls.extend(ls)

  return reviews_ls 

# all_reviews
def all_reviews(item_link):
  link  = 'https://www.flipkart.com' + item_link
  html = requests.get(link)
  list_of_reviews = []
  if html.status_code == 200:
    soup = BeautifulSoup(html.text, 'lxml')
    rvw_links = soup.find('div', attrs={'class': 'JOpGWq'}).findAll('a')
    review_link = rvw_links[-1]['href']
    list_of_reviews = get_reviews(review_link)

  review_df = pd.DataFrame({'Reviews': list_of_reviews})
  return review_df
    
# featch_from_flipkart
def featch_from_flipkart(product, prod_nam):
  html = requests.get(product)
  links_ls = []
  dataset = pd.DataFrame(columns=['Reviews'])
  if html.status_code == 200:
    soup = BeautifulSoup(html.text, 'lxml')
    sm_text = soup.findAll('div', attrs={'class': '_13oc-S'})
    for item in sm_text:

      info_dct = {}
      info_dct['link'] = item.find('a')['href']
      lnk = item.find('a')
      nam = lnk.find('div', attrs={'class': '_4rR01T'}).text
      info_dct['nam'] = nam
      info_dct['img'] = lnk.find('img', attrs={'alt': nam})['src']

      links_ls.append(info_dct)
    
    for item in links_ls:
      prd_nm = '^'+prod_nam
      itm_nam = item['nam'].lower()
      if len(re.findall(prd_nm, itm_nam)) > 0:
        df = all_reviews(item['link'])
        dataset = pd.concat([dataset, df], ignore_index=True)
        break

    return dataset, links_ls[1]['nam'], links_ls[1]['img']
  else:
    return 'Request is Not FullFilds'
    
global dataset
      
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        prod_name = request.form['prod_input']
        tr_name = '+'.join([w.lower() for w in prod_name.split()])
        tr_name

        flipkart_url = 'https://www.flipkart.com/search?q='+tr_name
        flipkart_url
        try:
            dataset, name, img = featch_from_flipkart(flipkart_url, prod_name.lower())
        except:
            return render_template('Emplty.html', dataset=dataset)

        if dataset.size:
          return render_template('reviews.html', dataset=dataset, prd_nam=name, prd_img = img)
        else:
            return render_template('Empty.html', dataset=dataset)

    return render_template('index.html')





@app.route('/reviews', methods=['GET', 'POST'])
def downlad():
  return len(dataset.size)

if __name__ == "__main__":
    app.run(debug=True)