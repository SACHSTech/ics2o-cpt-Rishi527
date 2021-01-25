import random

def display_intro():
    title = "** The Tech Quiz **"
    print("*" * len(title))
    print(title)
    print("*" * len(title))


def display_menu():
    menu_list = ["1. Ransomware", "2. Trojan Horse", "3. Worms", "4. Spyware", "5. GPU", "6. CPU", "7. Memory", "8. Keyboard", "9. Random", "10. Exit"]
    print(menu_list[0])
    print(menu_list[1])
    print(menu_list[2])
    print(menu_list[3])
    print(menu_list[4])
    print(menu_list[5]) 
    print(menu_list[6])
    print(menu_list[7])
    print(menu_list[8])
    print(menu_list[9])



done = False
display_intro() 
display_menu()
while done == False:
  question = int(input("Enter a number: "))
  
  if question == 1:
    quiz_one = input("Ransomware payments are often demanded in the form of _____, which is like digital gold. (credit cards, bitcoin, checks, bank account numbers): ").lower()
    if quiz_one == "bitcoin":
      print("Correct")
    else: 
      print("Wrong")


  if question == 2:
    quiz_one = input("Trojan Horses create backdoor access to your computer info for ________. (anyone on the internet, the user who created the malware, everyone in your email address book, anyone with your email address): ").lower()
    if quiz_one == "the user who created the malware":
      print("Correct")
    else: 
      print("Wrong")

  if question == 3  :
    quiz_one = input("Which of the following is not a similarity between a worm and virus? (they both cause system or network slowdowns, they both hide in host programs or change their appearance to evade detection, they both can spread through the Internet, they both use host programs to replicate): ").lower()
    if quiz_one == "they both use host programs to replicate":
      print("Correct")
    else: 
      print("Wrong")

  if question == 4:
    quiz_one = input("_____ tracks information on a user's viewing habits while on the internet, and then sends that information to a remote computer without the user's knowledge. (buffer overflow, cross-site scripting, worm, spyware): ").lower()
    if quiz_one == "spyware":
      print("Correct")
    else: 
      print("Wrong")

  if question == 5:
    quiz_one = input("Which one of these terms apply to the GPU. (clock speed, refresh rate, switches, dpi): ").lower()
    if quiz_one == "clock speed":
      print("Correct")
    else: 
      print("Wrong")

  if question == 6:
    quiz_one = input("Which one of these terms apply to the CPU. (size, cores, watts, efficiency rating): ").lower()
    if quiz_one == "cores":
      print("Correct")
    else: 
      print("Wrong")

  if question == 7:
    quiz_one = input("Which provides the fastest data access time. (ROM, RAM, CD-ROM, HDD): ").lower()
    if quiz_one == "ram":
      print("Correct")
    else: 
      print("Wrong")

  if question == 8:
    quiz_one = input("Which one of these terms apply to keyboards. (switches, DPI, resolution, memory): ").lower()
    if quiz_one == "switches":
      print("Correct")
    else: 
      print("Wrong")   
