#Among You.py Made by Andrew Chen and W W. Wu. AndrewChen51 on repl, AndrewC10 on AoPS. Wuwang2002 on AoPS, WWWtheW on repl. DO NOT REMOVE THIS LINE
import random
import time
import math


class among_you():
    def __init__(self):
      #varibles
        print("Among You.py Made by Andrew Chen and W. W. Wu.\nAndrewC10 on AoPS, AndrewChen51 on REPL.it\nWuwang2002 on AoPS, WWWtheW on REPL.it")
        self.time1 = ""
        self.sabatoge = "no"
        self.forthesakeofturningthisonagain = ['no', 'no', 'no']
        self.comms = "affirmative"
        self.lights = "affirmative"
        self.reactor = "affirmative"
        #self.oxygen = "affirmative"
        self.non_reported = {}
        self.current_room = "cafeteria"
        self.reactortimer = ""
        self.me = ''
        self.players = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "lime", "cyan", "brown", "black",
                        "white", "gray", "silver", "gold", "teal", "tan", "violet", "maroon", "olive"]
        self.backup = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "lime", "cyan", "brown", "black",
                       "white", "gray", "silver", "gold", "teal", "tan", "violet", "maroon", "olive"]
        self.players_dead = []
        self.imposters = []
        self.rooms = ["cafeteria", "medbay", "reactor", "security", "electrical", "storage", "admin","shields", "navigation", "oxygen", "weapons", "comms", "engine"]
        self.extra_rooms = ["cafe","cams","elec","navi","o2","lights"]
        self.download_data_location = random.choice(["cafeteria","navigation","comms","electrical","weapons"])
        self.tasks = ["medbay - scan", self.download_data_location+" - download data", "shields - prime shields", "reactor - unlock manifolds", "storage - refuel", "navigation - chart course", "navigation - stabilize steering", "oxygen - empty garbage","engine - align output", "electrical - calibrate distributor", "electrical - divert power", "reactor - start reactor", "admin - swipe card", "weapons - clear asteroids", "oxygen - clean o2 filter", "medbay - inspect sample", "electrical - fix wiring"]
        self.task_completed = []
        self.hascommsbeendown = "no"
        self.haslightsbeendown = "no"
        self.hasreactorbeendown = "no"
        #self.hasoxygenbeendown = "no"

        #input questions
        while True:
            self.me = str(input("You are waiting in the lobby, what is your player color")).strip().lower()
            if self.me not in self.players:
                print("Sorry, that color is not available")
            else:
                break
        self.players.remove(self.me)
        self.num_emergencies = int(input("How many emergency meetings?"))
        while True:
          self.num_imposter = int(input("How many imposters?"))
          if self.num_imposter >= 6:
            continue
          else:
            break
        self.impostor_or_not = input("Would you like to be Impostor? yes/no").strip().lower()
        if self.impostor_or_not == "no":
          while True:
            self.num_task = int(input("How many tasks? Minimum 7 tasks"))
            if self.num_task >= 7:
              break
            else:
              print("Minimum 7 tasks")
          print("The game has started\nThere are", self.num_imposter, "imposters among us")
          self.select_roles()
        if self.impostor_or_not == "yes":
          while True:
            self.kill_cooldown = float(input("How long of a kill cooldown? Minimum 10 seconds"))
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
        self.num_emergencies_left = self.num_emergencies
        self.time1 = ""


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
      if VARroomie in self.rooms:
        self.current_room = VARroomie
        if self.lights == "affirmative":
            vented = int(random.randint(1, 5))
            body = int(random.randint(1, 5))
            if VARroomie in self.non_reported:
                print("You go to", VARroomie, "and find", self.non_reported[VARroomie] + "'s body on the floor")
            if vented == 2 and self.current_room not in ["comms","storage","oxygen"]:
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
                VARsabotage = random.randint(1,7)
                if VARsabotage == 1 and self.hascommsbeendown == "no":
                  self.comms = ""
                  self.hascommsbeendown = "yes"
                  self.sab("comms")
                if VARsabotage == 2 and self.haslightsbeendown == "no":
                  self.lights = ""
                  self.haslightsbeendown = "yes"
                  self.sab("lights")
                if VARsabotage == 3 and self.hasreactorbeendown == "no":
                  self.reactor = ""
                  self.hasreactorbeendown = "yes"
                  self.sab("reactor")

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
            VAReject = input("who do you want to eject?").strip().lower()
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
        VAReject = input("who do you want to eject?").strip().lower()
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
                self.players.remove(VAReject)
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

    def main(self):
        while True:
            if len(self.imposters) == 0:
                print("Victory!")
                break
            if len(self.imposters) > len(self.players):
                self.text_anime("Defeat #of imps > #of players\nThere are " + str(len(self.imposters)) + " remaining\nThere imposters were: " + ", ".join(self.imposters), 0.07)
            room = input("What room would you like to go to? (type /help to get help)").strip().lower()
            if room == "/tasklist":
                if self.comms == "affirmative":
                    print("\n".join(self.task_list))
                else:
                    print("[Comms sabatoged. please go to comms and type: /fix]")
            if room[:5] == "/task":
                self.task(room[6:])
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
                print("\nList of rooms\ncafeteria, medbay, reactor, labratory, security, electrical, storage, admin, shields, navigation, oxygen, weapons, cams, 02, comms, engine\n\n")
            if self.reactor != "affirmative" and time.time() - self.reactortimer >= 20:
              print("Reactor has blown up the ship.")
              self.text_anime("Defeat\nThere are " + str(len(self.imposters)) + " remaining\nThere imposters were: " + ", ".join(self.imposters), 0.07)
              exit()
            elif room not in self.rooms and room not in self.extra_rooms and room not in ["/tasklist", "/task", "/fix", "/help"]:
                print("\nThere is no such room")
                continue
            elif room in self.rooms:
                self.investigate(room)
                time.sleep(0.5)
            elif room == "cafe":
                self.investigate("cafeteria")
            elif room == "cams":
                self.investigate("security")
            elif room == "elec" or room == "lights":
                self.investigate("electrical")
            elif room == "navi":
                self.investigate("navigation")
            elif room == "o2":
                self.investigate("oxygen")
    
    def impostor_investigate(self,VARroom):
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
          kill = input("Would you like to kill? yes/no").lower().strip()
          if (kill == "yes") and (self.current_room not in self.non_reported):
            while True:
              killed = input("Who would you like to kill? People you can kill are: "+", ".join(victims))
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
        room = input("What room would you like to go to?")
        if room[:3] == "/re":
          self.resourse(room[4:])
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
        if len(self.imposters) > len(self.players):
          print("Victory!")
          exit()
        if room == "/fix":
          self.sab("fix" + self.current_room)
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
        VAReject = input("who do you want to eject?").strip().lower()
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
        VAReject = input("who do you want to eject?").strip().lower()
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
            if self.current_room == "shields" and task == "prime shields":
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
                    VARtmp = int(input(">>>"))
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
                    VARtmp = int(input("Type in the numbers from 1 to 10. no spaces"))
                    if VARtmp == 12345678910:
                        self.text_anime("Task Complete", 0.07)
                        self.task_list.remove(self.current_room + " - " + task)
                        self.task_completed.append(self.current_room + " - " + task)
                        break
                    else:
                        print("Please type again")
        if self.current_room == "storage" and task == "refuel":
            while True:
                VARtmp = input("type /start to start").strip()
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
                VARtmp = input("type /start to start").strip()
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
        if self.current_room == "navigation" and task == "chart course":
            VARtmp = input("To chart course select 4 locations. list the numbers from 1-4")
            if VARtmp == "1234":
                self.task_list.remove(self.current_room + " - " + task)
                self.task_completed.append(self.current_room + " - " + task)
                print("Task Complete")
            else:
                self.task("chart course")
        if self.current_room == "navigation" and task == "stabilize steering":
            VARtmp = input("what coordinates are the origin? do in the format: (x, y)")
            if VARtmp == "(0, 0)":
                print("Task complete")
                self.task_list.remove(self.current_room + " - " + task)
                self.task_completed.append(self.current_room + " - " + task)
            else:
                self.task("stabilize steering")
        if self.current_room == "oxygen" and task == "empty garbage":
            VARtmp = input("enter /pull to pull the lever")
            if VARtmp == "/pull":
                print("Emptying garbage...\nTask Complete")
                self.task_list.remove("oxygen - empty garbage")
                self.task_list.append("storage - empty garbage")
            else:
                self.task("empty garbage")
        if self.current_room == "storage" and task == "empty garbage":
            VARtmp = input("enter /pull to pull the lever")
            if VARtmp == "/pull":
                print("Emptying garbage...\nTask Complete")
                self.task_list.remove(self.current_room+" - " + task)
                self.task_completed.append("storage, oxygen - empty garbage")
            else:
                self.task("empty garbage")
        if self.current_room == "engine" and task == "align output":
            VARtmp = input("What angle should we align at?")
            if VARtmp == "0":
                self.text_anime("Task complete", 0.07)
                self.task_list.remove(self.current_room + " - " + task)
                self.task_completed.append("engine - align output")
            else:
                self.text_anime("Task complete", 0.07)
                self.task("align output")

        if self.current_room == "electrical" and task == "calibrate distributor":
            while True:
                VARtmp = input('Type "click"')
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
                tmproom = random.choice(["engine", "weapons", "shields", "navigation", "comms", "oxygen", "security"])
                VARtmp = input("Type /pull to pull the lever to " + tmproom)
                if VARtmp == "/pull":
                    self.text_anime("Task Complete", 0.07)
                    self.task_list.remove("electrical - divert power")
                    self.task_list.append(tmproom+" - divert power")
                    break
        if self.current_room != "electrical" and task == "divert power":
            while True:
                VARtmp = input("Type /pull to pull to accept the power")
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
            VARtmp = input("Type /swipe to swipe card")
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
        if self.current_room == "weapons" and task == "clear asteroids":
          VARtmp = input("\nType /start to start")
          if VARtmp == "/start":
            for k in range(21):
              print("Shooting asteroids..."+str(k)+" complete")
              time.sleep(0.5)
            self.text_anime("Task Complete", 0.07)
            self.task_list.remove("weapons - clear asteroids")
            self.task_completed.append("weapons - clear asteroids")
        if self.current_room == "oxygen" and task == "clean o2 filter":
          VARtmp = random.randint(1,180)
          for k in range(1, 7):
            VARtmp = random.randint(1,180)
            while True:
              VARtmp2 = float(input("What angle do you clear at? Angle = "+str(VARtmp)))
              if VARtmp2 == VARtmp:
                print(str(6-k)+" more to go!")
                break
              else:
                continue
          self.text_anime("Task Complete", 0.07)
          self.task_list.remove("oxygen - clean o2 filter")
          self.task_completed.append("oxygen - clean o2 filter")
        if self.current_room == "medbay" and task == "inspect sample":
          if self.time1 == "":
            while True:
              VARtmp = input("Type /start to start")
              if VARtmp == "/start":
                print("Go take a coffee break")
                self.time1 = time.time()
                break
          else:
            time2 = time.time()
            if time2-self.time1 >= 75:
              randnum = random.randint(1, 5)
              while True:
                VARtmp = int(input("Which one will you select? 1 for the first one, 5 for the last one, etc. Please select the "+str(randnum)+"th sample."))
                if VARtmp == randnum:
                  print("Task Complete")
                  self.task_list.remove("medbay - inspect sample")
                  self.task_completed.append("medbay - inspect sample")
                  break
                else:
                  print("Incorrect, try again")
            else:
              print("It has only been "+str(math.floor(time2-self.time1))+" seconds yet. Come back later and get your coffee break")
          
        if self.current_room == "electrical" and task == "fix wiring":
          left = ['red', 'yellow', 'pink', 'blue']
          right = ['red', 'yellow', 'pink', 'blue']
          random.shuffle(left)
          random.shuffle(right)
          print("left side: ", str(", ".join(left)), "\nright side: ", str(", ".join(right)))
          for x in left:
            while True:
              y = int(input("Which one on the right side matches "+x+"? (number 1-4)"))
              if right[y-1] == x: 
                print("Correct")
                break
              else:
                print("Incorrect. Try again")
          print("Task Complete")
          self.task_list.remove("electrical - fix wiring")
          self.task_completed.append("electrical - fix wiring")
          
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
        if self.current_room == "security" and action == "cams" and self.comms == "affirmative":
          print("[Loading Cameras...]")
          time.sleep(1)
          r = random.randint(1, 5)
          room = random.choice(['admin', 'reactor', 'oxygen', 'medbay'])
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
            
    def sab(self, whatsab):
        self.sabotage = "yes"
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
        if whatsab == "fixelectrical":
          fixed = random.randint(1,3)
          if fixed == 1:
            print("Lights have been fixed already")
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
              if 20-self.reactortimer == 0:
                print("Crap time is up")
                break
              else:
                print("BEEP REACTOR IS DOWN. YOU HAVE 20 SECONDS TO FIX.")
                time.sleep(0.5)

        if whatsab == "fixreactor":
          if time.time() - self.reactortimer >= 20:
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
