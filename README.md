# WhatsApp Bomber
Developed By [Pradeep Gudipati](https://github.com/pradeepgudipati)
 ``` Version 1.0 ```
 ``` 22/07/2019 ```

### Description
This program is a simple Whatsapp Bomber written using Selenium and python. It downloads random images from google and sends them along with text to the intended recepient 


### Requirements
* [Python 3](https://www.python.org/downloads/)
* pip 3

* Selenium 
    ```
    pip install -U selenium
    ```

* Download [Chrome Driver](http://chromedriver.chromium.org/downloads) and add to PATH

#### In order to use this program, download the driver and then add it to the PATH Environment Variable ...

### How to use in Windows
1. Download and install Python from https://python.org
2. Download my script WBomb_Chrome from here 
3. Install the required packages 
    * Install the Windows application [Autoit](https://www.autoitscript.com/site/autoit/downloads/) 
    * Download the [PyAutoit package](https://pypi.org/project/PyAutoIt/) and run below command (Do not try pip install as it fails) and run the below inside the unzipped folder
        ``` 
            python setup.py install
        ```     
    * Next install Random Word Generator 
        ```
            pip install random-word
        ```
    * Next install [Google Images downloader](https://google-images-download.readthedocs.io/en/latest/installation.html)
        ```
            pip install google_images_download
        ```

4. Run the program now ! 
    ```python
        py WA_Image_Text_Bomber.py
    ```
5. Login to WhatsApp using the QR Code
6. Enter the required values 
    ```
        Enter the name of user or group: <Name of the contact>
        Enter your message: <Message>
        Enter the count: <Number of messages to send>
        Enter the Keyword for google search: <Some random keyword>
    ```
7. When prompted enter Y *(Case sensitive)*
8. Done!

### Optional 
1. To run above program with Firefox, Download the Gecko driver and modify the code accordingly 
2. You can add additional parameters to google image downloader refer docs [here ](https://google-images-download.readthedocs.io/en/latest/arguments.html)


### Contacts
* Email : pradeepgudipati@gmail.com

### License
This program has been licensed under the GNU GPL v3 License.
