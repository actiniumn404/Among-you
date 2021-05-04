![among us with python](https://i.ibb.co/CtdWRxP/among-us-with-py.png)
# Among You.py
### by Andrew Chen and W. Wu
###### Based on Among Us, by InnerSloth LLC
#### NOW FEATURING ALL 17 TASKS, IMPOSTER ROLE, AND ALL SABOTAGES BESIDES OXYGEN
Among you.py is a game developed by AndrewChen51 and WWWtheW. It is basically a Python adaption of Among Us

### As a Crewmate
---
* Your goal as a crewmate is to repair your ship with your "tasks" while trying to figure out who the Impostors are before they kill too many crewmates abord. Vote all of them out to win!
* You will know if a person is an imposter if they vent or kill. If they kill someone, report by typing `/report`. If they vent, go to cafeteria and call an emergency meeting by typing: `/task emergency`.
* To access the admin map, type `/re admin map`.
* To access the security cameras, type `/re cams`
* To turn off sabotages, do `/re sab off`
* To turn on sabotages again, do `/re sab on`
### Tasks
---
### How to do it
----
* To access your tasks, type in `/tasklist`. In the tasklist, the task will be labeled like this: `reactor - unlock manifolds` The first part of it, (In this case, it is `reactor`) is the room you need to go to to complete the task.  When in that room, do `/task` plus the second part of that. (In this case, it is `unlock manifolds` so when we are in reactor and we want to complete this task, we just do `/task unlock manifolds`)

#### FAQ: When I complete a task, that task is removed from `/tasklist`, but another similar task is appended. What is going on?
* You might have a Multi-part task. You can't just complete these tasks in one go. You will have to finish the first part, then do the follow up.
#### A Task Cheat Sheet
* Scan: Just hop into medbay and do `/task scan`, then wait for a few seconds
* Download Data: There are 5 locations where you can download. The program will specify which one. After download, you need to upload data.
* Prime Shields: Type in numbers from 1 to 7. If you get one, the program will say. Get all 4 to complete the task.
* Unlock Manifolds: Type in `12345678910`.
* Refuel: Type `/start`, then go to engine and do the same thing.
* Chart Course: Type in `1234`.
* Stabilize Steering: Type in `(0,0)`.
* Empty Garbage: Type `/pull`, then go to storage and do the same thing.
* Align Output: Type in `0`.
* Calibrate Distributor: Go to electrical and type `click` and get lucky.
* Divert Power - Go to electrical and type `/pull`. Then go to the other location specified and do the same thing.
* Start Reactor - Go to reactor and type the numbers given to you by the program.
* Swipe Card - Go to Admin and type `swipe` until you get really lucky.
* Clear Asteroids Go to weapons and type `/start` and wait till all 20 asteroids are shot.
* Clean O2 Filter: Type in the correct angle given by the program 6 times.
* Inspect Sample: This is a multi part task. Go into medbay and type `/start` then take a 75 second coffee break. If you come back to early, the system will tell you how many seconds have passed. After the 75 seconds, choose a number from 1 to 5.
* Fix Wiring: Go into electrical. You will be given two sets of strings. The system will ask you what position if the ___ color in the right. Look in the string in the right side. Type what order it is in (1 for first position, 2 for second position etc.)

### Sabotages
Currently, we have implemented three sabotages.
* Comms: Does not let you use `/tasklist`, use cams, or use the admin map. Go to comms and type `/fix` to fix it. To do that, you must answer an addition problem.
* Lights: Does not let you see impostors venting or dead bodies. Go to electrical and type `/fix` to fix it. To fix it, make all the numbers 1.
* Reactor: You die if it doesn't get fixed
* * You have exatly 20 seconds to go to fix. Trust me. I have a timer that doesn't multithread.
* * Note that two people are needed to fix reactor
* * There is a one in five chance that the reactor will not be fixed, as no one came into reactor to fix it. (Those pesky crewmates!)
* * There is a two in five chance that when you walk into reactor, there is only one other person in the room. You have to type `\fix` to fix reactor
* * There is a two in five chance that when you walk into reactor, two people have just fixed it.

### As an Impostor
---
* Your goal as an Impostor is to kill enough crewmates to win.
* Whenever you go to a room, there will be between 0 and 4 crewmates in the room, inclusive.
* If there is more than 1 crewmate in that room, there is a 1/2 chance that another crewmate will see you kill, unless there is a lights sabotage. 
* Also when that crewmate reports, there is a 1/number-of-people-in-room chance that the other crewmates will think it is a self-report and eject them. The same goes to skipping. The rest goes to you getting ejected. Ouch...
* You are asked whether or not you want to kill a crewmate or not whenever you go into a room.
* To access admin map or access cams, you need to put `/re` before it.
* You can sabotage lights, comms, and reactor by using `/sab `+whatever your sabotage is.


**To report errors in this MARKDOWN file, please private message *AndrewC10* or *Wuwang2002* via [The Art of Problem Solving Site](https://artofproblemsolving.com/community/my-messages)**
