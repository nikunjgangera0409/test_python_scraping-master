
import requests
import json
import gzip
import csv
import scrapy
import logging
import os



#Excercice 01

def http_request():
    #website url and params
    url = "https://httpbin.org/anything"
    params = {"isadmin": 1}

    try:
        response = requests.post(url, data=params)
        response.raise_for_status()  
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None
response = http_request()
if response is not None:
    print("Response:")
    print(response)






def http_request(user_agent=None):
    url = "https://httpbin.org/anything"
    params = {"isadmin": 1}
    headers = {"User-Agent": user_agent} if user_agent else None

    try:
        response = requests.post(url, data=params, headers=headers)
        response.raise_for_status()  
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None
response1 = http_request()
print("Response with default user-agent:")
print(response1)

custom_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
response2 = http_request(user_agent=custom_user_agent)
print("\nResponse with custom user-agent:")
print(response2)









#Excercice 2
class ProductProcessor:
    
    def load_product_data(self):
        data_file_path = os.path.join(os.path.dirname(__file__), 'test_python_scraping', 'third_part', 'data', 'data.json.gz')
        try:
            with gzip.open(data_file_path, 'rt', encoding='utf-8') as data_file:
                return json.load(data_file)
        except FileNotFoundError:
            logging.error("Data file not found")
        except json.JSONDecodeError:
            logging.error("Error decoding JSON data")
        return []

    def process_products(self):
        for product in self.product_data:
            product_id = product.get('product_id')
            product_name = product.get('product_name')
            product_price = product.get('product_price')

            if product_name and product_price:
                truncated_product_name = product_name[:30]

                rounded_product_price = round(float(product_price), 1)

                self.available_products.append((product_id, truncated_product_name, rounded_product_price))
                print(f"You can buy {truncated_product_name} at our store at {rounded_product_price}")

            elif not product_name:
                logging.warning(f"Product ID {product_id} has no name")
            elif not product_price:
                logging.warning(f"Product ID {product_id} has no price")
        self.save_available_products_to_csv()



    def save_available_products_to_csv(self):
        if self.available_products:
            csv_file_path = os.path.join(os.path.dirname(__file__), 'data', 'available_products.csv')
            with open(csv_file_path, mode='w', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(['Product ID', 'Product Name', 'Product Price'])
                csv_writer.writerows(self.available_products)
            print("Available products saved to available_products.csv")