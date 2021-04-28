class Command:

  command_list = ["quit", "exit", "save", "version", "login", "commands"]

  def __init__(self):
    pass

  @staticmethod
  def exit(main, player):
    main.quit()

  @staticmethod
  def quit(main, player):
    main.quit()

  @staticmethod
  def save(main, player):
    if (player):
      print("Saving player...")
      main.save_player()
      return True
    print("Player not loaded, unable to save.")
    return False

  @staticmethod
  def version(main, player):
    print("This is version 0.0.1.")
    return True

  @staticmethod
  def login(main, player):
    player_name = input("What is your player name? ")
    if (main.load_player(player_name)):
      print("Player loaded successfully.")
      return True
    else:
      print("Player does not exist.")
      return False

  @staticmethod
  def commands(main, player):
    print('Commands list: ') 
    for i in Command.command_list:
      print('\t' + i)
    return True
