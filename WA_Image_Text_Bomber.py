import autoit
from selenium import webdriver
import time
import datetime
import os,shutil
from google_images_download import google_images_download
import json
from random_word import RandomWords



driver = webdriver.Chrome()
doc_filename = None
keywordsList = None
randomWordsGen = RandomWords()


def banner():
    print('''
\    /|_  _._|_ _ /\ ._ ._   | ._ _  _. _  _  |_) _ ._ _ |_  _ ._
 \/\/ | |(_| |__>/--\|_)|_) _|_| | |(_|(_|(/_ |_)(_)| | ||_)(/_| 
                     |  |               _|                       
                     _   
                    |_)  
                    |_)\/
                       / 
 _                   __                 
|_).__. _| _  _ ._  /__    _|o._  _._|_o
|  |(_|(_|(/_(/_|_) \_||_|(_|||_)(_| |_|
                |             |         

		''')


def send_attachment(image_path):
    try:
        # Attachment Drop Down Menu
        clipButton = driver.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/div/span')
        clipButton.click()
        time.sleep(1)

        # To send Videos and Images.
        mediaButton = driver.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[2]/span/div/div/ul/li[1]/button')
        mediaButton.click()
        time.sleep(3)

        autoit.control_focus("Open","Edit1")
        autoit.control_set_text("Open","Edit1",(image_path) )
        autoit.control_click("Open","Button1")
        time.sleep(6)

        whatsapp_send_button = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span[2]/div/div/span')
        whatsapp_send_button.click()
    except Exception as e:
        print(e)


def clearFolder():
    folder = os.getcwd() + '/downloads'
    print("Checking if Folder exists ")
    print(os.path.isdir(folder))
    if os.path.isdir(folder) == True:
        for the_file in os.listdir(folder):
            file_path = os.path.join(folder, the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path): shutil.rmtree(file_path)
                print("Cleaned the folder")
            except Exception as e:
                print(e)


def downloadImages(count,keyword):
    global keywordsList
    try:
        response = google_images_download.googleimagesdownload()  #class instantiation
        keywordsList = keyword
        print("Searching images using keyword -- "+keywordsList)
        arguments = {"keywords":keywordsList,"limit":count,"print_urls":False,"print_size":True,"size":'medium'}   #creating list of arguments
        absolute_image_paths = response.download(arguments)  #passing the arguments to the function
        # print(absolute_image_paths)  #printing absolute paths of the downloaded images
        return absolute_image_paths
    except Exception as e:
        print(e)


def sendMessage(msg):
    # Search for the message box and send the keys 
    msg_box = driver.find_element_by_xpath("//div[@class='_3u328 copyable-text selectable-text']")
    msg_box.send_keys(msg)
    # Search for the Send button and click on it
    button = driver.find_element_by_xpath("//button[@class='_3M-N-']")
    button.click()


def main():
    clearFolder()
    driver.get('https://web.whatsapp.com/')
    name = input('Enter the name of user or group: ')
    msg = input('Enter your message: ')
    count = int(input('Enter the count: '))
    # If you want a random word to be used
    # keywordsList = randomWordsGen.get_random_word()
    # If you want user entered keyword 
    keyword = input('Enter the Keyword for google search: ')
    # Download the images 
    absolute_image_paths = downloadImages(count, keyword)

    input('Enter any key after scanning QR code')
    
    # Search for the name and click on it
    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()

    # Dump the tuple into a JSON String 
    json_dump = json.dumps(absolute_image_paths)
    values = json.loads(json_dump)
    # print(values[0][keywordsList])
    # Get all the keys 
    keywordValues = values[0][keywordsList]
    # Send the images one by one 
    
    final_confirmation = input("START IMAGE ATTACK ? [Y/N]")
    if final_confirmation != "Y":
        print("Aborted!\n\n\n")
        
    else:
        for j in keywordValues:
            print(j)   
            send_attachment(j)
            time.sleep(3)
        final_confirmation = input("START Text Attack ? [Y/N]")
        if final_confirmation == "Y":
            k = 0;
            for i in range(count):
                seperator = ' '
                sendMessage("Message "+str(k)+" "+msg +" "+ seperator.join(randomWordsGen.get_random_words()))
                time.sleep(3)
                k=k+1
            


    # Bombing is complete now !
    print('Bombing Complete!!')




banner()
main()
clearFolder()