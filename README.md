# gdrive-url-to-path
Returns the full path of a Google Drive file based on its URL.

# Installation
Install the dependencies:
sudo apt install xclip python3-pip
pip3 install -r requirements.txt

Create a OAuth Client ID for "Google Drive URL to Path":
https://console.cloud.google.com/apis/credentials?project=gdrive-url-to-path-1

Download the file and rename it to ~/google-credential.json

Copy gdp and gdrive_url_to_path.py to a folder in your $PATH. For instance:
sudo cp gdp gdrive_url_to_path.py /usr/local/bin

To confirm it works:
gdrive_url_to_path.py http://fdsfdsffdsfdfdf

On the first time, it will ask you to login with your google account (if you have
multiple accounts, use the one you want to search in Google Drive).
It will ask you to accept the connection on the first time.

# Usage
gdrive_url_to_path.py <url>
-> Output the full path

Or:
Copy the URL to the clipboard.
gdp
<wait a few seconds>
The clipboard countains the full path.
