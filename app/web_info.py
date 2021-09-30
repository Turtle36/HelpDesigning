import urllib.request
import urllib.parse
import colorama

print(
    colorama.Back.LIGHTWHITE_EX + colorama.Fore.WHITE + "______" + colorama.Fore.LIGHTBLUE_EX + "WEBINFO" + colorama.Fore.WHITE + "______")
jawab = 'y'
while (jawab == 'y'):
    post_url = input(colorama.Fore.LIGHTBLACK_EX + "URL: ")

    post_response = urllib.request.urlopen(url=post_url)
    print(post_response.info())

    running = True
    while running:
        a = input("ulang lagi (y/n): ")
        if a == 'y':
            running = False
        elif a == 'n':
            jawab = 'n'; running = False
        else:
            running = True
