<div align="center">
  <img src='https://github.com/Varinder-KM/Critic_Crawler/blob/master/static/logo.png' alt='logo'>
</div>
<hr>
<p>
  Welcome to CriticCrawler! This project is designed to make it easy for users to fetch product reviews from the popular e-commerce 
  website, Flipkart. By simply providing the name of a product as input, you can retrieve a comprehensive list of reviews related to 
  that product. Additionally, this project incorporates sentiment analysis to help you gain insights into the overall sentiment expressed 
  in the reviews.
 </p>
 <hr>
 
 <h2>Main Features:</h2>
 <ul>
  <li>Web Scraping: Utilizing web scraping technology, this project fetches product reviews from Flipkart by leveraging the provided product name.</li>
  <li>Review Extraction: It extracts a wide range of information from the reviews, including the reviewer's name, rating, date, and the text of the review itself.</li>
  <li>CSV Export: The project provides the option to export the collected reviews in CSV format. This allows for convenient analysis and further processing of the data.</li>
  <li>Sentiment Analysis: By employing sentiment analysis techniques, the project evaluates the sentiment expressed in each review, providing a deeper understanding of customer opinions.</li> 
 </ul>
 
 <h2>Installation: </h2>
 <ol>
  <li>
    <p>After downloading the project open it in VSCode and create a virtual environment.</p>
    <code>python -m venv venv </code>
  </li>
  <li>
    <p>Activate the enviroment.</p>
    <code>venv/Scripts/Activate.ps1</code>
  </li>
  <li>
     <p> Install all the required packages</p>
     <code>pip install -r requirements.txt</code>
  </li>
  <li>
    <p>Run the project</p>
    <code>flask run</code>
 </ol>


<h2>How to Use:</h2>
<ul>
  <li>Installation: Follow the installation instructions outlined in the README file to set up the project environment and install the necessary dependencies.</li>
  <li>Input: Provide the name of the product you wish to fetch reviews for.</li>
  <li>Execution: Run the project, and it will initiate the web scraping process, fetching the reviews from Flipkart.</li>
  <li>CSV Export: Once the reviews are collected, you will have the option to download them in CSV format for further analysis.</li>
  <li>Sentiment Analysis: The project automatically performs sentiment analysis on the collected reviews, categorizing them as positive, negative, or neutral.</li>
 </ul>
 
 
 <p>
  Please note that this project is specifically tailored to work with Flipkart's website structure and may have limitations when scraping data from other websites. However, it offers a convenient solution for extracting product reviews, analyzing sentiment, and gaining valuable insights into customer feedback.
 </p>
 <p>
  We hope you find CriticCrawler useful and that it simplifies your research and analysis of product reviews from Flipkart. Feel free to provide feedback, report any issues. 
 </p>
  
 
 
