# I-can-see-you
A Honeypot in python with a web based dashboard made with flask to get live updates on the attacker activities

## ToDo
1) Add different services like ftp, etc and monitor
2) log commands executed by attacker
3) improve UI

## How to run
1) git clone
2) docker build -t i-can-see-you .
3) docker run -p 5000:5000 -p 2222:2222 i-can-see-you
4) Now visit the page in localhost:5000
5) try ssh into the ip and see the webpage
