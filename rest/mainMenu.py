import os
import sys
import time

def escrita(texto):
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(0.09)

'''texto = 'Welcome to ancient History'
escrita(texto)'''

class GameMenu:
    def __init__(self):
        self.clear_screen()

    def clear_screen(self):
        if os.name == 'nt':  # Windows
            os.system('cls')
        else:  # Unix/Linux
            os.system('clear')

    def main_logo(self):
        print('')
        print("             _____________")
        print("       ,===:'.,            `-._")
        print("            `:.`---.__         `-._")
        print("              `:.     `--.         `.")
        print("                \.        `.         `.")
        print("       ( (,,(,   \.        `.    ____,-`.")
        print("     (,'     `/   \.   ,--.___`.'")
        print(" ,  ,'  ,--.  `,   \.;'         `")
        print("  `{D, {    \  :    \;           ;")
        print("    V,,'    /  /    //")
        print("    j;;    /  ,' ,-//.    ,---.      ,")
        print("    \;'   /  ,' /  _  \  /  _  \   ,'/")
        print("          \   `'  / \  `'  / \  `.' /")
        print("           `.__B,'   `.__,'   `.__,' ")
    
    def mage_character(self):
        print('')
        print('')
        print('              Mage          ')
        print('                            ')
        print('                  _,._      ')
        print("      .||,       /_ _\\     ")
        print("     \.`',/      |'L'| |    ")
        print("     = ,. =      | -,| L    ")
        print("     / || \    ,-'\"/,'`.   ")
        print("       ||     ;   `,,.  ;  ")
        print("       ||____,' , ,;' \| |  ")
        print("      (3|\    _/|/'   _| |  ")
        print("       ||/,-''  | >-'' _,\\ ")
        print("       ||'      ==\ ,-'  ,' ")
        print('')

    def mage_skills(self):
        print('    Skills: ')
        print('    3 - Ataque')
        print('    1 - Defesa')
        print('    2 - Ataque e Defesa')
        print('    8 - Magia')
        print('    5 - Sorte')
        print('Start with Mage?')
        print('[S]elect')
        print('Press any button to back')
        choose = input('').lower()
        if choose == 's':
            return ...
        else:
            return self.start()
        
        

    def assassin_character(self):
        print("             Assassin        ")
        print("      ____                   ")
        print("      |--|                   ")
        print("      |  |                   ")
        print("    _.+  +._                 ")
        print("   /\,)    /\                ")
        print("  :  `-._.'  ;               ")
        print("  |      '*--|               ")
        print("  | \        |               ")
        print("  |  `.      ;               ")
        print("  :         /|               ")
        print("  |\      -' |               ")
        print("  | `.       |               ")
        print("  :          |               ")
        print("")
    
    def assassin_skills(self):
        print('    Skills: ')
        print('    6 - Ataque')
        print('    2 - Defesa')
        print('    3 - Ataque e Defesa')
        print('    2 - Magia')
        print('    6 - Sorte')
        print('Start with Assassin?')
        print('[S]elect')
        print('Press any button to back')
        choose = input('').lower()
        if choose == 's':
            return ...
        else:
            return self.start()

    def warrior_character(self):
        print("                     .-'`-.")
        print("                    / | |   \ ")
        print("                   /  | |    \ ")
        print("                  |___|_|__  |")
        print("                  ||<o>| <o>`|")
        print("                  ||   J_   )|")
        print("                  `|`-'__`-'|/")
        print("                   |  `--'   \ ")
        print("                 .-|         |_")
        print("               .-'  \     /  | |`-.")
        print("            .-'      `.     /| |   \ ")
        print("           /           ````' | |    \ ")
        print("          |_____             | |     L")
        print("      .-' ___   `-.         F F  |  |")
        print("    .'.-'  |  `-.  `.      J J   /  |")

    def warrior_skills(self):
        print('Skills:')
        print('    5 - Ataque')
        print('    5 - Defesa')
        print('    4 - Ataque e Defesa')
        print('    1 - Magia')
        print('    3 - Sorte')
        print('Start with Warior?')
        print('[S]elect')
        print('Press any button to back')
        choose = input('').lower()
        if choose == 's':
            return ...
        else:
            return self.start()

    def barra(self):
        print('``------------------------------------´´')

    def barra2(self):
        print('..------------------------------------..')

    def main_name(self):
        print('            Ancient History            ')

    def main_name_init(self):
        texto = '       Welcome to ancient History \n'
        escrita(texto)

    def options(self):
        print('    > Play     [P]')
        print('    > Help     [H]')
        print('    > Quit     [Q]')

    def options_character(self):
        print("    Select your class     ")
        print("    > Mage         [M]    ")
        print("    > Assassin     [A]    ")
        print("    > Warrior      [W]    ")
    
    def mage(self):
        self.clear_screen()
        self.mage_character()
        self.barra()
        self.main_name()
        self.barra2()
        self.mage_skills()

    def assassin(self):
        self.clear_screen()
        self.assassin_character()
        self.barra()
        self.main_name()
        self.barra2()
        self.assassin_skills()

    def warrior(self):
        self.clear_screen()
        self.warrior_character()
        self.barra()
        self.main_name()
        self.barra2()
        self.warrior_skills()

    def help(self):
        self.clear_screen()
        self.main_logo()
        self.barra()
        self.main_name()
        self.barra2()

        help_text = input("""
            Welcome to Ancient History Help!

            This is a simple text-based game. In this game, you can choose to:

            1. Play the game and go on an adventure.
            2. Access the Help menu to learn more about the game.
            3. Quit the game.

            To play the game, select "Play" by entering 'P' in the menu.
            To access this Help menu, select "Help" by entering 'H' in the menu.
            To quit the game, select "Quit" by entering 'Q' in the menu.

            Have fun and enjoy your journey through Ancient History!

            Press Enter to return to the main menu...
        """)
        if help_text == '':
            return self.play()
        
        


    def play(self):
        self.clear_screen()
        self.main_logo()
        self.barra()
        self.main_name_init()
        self.barra2()
        self.options()
        
        first_pass = input('').lower()

        if first_pass == 'p':
            self.clear_screen()
            self.start()
        elif first_pass == 'h':
            self.help()  # Chama a função help
        elif first_pass == 'q':
            exit()
        else:
            print('Invalid option')
            return self.play()

    def start(self):
        self.clear_screen()
        self.main_logo()
        self.barra()
        self.main_name()
        self.barra2()
        self.options_character()
        character_select = input('').lower()
        if character_select == 'm':
            self.clear_screen()
            self.mage()
            self.init_name("mage")
        elif character_select == 'a':
            self.clear_screen()
            self.assassin()
            self.init_name("assassin")
        elif character_select == 'w':
            self.clear_screen()
            self.warrior()
            self.init_name("warrior")
        elif character_select == 'b':
            self.play()
        else:
            self.clear_screen()
            self.start()

    def init_name(self, character_name):
        self.clear_screen()
        print(f'    Congratulations, you decided to play with {character_name}')
        self.barra()
        name = input("    Your name will be: ")
        self.barra2()

        if character_name == "mage":
            self.mage_story(name)
        elif character_name == "assassin":
            self.assassin_story(name)
        elif character_name == "warrior":
            self.warrior_story(name)

    def mage_story(self, name):
        self.clear_screen()
        self.barra()
        print(f'    Welcome, {name} the Mage!')
        self.barra2()
        input("Press Enter to continue...")

        self.clear_screen()
        self.barra()
        print("    You are a powerful Mage on a quest to save the kingdom from the evil dragon.")
        print("    Your magic abilities will be your greatest asset.")
        self.barra2()
        input("Press Enter to continue...")

        # Adicione mais detalhes à história do Mage aqui...

    def assassin_story(self, name):
        self.clear_screen()
        self.barra()
        print(f'    Welcome, {name} the Assassin!')
        self.barra2()
        input("Press Enter to continue...")

        self.clear_screen()
        self.barra()
        print("    You are a stealthy Assassin tasked with eliminating the kingdom's enemies.")
        print("    Your agility and precision will be your keys to success.")
        self.barra2()
        input("Press Enter to continue...")

        # Adicione mais detalhes à história do Assassino aqui...

    def warrior_story(self, name):
        self.clear_screen()
        self.barra()
        print(f'    Welcome, {name} the Warrior!')
        self.barra2()
        input("Press Enter to continue...")

        self.clear_screen()
        self.barra()
        print("    You are a fearless Warrior chosen to defend the kingdom against its foes.")
        print("    Your strength and bravery will be your greatest weapons.")
        self.barra2()
        input(" Press Enter to continue...")


menu = GameMenu()
menu.play()