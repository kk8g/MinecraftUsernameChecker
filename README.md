# How it works?
We use the already mojang API from the official publishers from minecraft. Then we can use this API to send request to return a valid response, Once we get the request back the data is sent to us and print to visualize what data we captured from the request we gave. For this instance we requested to check a list of usernames that arnt taken by already exsisting users. Then it is sent to Discord webhook where we can get a clearer output.
## Picture
![Picture](https://cdn.discordapp.com/attachments/1361127529913778277/1366167217431117834/image.png?ex=680ff5de&is=680ea45e&hm=484062c55f72f042d568c60798ac7b01e4c93238dfcbe8aee092fde8115097aa&)
![Picture](https://cdn.discordapp.com/attachments/1361127529913778277/1366167606473523230/image.png?ex=680ff63b&is=680ea4bb&hm=9ee8a48fb14578a1b864e397cc86e155f74e947d67813fb7bd3f760e32531c1f&)

## How to use
- Python must be installed

1. If you dont have python installed, download python 3.7.6
and make sure you click on the 'ADD TO PATH' option during
the installation.

2. Type ```pip install aiohttp``` in cmd

3.  Add the usernames you want to check in ```usernames.txt```. Do not put a lot of usernames because you can get rate limited and it can become more inaccurate. It is recommended to check around 500 usernames then wait 24 hours before you can check again.  

4.  Make sure you are in the same directory as the folder you downloaded it in.  Type
```python main.py``` in cmd to run

5. Once it is done running, available usernames will be saved in ```hits.txt```. 
