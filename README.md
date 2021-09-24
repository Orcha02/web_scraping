# Steps of web-scraping using Selenium

### **Step 1:** Import libraries

### **Step 2:** Install Driver

### **Step 3:** Specify search URL

### **Step 4:** Scroll to the end of page

### **Step 5:** Locate the info to be scraped from the page

### **Step 6:** Extract the corresponding link of each info

### **Step 7:** Download & save each info in the Destination directory

## Once written proper code then the browser is not important

#### Collect data without browser = "headless browser window"

    #Headless chrome browser
    from selenium import webdriver
    opts = webdriver.ChromeOptions()
    opts.headless =True
    driver =webdriver.Chrome(ChromeDriverManager().install())
