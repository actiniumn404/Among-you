#Among You.py Made by Andrew Chen and W W. Wu. AndrewChen51 on repl, AndrewC10 on AoPS. Wuwang2002 on AoPS, WWWtheW on repl. DO NOT REMOVE THIS LINE
import random
import time
import math


class among_you():
    def __init__(self):
      #variables
        print("Among You.py Made by Andrew Chen and W. W. Wu.\nAndrewC10 on AoPS, AndrewChen51 on REPL.it\nWuwang2002 on AoPS, WWWtheW on REPL.it")
        self.map = input("What map would you like? ").lower()
        self.time1 = ""
        self.time2 = ""
        self.sabatoge = "no"
        self.forthesakeofturningthisonagain = ['no', 'no', 'no']
        self.comms = "affirmative"
        self.lights = "affirmative"
        self.reactor = "affirmative"
        #self.oxygen = "affirmative"
        self.non_reported = {}
        self.reactortimer = ""
        self.me = ''
        self.mrs = 1
        self.players = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "lime", "cyan", "brown", "black",
                        "white", "gray", "silver", "gold", "teal", "tan", "violet", "maroon", "olive"]
        self.backup = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "lime", "cyan", "brown", "black",
                       "white", "gray", "silver", "gold", "teal", "tan", "violet", "maroon", "olive"]
        self.players_dead = []
        self.imposters = []
        if self.map == "skeld" or self.map == "the skeld":
          self.current_room = "cafeteria"
          self.rooms = ["cafeteria", "medbay", "reactor", "security", "electrical", "storage", "admin","shields", "navigation", "oxygen", "weapons", "comms", "engine"]
          self.extra_rooms = ["cafe","cams","elec","navi","o2","lights"]
          self.download_data_location = random.choice(["cafeteria","navigation","comms","electrical","weapons"])
          self.tasks = ["medbay - scan", self.download_data_location+" - download data", "shields - prime shields", "reactor - unlock manifolds", "storage - refuel", "navigation - chart course", "navigation - stabilize steering", "oxygen - empty garbage","engine - align output", "electrical - calibrate distributor", "electrical - divert power", "reactor - start reactor", "admin - swipe card", "weapons - clear asteroids", "oxygen - clean o2 filter", "medbay - inspect sample", "electrical - fix wiring"]
          self.move_rooms = {
            "cafeteria":["admin","storage","medbay","engine","weapons"],
            "admin":["cafeteria","storage"],
            "storage":["admin","cafeteria","comms","shields","electrical"],
            "comms":["storage","shields"],
            "shields":["comms","storage","navigation"],
            "navigation":["oxygen","shields","weapons"],
            "oxygen":["weapons","cafeteria","navigation"],
            "electrical":["storage","engine"],
            "engine":["electrical, storage","reactor","security","medbay","cafeteria"],
            "reactor":["engine","security"],
            "security":["engine","reactor"],
            "weapons":["cafeteria","oxygen","navigation"],
            "medbay":["engine","cafeteria"]
          }
          self.cams_rooms = ['admin', 'reactor', 'oxygen', 'medbay']
          self.map = "skeld"
          self.ventable = ["cafeteria", "medbay", "reactor", "security", "electrical", "admin","shields", "navigation", "weapons", "engine"]
          self.vents = {
            "cafeteria":["shields","admin"],
            "admin":["cafeteria","shields"],
            "navigation":["weapons","shields"],
            "weapons":["navigation"],
            "shields":["navigation","cafeteria","admin"],
            "reactor":["engine"],
            "security":["medbay","electrical"],
            "medbay":["security","electrical"],
            "electrical":["security","medbay"]
          }
          self.divertpowerroom = ""
        if self.map == "mira" or self.map == "mira hq":
          self.current_room = "launchpad"
          self.rooms = ["launchpad", "medbay", "comms", "locker room", "office", "admin", "balcony", "cafeteria", "decontamination", "lab", "reactor", "storage", "greenhouse", "launchpad hallway", "doorlog hallway"]
          self.download_data_location = random.choice(["office"])
          self.tasks = ["lab - assemble artifact", "cafeteria - buy beverage", "admin - chart course", "greenhouse - clean o2 filter", "balcony - clear asteroids", "reactor - divert power", "cafeteria - empty garbage", "admin - enter id code", "locker room - fix wiring", "launchpad - fuel engines", "balcony - measure weather", "admin - prime shields", self.download_data_location+" - process data","launchpad - run diagnostics", "lab - sort samples", "reactor - start reactor", "medbay - scan", "reactor - unlock manifolds", "storage - retrieve watering can"]
          self.move_rooms = {
            "launchpad":["launchpad hallway"],
            "medbay":["comms","locker room","doorlog hallway","launchpad hallway"],
            "comms":["doorlog hallway","medbay","locker room","launchpad hallway"],
            "locker room":["decontamination","doorlog hallway","medbay","comms","launchpad hallway"],
            "office":["doorlog hallway","admin","greenhouse"],
            "admin":["doorlog hallway","office","greenhouse"],
            "balcony":["cafeteria","storage"],
            "cafeteria":["balcony","doorlog hallway","storage"],
            "decontamination":["reactor","locker room","lab"],
            "lab":["reactor","decontamination"],
            "reactor":["decontamination","lab"],
            "storage":["balcony","cafeteria"],
            "greenhouse":["admin","office","doorlog hallway"],
            "launchpad hallway":["launchpad","locker room","medbay","comms","doorlog hallway"],
            "doorlog hallway":["locker room","comms","medbay","launchpad hallway","office","greenhouse","admin","cafeteria"]
          }
          self.extra_rooms = ["oxygen","cafe","doorlog","decontam","o2"]
          self.ventable = ["launchpad","locker room","decontamination","lab","reactor","medbay","doorlog hallway","balcony","office","greenhouse","admin"]
          self.map = "mira hq"
          self.divertpowerroom = ""
        self.task_completed = []
        self.hascommsbeendown = "no"
        self.haslightsbeendown = "no"
        self.hasreactorbeendown = "no"
        #self.hasoxygenbeendown = "no"

        #input questions
        while True:
            self.me = str(input("You are waiting in the lobby, what is your player color ")).strip().lower()
            if self.me not in self.players:
                print("Sorry, that color is not available")
            else:
                break
        self.players.remove(self.me)
        self.num_emergencies = int(input("How many emergency meetings? "))
        while True:
          self.num_imposter = int(input("How many imposters? "))
          if self.num_imposter >= 6:
            continue
          else:
            break
        self.num_emergencies_left = self.num_emergencies
        self.time1 = ""
        self.impostor_or_not = input("Would you like to be Impostor? yes/no ").strip().lower()
        if self.impostor_or_not == "no":
          while True:
            self.num_task = int(input("How many tasks? Minimum 7 tasks, max "+str(len(self.tasks))+" "))
            if self.num_task >= 7 and self.num_task <= len(self.tasks):
              break
            else:
              print("Minimum 7 tasks")
          print("The game has started\nThere are", self.num_imposter, "imposters among us")
          self.select_roles()
        if self.impostor_or_not == "yes":
          while True:
            self.kill_cooldown = float(input("How long of a kill cooldown? Minimum 10 seconds "))
            self.backup_kill_cooldown = self.kill_cooldown
            if self.backup_kill_cooldown >= 10:
              break
            else:
              print("Minimum is 10")
          if self.num_imposter != 1:
            for x in range(1, self.num_imposter):
              ranchoice = random.choice(self.players)
              self.imposters.append(ranchoice)
              self.players.remove(ranchoice)
            print("You are an Impostor with ",", ".join(self.imposters))
            self.imposters.append(self.me)
          self.impostor_main()
        else:
          print("That is not an answer")


    def select_roles(self):
        self.task_list = []
        while True:  # imposter roles
            VARtmp = random.choice(self.players)  # Var tmp means varable temporary
            if VARtmp == self.me or VARtmp in self.imposters:
                continue
            if len(self.imposters) == self.num_imposter:
                break
            self.imposters.append(VARtmp)
            self.players.remove(VARtmp)
        while True:
            VARtmp = random.choice(self.tasks)
            self.task_list.append(VARtmp)
            self.tasks.remove(VARtmp)
            if len(self.task_list) == self.num_task:
                self.main()
                break
                
    def investigate(self, VARroomie):
      if ((self.mrs == 1) and (VARroomie in self.move_rooms[self.current_room])) or (self.mrs == 0):
        self.current_room = VARroomie
        if self.lights == "affirmative":
            vented = int(random.randint(1, 5))
            body = int(random.randint(1, 5))
            if VARroomie in self.non_reported:
                print("You go to", VARroomie, "and find", self.non_reported[VARroomie] + "'s body on the floor")
            if vented == 2 and self.current_room in self.ventable:
                print("You caught", random.choice(self.imposters), "venting in", VARroomie)
            if body == 5:
                if VARroomie not in self.non_reported:
                    ded_body = random.choice(self.players)
                    print("You go to", VARroomie, "and find", ded_body + "'s body on the floor")
                    self.players.remove(ded_body)
                    self.backup.remove(ded_body)
                    self.players_dead.append(ded_body)
                    self.non_reported[VARroomie] = ded_body
            if int(random.randint(1, 3)) == 4:
                print("Suddenly the doors close and and an imposter jumps out of the vent and kills you")
                self.text_anime(
                    "Defeat\nThere are " + str(len(self.imposters)) + " remaining\nThere imposters were: " + ", ".join(
                        self.imposters), 0.07)
                exit()
            else:
                print("You go to", VARroomie, "and look around, but there seems to be nothing there")
                if self.map == "skeld":
                  VARsabotage = random.randint(1,7)
                  if VARsabotage == 1:
                  #and self.hascommsbeendown == "no"
                    self.comms = ""
                    #self.hascommsbeendown = "yes"
                    self.sab("comms")
                  if VARsabotage == 2:
                  #and self.haslightsbeendown == "no"
                    self.lights = ""
                    #self.haslightsbeendown = "yes"
                    self.sab("lights")
                  if VARsabotage == 3:
                  #and self.hasreactorbeendown == "no"
                    self.reactor = ""
                    #self.hasreactorbeendown = "yes"
                    self.sab("reactor")
                if self.map == "mira hq":
                  VARsabotage = random.randint(1,7)
                  if VARsabotage == 1:
                    self.reactor = ""
                    self.sab("reactor")
                  if VARsabotage == 2:
                    self.lights = ""
                    self.sab("lights")
      else:
        print("You may not move to that room")

    def emergency_meeting(self):
        if self.num_emergencies_left == 0:
          print("Sorry, you have no emergency meetings left.")
        if self.sabatoge == "yes":
          print("You may not call an emergency meeting as the sabotage has not been fixed.")
        else:
          while True:
            self.current_room = "cafeteria"
            print("\nYou press the button and everyone is teleported to the cafeteria")
            print("The following are alive:", ", ".join(self.backup))
            print("The following are dead:", ", ".join(self.players_dead))
            VAReject = input("who do you want to eject? ").strip().lower()
            if VAReject not in self.backup:
                print("No such player")
            else:
                if VAReject == self.me:
                    self.text_anime("You ejected youself!!!\nDefeat\nThere are " + str(len(self.imposters)) + " remaining\nThere imposters were: " + ", ".join(self.imposters), 0.07)
                    exit()
                if VAReject == "skip":
                    self.text_anime("No one was ejected (skipped)\n\n", .07)
                elif VAReject not in self.imposters and VAReject in self.backup:
                    self.text_anime("{} was not an imposter\n\n".format(VAReject), .07)
                    self.players.remove(VAReject)
                    self.backup.remove(VAReject)
                    self.players_dead.append(VAReject)
                else:
                    self.text_anime("{} was an imposter\n\n".format(VAReject), .07)
                    self.imposters.remove(VAReject)
                print(len(self.imposters), "imposters remain")
                self.num_emergencies_left += -1
                break
    
    def report_body(self):
      while True:
        self.reactor = "affirmative"
        self.sabatoge = "no"
        self.hasreactorbeendown = "yes"
        self.current_room = "cafeteria"
        print("You report the body and everyone is teleported to the cafeteria")
        print("The following are alive:", ", ".join(self.backup))
        print("The following are dead:", ", ".join(self.players_dead))
        VAReject = input("who do you want to eject? ").strip().lower()
        if VAReject not in self.backup:
            print("No such player")
        else:
            if VAReject == self.me:
                self.text_anime("You ejected youself!!!\nDefeat\nThere are " + str(len(self.imposters)) + " remaining\nThere imposters were: " + ", ".join(self.imposters), 0.07)
                exit()
            if VAReject == "skip":
                self.text_anime("No one was ejected (skipped)\n\n", .07)
            elif VAReject not in self.imposters and VAReject in self.backup:
                self.text_anime("{} was not an imposter\n\n".format(VAReject), .07)
                self.players.remove(VAReject)
                self.backup.remove(VAReject)
                self.players_dead.append(VAReject)
            else:
                self.text_anime("{} was an imposter\n\n".format(VAReject), .07)
                self.imposters.remove(VAReject)
            print(len(self.imposters), "imposters remain")
            break

    def text_anime(self, text, timee):
        for char in text:
            print(char, end='')
            time.sleep(timee)
    
    def crewmate_report(self, person_who_reported, number_people_in_room):
      sus = random.randint(0, number_people_in_room)
      if sus == 0:
        if person_who_reported in self.backup:
          self.text_anime("{} was not an imposter\n\n".format(person_who_reported), .07)
          self.players.remove(person_who_reported)
          self.backup.remove(person_who_reported)
          self.players_dead.append(person_who_reported)
      if sus == 1:
        self.text_anime("No one was ejected (skipped)\n\n", .07)
      if sus > 1:
        self.text_anime("{} was an imposter\n\n".format(self.me), .07)
        self.text_anime("You were ejected.\nDefeat.",0.07)
        exit()

    def bfs(self, graph, start, end):
      queue = [(start, [])]
      while queue:
        point, path = queue.pop(0)
        if point == end:
            return self.copy_add(path, point)
        for nextpoint in graph[point]:
            new_path = self.copy_add(path, point)
            queue.append((nextpoint, new_path))
      return []

    def copy_add(self, path, point):
        new_path = path[:]
        new_path.append(point)
        return new_path

    def main(self):
        while True:
            if len(self.imposters) == 0:
                print("Victory!")
                break
            if len(self.imposters) > len(self.players):
                self.text_anime("Defeat #of imps > #of players\nThere are " + str(len(self.imposters)) + " remaining\nThere imposters were: " + ", ".join(self.imposters), 0.07)
            room = input("What room would you like to go to? (type /help to get help, \ntype /moveto to get list of rooms you can move to)\n").strip().lower()
            if room == "/moveto":
              print(", ".join(self.move_rooms[self.current_room]))
            if room == "/tasklist":
                if self.comms == "affirmative":
                    print("\n".join(self.task_list))
                else:
                    print("[Comms sabatoged. please go to comms and type: /fix]")
            if room[:5] == "/task":
                self.task(room[6:])
            if room[:4] == "/bfs":
                print(self.bfs(self.move_rooms,self.current_room, room[5:]))
            if room[:3] == "/re":
                self.resourse(room[4:])
            if (room == "/report") and (self.current_room in self.non_reported):
                self.non_reported.pop(self.current_room)
                self.report_body()
            if room == "/fix":
                self.sab("fix" + self.current_room)
            if room == "/help":
                print("\nHelp is here!\n/tasklist\t-\tList of tasks\n/task emergency\t-\tCalls an emergency meeting\t(Can only be triggered in cafeteria)\n/fix\t-\tFix a sabotage\n/report\t-\treport a body")
                print("\nHow to do a task\n\nFirst do /tasklist to get list of tasks \nGo to the room labeled before the dash\nLastly do \"/task [the word after the dash]\"\n")
                print("\nList of rooms\n"+", ".join(self.rooms)+"\n\n")
            if self.reactor != "affirmative" and time.time() - self.reactortimer >= 40:
              print("Reactor has blown up the ship.")
              self.text_anime("Defeat\nThere are " + str(len(self.imposters)) + " remaining\nThere imposters were: " + ", ".join(self.imposters), 0.07)
              exit()
            elif room not in self.rooms and room not in self.extra_rooms and room not in ["/tasklist", "/task", "/fix", "/help"]:
                print("\nThere is no such room")
                continue
            elif room in self.rooms:
              if self.mrs == 1 and room in self.move_rooms[self.current_room]:
                self.investigate(room)
                time.sleep(0.5)
              if self.mrs == 0:
                self.investigate(room)
                time.sleep(0.5)
            elif self.map == "skeld":
              if room == "cafe":
                  self.investigate("cafeteria")
              elif room == "cams":
                  self.investigate("security")
              elif room == "elec" or room == "lights":
                  self.investigate("electrical")
              elif room == "navi":
                  self.investigate("navigation")
              elif room == "o2":
                  self.investigate("oxygen")
            elif self.map == "mira hq":
              if room == "cafe":
                self.investigate("cafeteria")
              elif room == "oxygen" or room == "o2":
                self.investigate("greenhouse")
              elif room == "doorlog":
                self.investigate("comms")
              elif room == "decontam":
                self.investigate("decontamination")
    
    def impostor_investigate(self,VARroom):
      if (self.mrs == 0) or (self.mrs == 1 and (VARroom in self.move_rooms[self.current_room])):
        if self.kill_cooldown > 5:
          VARtmp = random.randint(1,10)
          self.kill_cooldown += -VARtmp/2
          print("Please wait a kill cooldown of", self.kill_cooldown, "seconds till your next move")
          self.current_room = VARroom
          victims = []
          number_people_in_room = random.randint(0, 3)
          if number_people_in_room != 0:
            for x in range(number_people_in_room):
              victims.append(random.choice(self.players))
          print("You go into", VARroom, "and find: ", ", ".join(victims) + " in there.")
          if self.current_room in self.non_reported:
            print("The dead bodies in the room are ",self.non_reported[self.current_room])
        else:
          self.kill_cooldown = 0
          self.current_room = VARroom
          victims = []
          number_people_in_room = random.randint(0, 4)
          if number_people_in_room != 0:
            while True:
              ranperson = random.choice(self.players)
              if len(victims) == number_people_in_room:
                break
              if ranperson in victims:
                continue
              else:
                victims.append(ranperson)
            joined_victims = ", ".join(victims)
            print("You go into", VARroom, "and find: " + joined_victims + " in there.")
            if self.current_room in self.non_reported:
              print("The dead bodies in the room are ",self.non_reported[self.current_room])
            kill = input("Would you like to kill? yes/no ").lower().strip()
            if (kill == "yes") and (self.current_room not in self.non_reported):
              while True:
                killed = input("Who would you like to kill? People you can kill are: "+", ".join(victims)+" ")
                if killed in victims:
                  self.players.remove(killed)
                  self.players_dead.append(killed)
                  self.backup.remove(killed)
                  self.non_reported[VARroom] = killed
                  self.kill_cooldown = self.backup_kill_cooldown
                  break
                else:
                  print("That is not in the room")
              if self.lights != "affirmative":
                if number_people_in_room > 1:
                  saw  = random.randint(1, 3)
                  report = random.randint(1, 4)
                  if saw == 1 or saw == 2:
                    if report != 1:
                      if self.lights == "affirmative":
                        self.crewmate_report(random.choice(victims),number_people_in_room+1)
            for i in range(self.num_imposter):
              other_imps_kill = random.randint(1,10)
              if other_imps_kill == 1:
                print("Your kill button just flashed!")
                room = self.rooms
                for i in list(self.non_reported):
                  if i not in room:
                    room.remove(i)
                  else:
                    pass
                for x in range(self.num_imposter-1):
                  room_kill = random.choice(room)
                  person_kill = random.choice(self.players)
                  self.players.remove(person_kill)
                  self.players_dead.append(person_kill)
                  self.backup.remove(person_kill)
                  self.non_reported[room_kill] = person_kill
                  break
          else:
            print("No one is in", VARroom)
    
    def impostor_main(self):
      while True:
        room = input("What room would you like to go to? ")
        if room[:3] == "/re":
          self.resourse(room[4:])
        if room[:4] == "/bfs":
          print(self.bfs(self.move_rooms,self.current_room, room[5:]))
        if room[:5] == "/vent":
          ventroom = room[6:]
          if (self.current_room in self.ventable) and (((self.map == "skeld") and (ventroom in self.vents[self.current_room])) or (self.map == "mira hq" and self.current_room in self.ventable)):
            self.current_room = ventroom
            print("You have vented to "+ventroom)
        if room[:7] == "/moveto":
          print(", ".join(self.move_rooms[self.current_room]))
        elif self.map == "skeld" and (room in self.move_rooms[self.current_room]):
          if room == "elec" or room == "lights":
            self.impostor_investigate("electrical")
          elif room == "cams":
            self.impostor_investigate("security")
          elif room == "o2":
            self.impostor_investigate("oxygen")
          elif room == "navi":
            self.impostor_investigate("navigation")
          elif room == "cafe":
            self.impostor_investigate("cafeteria")
        elif self.map == "mira hq":
          if room == "decontam":
            self.impostor_investigate("decontamination")
          elif room == "doorlog":
            self.impostor_investigate("comms")
          elif room == "oxygen" and room == "o2":
            self.impostor_investigate("greenhouse")
          elif room == "cafe":
            self.impostor_investigate("cafeteria")
        if len(self.imposters) > len(self.players):
          print("Victory!")
          exit()
        if room == "/fix":
          self.sab("fix" + self.current_room)
        if self.map == "mira hq":
          if room == "/sab reactor" and self.sabatoge != "yes":
            self.sab("reactor")
          if room == "/sab lights" and self.sabatoge != "yes":
            self.sab("lights")
          if room == "/sab comms" and self.sabatoge != "yes":
            self.sab("comms")
        if (room == "/report") and (self.current_room in self.non_reported):
          self.non_reported.pop(self.current_room)
          self.impostor_report()
        if self.current_room == "cafeteria" and room == "/task emergency" and self.sabatoge != "yes":
            self.impostor_emergency()
        if self.reactor != "affirmative":
          if random.randint(1, 5) != 1:
            print("Reactor has been fixed.")
            self.reactor = "affirmative"
            self.sabatoge = "no"
            self.reactortimer = float('inf')
            if self.impostor_or_not == "no":
              pass
        elif room not in self.rooms:
            print("There is no such room")
            continue
        else:
          self.impostor_investigate(room)

    def impostor_report(self):
      while True:
        self.current_room = "cafeteria"
        print("You report the body and everyone is teleported to the cafeteria")
        print("The following are alive:", ", ".join(self.backup))
        print("The following are dead:", ", ".join(self.players_dead))
        VAReject = input("who do you want to eject? ").strip().lower()
        if VAReject not in self.backup and VAReject not in ["skip"]:
            print("No such player")
        else:
            if VAReject == self.me:
                self.text_anime("You ejected youself!!!\nDefeat", 0.07)
                exit()
            if VAReject == "skip":
                self.text_anime("No one was ejected (skipped)\n\n", .07)
                print(len(self.imposters)+1, "imposters remain")
            elif VAReject not in self.imposters and VAReject in self.backup:
                self.text_anime("{} was not an imposter\n\n".format(VAReject), .07)
                self.players.remove(VAReject)
                self.backup.remove(VAReject)
                self.players_dead.append(VAReject)
                print(len(self.imposters), "imposters remain")
            else:
                self.text_anime("{} was an imposter\n\n".format(VAReject), .07)
                self.imposters.remove(VAReject)
                self.players.remove(VAReject)
                print(len(self.imposters), "imposters remain")
            break

    def impostor_emergency(self):
      while True:
        self.current_room = "cafeteria"
        print("You report the body and everyone is teleported to the cafeteria")
        print("The following are alive:", ", ".join(self.backup))
        print("The following are dead:", ", ".join(self.players_dead))
        VAReject = input("who do you want to eject? ").strip().lower()
        if VAReject not in self.backup:
            print("No such player")
        else:
            if VAReject == self.me:
                self.text_anime("You ejected youself!!!\nDefeat", 0.07)
                exit()
            if VAReject == "skip":
                self.text_anime("No one was ejected (skipped)\n\n", .07)
            elif VAReject not in self.imposters and VAReject in self.backup:
                self.text_anime("{} was not an imposter\n\n".format(VAReject), .07)
                self.players.remove(VAReject)
                self.backup.remove(VAReject)
                self.players_dead.append(VAReject)
            else:
                self.text_anime("{} was an imposter\n\n".format(VAReject), .07)
                self.imposters.remove(VAReject)
            print(len(self.imposters)+1, "imposters remain")
            self.num_emergencies_left += -1
            break

    def task(self, task):
        if self.current_room == "cafeteria" and task == "emergency" and self.sabatoge != "yes":
            self.emergency_meeting()
        if self.current_room+" - "+task in self.task_list:
            if self.current_room == "medbay" and task == "scan":
                self.text_anime("Id:" + self.me + "04\nHeight:3 feet 6 inches\nWeight:92 pounds\nBlood Type:AB+\nScan Complete In 5\n4\n3\n2\n1\nScan Complete\n",0.1)
                self.task_list.remove(self.current_room + " - " + task)
                self.task_completed.append(self.current_room + " - " + task)
            if self.current_room == self.download_data_location and task == "download data":
                self.text_anime("Estimated time: 9h21m\n8h1m\n6h41m\n3h50m\n5\n4\n3\n2\n1\n", 0.12)
                self.task_list.remove(self.current_room+" - "+task)
                self.task_list.append("admin - upload data")
            if self.current_room == "admin" and task == "upload data":
                self.text_anime("Estimated time: 9h21m\n8h1m\n6h41m\n3h50m\n5\n4\n3\n2\n1\n", 0.12)
                self.task_list.remove(self.current_room + " - " + task)
                self.task_completed.append(self.current_room + " - " + task)
            if ((self.current_room == "shields" and self.map == "skeld") or (self.current_room == "admin" and self.map == "mira hq")) and task == "prime shields":
                primeshieldslist = []
                while True:
                    VARtmp = random.randint(1, 7)
                    if VARtmp in primeshieldslist:
                        continue
                    if len(primeshieldslist) == 4:
                        break
                    else:
                        primeshieldslist.append(VARtmp)
                while True:
                    VARtmp = int(input(">>> "))
                    if VARtmp not in primeshieldslist:
                        print("Sorry you didn't get one, try again", len(primeshieldslist), "to go")
                    if VARtmp in primeshieldslist:
                        primeshieldslist.remove(VARtmp)
                        print("You got one!", str(len(primeshieldslist)), "to go")
                    if len(primeshieldslist) == 0:
                        self.task_list.remove(self.current_room + " - " + task)
                        self.task_completed.append(self.current_room + " - " + task)
                        break
            if self.current_room == "reactor" and task == "unlock manifolds":
                while True:
                    VARtmp = int(input("Type in the numbers from 1 to 10. no spaces "))
                    if VARtmp == 12345678910:
                        self.text_anime("Task Complete", 0.07)
                        self.task_list.remove(self.current_room + " - " + task)
                        self.task_completed.append(self.current_room + " - " + task)
                        break
                    else:
                        print("Please type again")
        if self.current_room == "storage" and task == "refuel":
            while True:
                VARtmp = input("type /start to start ").strip()
                if VARtmp == "/start":
                    for x in range(9, 0, -1):
                        print(x, "seconds remaining")
                        time.sleep(1)
                    print("Task Complete")
                    self.task_list.remove(self.current_room + " - " + task)
                    self.task_list.append("engine - refuel")
                    break
                else:
                    print("Please try again")
        if self.current_room == "engine" and task == "refuel":
            while True:
                VARtmp = input("type /start to start ").strip()
                if VARtmp == "/start":
                    for x in range(9, 0, -1):
                        print(x, "seconds remaining")
                        time.sleep(1)
                    print("Task Complete")
                    self.task_list.remove(self.current_room + " - " + task)
                    self.task_completed.append("engine, storage - refuel")
                    break
                else:
                    print("Please try again")
        if ((self.current_room == "navigation" and self.map == "skeld") or (self.current_room == "admin" and self.map == "mira hq")) and task == "chart course":
            VARtmp = input("To chart course select 4 locations. list the numbers from 1-4 ")
            if VARtmp == "1234":
                self.task_list.remove(self.current_room + " - " + task)
                self.task_completed.append(self.current_room + " - " + task)
                print("Task Complete")
            else:
                self.task("chart course")
        if self.current_room == "navigation" and task == "stabilize steering":
            VARtmp = input("what coordinates are the origin? do in the format: (x, y) ")
            if VARtmp == "(0, 0)":
                print("Task complete")
                self.task_list.remove(self.current_room + " - " + task)
                self.task_completed.append(self.current_room + " - " + task)
            else:
                self.task("stabilize steering")
        if self.current_room == "oxygen" and task == "empty garbage":
            VARtmp = input("enter /pull to pull the lever ")
            if VARtmp == "/pull":
                print("Emptying garbage...\nTask Complete")
                self.task_list.remove("oxygen - empty garbage")
                self.task_list.append("storage - empty garbage")
            else:
                self.task("empty garbage")
        if self.current_room == "storage" and task == "empty garbage":
            VARtmp = input("enter /pull to pull the lever ")
            if VARtmp == "/pull":
                print("Emptying garbage...\nTask Complete")
                self.task_list.remove(self.current_room+" - " + task)
                self.task_completed.append("storage, oxygen - empty garbage")
            else:
                self.task("empty garbage")
        if self.current_room == "engine" and task == "align output":
            VARtmp = input("What angle should we align at? ")
            if VARtmp == "0":
                self.text_anime("Task complete", 0.07)
                self.task_list.remove(self.current_room + " - " + task)
                self.task_completed.append("engine - align output")
            else:
                self.text_anime("Task complete", 0.07)
                self.task("align output")

        if self.current_room == "electrical" and task == "calibrate distributor":
            while True:
                VARtmp = input('Type "click" ')
                if VARtmp == "click":
                    VARtmp2 = random.randint(0, 4)
                    if VARtmp2 == 0:
                        self.text_anime("Task Complete", 0.07)
                        self.task_list.remove(self.current_room + " - " + task)
                        self.task_completed.append("electrical - calibrate distributor")
                        break
                    else:
                        self.text_anime("Try again please", 0.07)
        if self.current_room == "electrical" and task == "divert power":
            while True:
                self.divertpowerroom = random.choice(["engine", "weapons", "shields", "navigation", "comms", "oxygen", "security"])
                VARtmp = input("Type /pull to pull the lever to " + self.divertpowerroom+" ")
                if VARtmp == "/pull":
                    self.text_anime("Task Complete", 0.07)
                    self.task_list.remove("electrical - divert power")
                    self.task_list.append(self.divertpowerroom+" - divert power")
                    break
        if self.current_room == self.divertpowerroom and task == "divert power":
            while True:
                VARtmp = input("Type /pull to pull to accept the power ")
                if VARtmp == "/pull":
                    self.text_anime("Task Complete", 0.07)
                    self.task_list.remove(self.current_room + " - " + task)
                    self.task_completed.append("electrical - divert power")
                    break
        if self.current_room == "reactor" and task == "start reactor":
          numbers = []
          for x in range(1, 6):
            numbers.append(str(random.randint(1,9)))
            while True:
              VARtmp = input("Enter this sequence, without spaces"+" "+"".join(numbers)+" ")
              if VARtmp == "".join(numbers):
                print("you got one!")
                break
              else:
                print("please try again")
          self.text_anime("Task Complete",0.07)
          self.task_list.remove("reactor - start reactor")
          self.task_completed.append("reactor - start reactor")
          
        if self.current_room == "admin" and task == "swipe card":
          while True:
            VARtmp = input("Type /swipe to swipe card ")
            if VARtmp == "/swipe":
              VARtmp2 = random.randint(1,4)
              if VARtmp2 == 1:
                print("Bad read. Try Again.")
              if VARtmp2 == 2:
                print("Too fast. Try Again.")
              if VARtmp2 == 3:
                print("Too slow. Try Again.")
              if VARtmp2 == 4:
                print("Accepted. Thank you.")
                self.text_anime("Task Complete", 0.07)
                self.task_list.remove("admin - swipe card")
                self.task_completed.append("reactor - start reactor")
                break
        if (self.current_room == "weapons" or (self.current_room == "balcony")) and task == "clear asteroids":
          VARtmp = input("\nType /start to start ")
          if VARtmp == "/start":
            for k in range(21):
              print("Shooting asteroids..."+str(k)+" complete")
              time.sleep(0.5)
            self.text_anime("Task Complete", 0.07)
            self.task_list.remove(self.current_room + " - clear asteroids")
            self.task_completed.append(self.current_room+" - clear asteroids")
        if (self.current_room == "oxygen" or (self.current_room == "greenhouse" and self.map == "mira hq")) and task == "clean o2 filter":
          VARtmp = random.randint(1,180)
          for k in range(1, 7):
            VARtmp = random.randint(1,180)
            while True:
              VARtmp2 = float(input("What angle do you clear at? Angle = "+str(VARtmp))+" ")
              if VARtmp2 == VARtmp:
                print(str(6-k)+" more to go!")
                break
              else:
                continue
          self.text_anime("Task Complete", 0.07)
          self.task_list.remove(self.current_room+" - clean o2 filter")
          self.task_completed.append(self.current_room+" - clean o2 filter")
        if self.current_room == "medbay" and task == "inspect sample":
          if self.time1 == "":
            while True:
              VARtmp = input("Type /start to start ")
              if VARtmp == "/start":
                print("Go take a coffee break")
                self.time1 = time.time()
                break
          else:
            time2 = time.time()
            if time2-self.time1 >= 75:
              randnum = random.randint(1, 5)
              while True:
                VARtmp = int(input("Which one will you select? 1 for the first one, 5 for the last one, etc. Please select the "+str(randnum)+"th sample. "))
                if VARtmp == randnum:
                  print("Task Complete")
                  self.task_list.remove("medbay - inspect sample")
                  self.task_completed.append("medbay - inspect sample")
                  break
                else:
                  print("Incorrect, try again")
            else:
              print("It has only been "+str(math.floor(time2-self.time1))+" seconds yet. Come back later and get your coffee break")
          
        if (self.current_room == "electrical" or (self.current_room == "locker room" and self.map == "mira hq")) and task == "fix wiring":
          left = ['red', 'yellow', 'pink', 'blue']
          right = ['red', 'yellow', 'pink', 'blue']
          random.shuffle(left)
          random.shuffle(right)
          print("left side: ", str(", ".join(left)), "\nright side: ", str(", ".join(right)))
          for x in left:
            while True:
              y = int(input("Which one on the right side matches "+x+"? (number 1-4) "))
              if right[y-1] == x: 
                print("Correct")
                break
              else:
                print("Incorrect. Try again")
          print("Task Complete")
          self.task_list.remove(self.current_room+" - fix wiring")
          self.task_completed.append(self.current_room + " - fix wiring")
        
        #the following are for Mira HQ
        if self.current_room == "lab" and task == "assemble artifact":
          pieces = ['top', 'top-center', 'center', 'center-bottom', 'bottom']
          random.shuffle(pieces)
          while True:
            print("here are the pieces. Please list the numbers in order from top-bottom\n")
            print(", ".join(pieces))
            order = input("")
            if order == str(pieces.index("top")+1)+str(pieces.index("top-center")+1)+str(pieces.index("center")+1)+str(pieces.index("center-bottom")+1)+str(pieces.index("bottom")+1):
              self.task_list.remove("lab - assemble artifact")
              self.task_completed.append("lab - assemble artifact")
              print("Task Complete")
              break
        
        if self.current_room == "cafeteria" and task == "buy beverage":
          slots = ["A1", "A2", "A3", "A4", "B1", "B2", "B3", "B4", "C1", "C2", "C3", "C4"]
          drinks = random.choice(slots)
          while True:
            buy = input("Please buy the drink at slot: "+drinks+" ")
            if buy == drinks:
              self.task_list.remove("cafeteria - buy beverage")
              self.task_completed.append("cafeteria - buy beverage")
              print("Task Complete")
              break
        
        if self.current_room == "balcony" and task == "measure weather":
          while True:
            if input("type '/start' ") == "/start":
              print("Starting...")
              for x in range(0, 100, 10):
                print("Completed:", str(x)+"%")
                time.sleep(6/10)
              print("Task Complete.")
              self.task_list.remove("balcony - measure weather")
              self.task_completed.append("balcony - measure weather")
              break
            else:
              print("418 I'm a teapot\nThe server refuses the attempt to brew coffee with a teapot.")
          
        if self.current_room == "storage" and task == "retrieve watering can":
          loc = random.choice(["shelf", "box", "floor"])
          while True:
            where = input("to retrieve the watering can, please search either the shelf, box, or the floor. ").lower().strip()
            if where == loc:
              print("Yay! you found the can.")
              while True:
                if input("type '/take' to take the can with you") == "/take":
                  print("Watering can has been taken. please proceed to the greenhouse ")
                  self.task_list.remove("storage - retrieve watering can")
                  self.task_completed.append("storage - retrieve watering can")
                  self.task_list.append("greenhouse - water plants")
                  break
              break
        if self.current_room == "greenhouse" and task == "water plants":
          thing = ["1", "2", "3", "4"]
          while True:
            water = input("What plant would you like to water ")
            if water in thing:
              print("Watered that plant")
              thing.remove(water)
            if len(thing) == 0:
              print("Task complete")
              self.task_list.remove("greenhouse - water plants")
              self.task_completed.append("greenhouse - water plants")
              break
            else:
              print("404\nPlant has not been found")
        if self.current_room == "launchpad" and task == "fuel engines":
          while True:
              VARtmp = input("type /start to start ").strip()
              if VARtmp == "/start":
                  for x in range(9, 0, -1):
                      print(x, "seconds remaining")
                      time.sleep(1)
                  print("Task Complete")
                  self.task_list.remove(self.current_room + " - " + task)
                  break
              else:
                  print("Please try again")
        if self.current_room == "cafeteria" and self.map == "mira hq" and task == "empty garbage":
          VARtmp = input("enter /pull to pull the lever ")
          if VARtmp == "/pull":
              print("Emptying garbage...\nTask Complete")
              self.task_list.remove("cafeteria - empty garbage")
          else:
              self.task("empty garbage")
        if self.current_room == "reactor" and self.map == "mira hq" and task == "divert power":
          while True:
              self.divertpowerroom = random.choice(["admin", "cafeteria", "comms", "greenhouse", "launchpad", "lab", "medbay","office"])
              VARtmp = input("Type /pull to pull the lever to " + self.divertpowerroom+" ")
              if VARtmp == "/pull":
                  self.text_anime("Task Complete", 0.07)
                  self.task_list.remove("reactor - divert power")
                  self.task_list.append(self.divertpowerroom+" - divert power")
                  break
          if self.current_room == self.divertpowerroom and task == "divert power" and self.map == "mira hq":
            while True:
                VARtmp = input("Type /pull to pull to accept the power ")
                if VARtmp == "/pull":
                    self.text_anime("Task Complete", 0.07)
                    self.task_list.remove(self.current_room + " - " + task)
                    self.task_completed.append("reactor - divert power")
                    break
        if self.current_room == "admin" and task == "enter id code":
          randomnum = random.randint(10000,99999)
          while True:
            idcode = int(input("Your id code is "+str(randomnum)+". Please enter it. "))
            if idcode == randomnum:
              self.text_anime("Task Complete",0.07)
              self.task_list.remove(self.current_room+" - enter id code")
              break
        if self.current_room == "office" and task == "process data":
          while True:
            start = input("Type /start to start ")
            if start == "/start":
              break
          for i in range(1,13):
            print("Processing data..."+str(200/(13-i))+"% done.")
            time.sleep(1)
          print("Done!")
          self.text_anime("Task Complete",0.07)
          self.task_list.remove("office - process data")
        if self.current_room == "launchpad" and task == "run diagnostics":
          if self.time2 != "":
            if time.time() - self.time2 >= 90:
              print("Diagnostics complete.")
              time.sleep(1)
              random_anomaly = random.randint(1,5)
              anomaly = int(input("Please select anomaly "+str(random_anomaly)))
              if anomaly == random_anomaly:
                self.text_anime("Task Complete",0.07)
                self.task_list.remove("launchpad - run diagnostics")
            else:
              print("Diagnostics are still running. It has only been "+str(time.time()-self.time2)+" seconds so far.")
          else:
            while True:
              start = input("Type /start to start ")
              if start == "/start":
                break
            self.time2 = time.time()
            print("Diagnostics are now running")
          
        if self.current_room == "lab" and task == "sort samples":
          items = ["f1", "f2", "f3", "r1", "r2", "r3", "p1", "p2", "p3"]
          random.shuffle(items)
          for i in items:
            while True:
              box = input("Which box would you like to put "+i+" in? Fossil, Rock, Plant ").strip()
              if box == "":
                print("Enter an answer!!!")
              elif (i[0] == box[0].lower()):
                print("Yay! You got it!!!")
                break
          self.text_anime("Task Complete",0.07)
          self.task_list.remove("lab - sort samples")
          
    def resourse(self, action):
        if self.current_room == "admin" and action == "admin map" and self.comms == "affirmative":
          print("[Loading Admin Map...]")
          time.sleep(1)
          for x in self.rooms:
            if x == "admin":
              print("There is 1 player (you) in admin")
            else:
              numplayers = random.randint(0, 3)
              if numplayers == 0:
                print("No one is in "+x)
              else:
                print("There are "+str(numplayers)+" players are in "+x)
          print("The rest of the players are in the hallways")
        if self.current_room == "security" and action == "cams" and self.comms == "affirmative" and map == "skeld":
          print("[Loading Cameras...]")
          time.sleep(1)
          r = random.randint(1, 5)
          room = random.choice()
          imp = random.choice(self.imposters)
          player = random.choice(self.players)
          if imp != self.me:
            if r == 3:
              print("You caught "+imp+" venting near shields and navigation!")
            if r == 2:
              print(imp+" killed "+player+" near "+room)
              self.non_reported[room] = player
            else:
              print("Nothing exciting so far")
        if action=="sab off":
          self.forthesakeofturningthisonagain = []
          self.forthesakeofturningthisonagain.extend([self.hascommsbeendown, self.haslightsbeendown, self.hasreactorbeendown])
          self.hascommsbeendown = "yes"
          self.haslightsbeendown = "yes"
          self.hasreactorbeendown = "yes"
          print("Sabotages have been turned off")
        if action == "sab on":
          self.hascommsbeendown = self.forthesakeofturningthisonagain[0]
          self.haslightsbeendown = self.forthesakeofturningthisonagain[1]
          self.hasreactorbeendown = self.forthesakeofturningthisonagain[2]
          self.forthesakeofturningthisonagain.extend([self.hascommsbeendown, self.haslightsbeendown, self.hasreactorbeendown])
          print("Sabotages have been turned on")
        if self.current_room == "comms" and action == "doorlog" and self.map == "mira hq":
          players = self.players
          for i in range(1,11):
            chance = random.randint(1,4)
            if chance == 1:
              player = random.choice(players)
              sensor = random.choice(["north","east","west"])
              print(player+" passed the "+sensor+" sensor")
        
        if action == "console":
          command = input(">>> ")
          command = command.replace("<indent>", "  ")
          command = command.replace("<br>", "\n")
          exec(command)

        if action == "beta test":
          if self.mrs == 0:
            self.mrs = 1
            print("Beta test mode on")
          if self.mrs == 1:
            self.mrs = 0

            
            
    def sab(self, whatsab):
        self.sabotage = "yes"
        if self.map == "skeld":
          if whatsab == "comms":
              self.comms = "Houston we have a problem, comms are down so it is useless to call you. Have a great day!"
              print("[Comms sabotaged]")
          if whatsab == "fixcomms":
            fixed = random.randint(1,4)
            if fixed == 1:
              print("Comms has already been fixed.")
              self.comms = "affirmative"
              self.sabotage = "no"
            else:
              num1 = random.randint(1,5)
              num2 = random.randint(1,5)
              hardmathprobs = input("What is "+str(num1)+"+"+str(num2))
              if hardmathprobs == str(num1+num2):
                  print("You dial into "+str(num1+num2)+" and get the comms back")
                  self.comms = "affirmative"
                  self.sabotage = "no"
              else:
                  self.sab("fixcomms")
        if whatsab == "lights":
            self.lights = "Houston we have a problem, the power is off so our computers are off. We will be crashing near the sea of tranquility! Have a great day!"
            for x in range(100, 1, -10):
                print("Lights:", str(x)+"%")
                time.sleep(0.1)
            #original_time = time.time()
            #random_fix = random.randint(10,120)
            '''while True:
                if time.time() >= (original_time+random_fix):
                    print("Lights have been fixed already")
                    self.lights = "affirmative"
                    self.sabotage = "no"
                    break'''
        if whatsab == "fixelectrical":
          if self.current_room == "electrical" or self.current_room == "office":
            fixed = random.randint(1,5)
            if fixed == 1:
              print("Lights have just been fixed")
              self.lights = "affirmative"
              self.sabotage = "no"
            else:
              seq = random.choice(["0", "1"])+random.choice(["0", "1"])+random.choice(["0", "0"])+random.choice(["0", "1"])+random.choice(["0", "1"])+random.choice(["0", "1"])
              print("1 is for on 0 is for off. Switch all the 0s to on to fix.\n"+seq)
              seq= list(seq)
              while True:
                  if seq == ["1", "1", "1", "1", "1", "1"]:
                      print("lights fixed")
                      self.lights = "affirmative"
                      break
                  target = int(input("which switch would you like to flick? 1-6"))-1
                  if seq[target] == "0":
                      seq[target] = "1"
                  else:
                      seq[target] = "0"
                  print("Current position is \n"+"".join(seq))
        if whatsab == "reactor":
            self.reactortimer = time.time()
            self.reactor = "Houston we have a problem, reactor is down! HELLLLLLLLP"
            for i in range(1,11):
              if 40-self.reactortimer == 0:
                print("Crap time is up")
                break
              else:
                print("BEEP REACTOR IS DOWN. YOU HAVE 40 SECONDS TO FIX.")
                time.sleep(0.5)
            random_time = random.randint(5,30)
            reactor_time = self.reactortimer+random_time
            """while True:
              if self.sabotage == "yes":
                if time.time() >= reactor_time:
                  if self.impostor_or_not == "no":
                    print("Reactor has blown up the ship.")
                    self.text_anime("Defeat\nThere are " + str(len(self.imposters)) + " remaining\nThe imposters were: " + ", ".join(self.imposters), 0.07)
                    exit()
                  else:
                    if random.randint(1, 5) == 1:
                      print("Hey! Reactor has been fixed.")
                      self.reactor = "affirmative"
                      self.sabatoge = "no"
                      self.reactortimer = float('inf')
                      if self.impostor_or_not == "no":
                        pass
                    else:
                      self.text_anime("You won from the reactor sabotage!",0.07)
                      print("\nVICTORY!")
                      exit()"""

        if whatsab == "fixreactor":
          if time.time() - self.reactortimer >= 40:
            if self.impostor_or_not == "no":
              print("You took way too much time to even come here")
              self.text_anime("Defeat\nThere are " + str(len(self.imposters)) + " remaining\nThere imposters were: " + ", ".join(self.imposters), 0.07)
              exit()
            else:
              self.text_anime("You won from the reactor sabotage!",0.07)
              print("\nVICTORY!")
              exit()
          else:
            reactorchance = random.randint(1, 5)
            if reactorchance == 3:
              if self.impostor_or_not == "no":
                time.sleep(5)
                print("No one came into the room to help you. Those pesky crewmates!")
                self.text_anime("Defeat\nThere are " + str(len(self.imposters)) + " remaining\nThere imposters were: " + ", ".join(self.imposters), 0.07)
                exit()
              else:
                self.text_anime("You won from the reactor sabotage!",0.07)
                print("\nVICTORY!")
                exit()
            if reactorchance == 4 or reactorchance == 5:
              if self.current_room == "reactor":
                print("Another person is in the room.")
                while True:
                  if time.time() - self.reactortimer >= 20:
                    if self.impostor_or_not == "no":
                      self.text_anime("Defeat\nThere are " + str(len(self.imposters)) + " remaining\nThere imposters were: " + ", ".join(self.imposters), 0.07)
                      exit()
                    else:
                      self.text_anime("You won from the reactor sabotage!",0.07)
                      print("\nVICTORY!")
                      exit()
                  scanhand = input("Type /fix to fix")
                  if scanhand == "/fix":
                    print("Reactor fixed!")
                    self.reactor = "affirmative"
                    self.sabatoge = "no"
                    self.reactortimer = float('inf')
                    if self.impostor_or_not == "no":
                      pass
                    break
            else:
              print("Reactor fixed!")
              self.reactortimer = float('inf')
              self.sabotage = "no"
        '''if whatsab == "oxygen":
            self.oxygen = "Houston we have a problem, We have no oxygen! HELLLLLLLLP"
            for i in range(1,10):
              print("BEEP OYXYGEN UNREACHABLE!!")
              time.sleep(0.5)'''


among_you()
