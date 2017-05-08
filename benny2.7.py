input_a = raw_input("State your name: ")
input_b = raw_input("State your class: ")
input_c = raw_input("State the password: ")
print
print
print
if input_c == "WETSU" or "wetsu" or "Wetsu":
  print "Good Evening Cadet %s, Class of %s. I am Benny, your personal USMA valet." % (input_a, input_b)
  print
  print "*************************************************************************"
  print
  print "Current conditions at McArthur Hall:"
  print

import pyowm
owm = pyowm.OWM('cdb0f1f55a1db9e90ae4fb10532ecb2b')
observation = owm.weather_at_place("Westpoint,us")
w = observation.get_weather()
wind = w.get_wind()
temperature = w.get_temperature('celsius')
print
print w
print
print wind
print 
print temperature
print
print "Wind speed: %s m/s" % (w.get_wind()['speed'])
print     
print "Temperature: %s degrees celsius" %(w.get_temperature('celsius')['temp'])
print
print "Cloudiness: %s percent" %(w.get_clouds())
print
print "Pressure: %s hpa" %(w.get_pressure())
print
print "Sunrise: %s GMT" %(w.get_sunrise_time('iso'))
print
print "Sunset: %s GMT" %(w.get_sunset_time('iso'))
print
print                         
input_d = raw_input("Would you like to continue to my menu of services? ")
print
print
print "*************************************************************************"
print
print
if input_d != "Yes":
  input_h = raw_input("You seem sullen and indifferent.  Did you go to the Air Force Academy?  If you change your mind, type Yes here, and I'll show you what I can do for you.  Unfortunately, I can't change that you're a zoomie.")
if input_d or input_h == "Yes" or "yes" or "YES":
  print "Here is a selection of services I can offer you, Cadet %s:" %(input_a)
  print
  print "1. I can quiz you on your Bugle Notes (aka Poop);" 
  print "2. I can give you academic calendar information or you can use my Time Machine;"
  print "3. I can display the latest USMA news from Google;" 
  print "4. You can watch a new USMA video from YouTube;" 
  print "5. I can display recent photos of West Point."
  print "6. We can play a USMA trivia game."
  print "7. I can generate a quote from an esteemed West Pointer."
  print
  print
elif input_d == "No" or "no" or "NO":
  input_h = raw_input("You seem sullen and indifferent.  Did you go to the Air Force Academy?  If you change your mind, type Yes here, and I'll show you what I can do for you.  Unfortunately, I can't change that you're a zoomie.")
print
print
input_e = raw_input("Please select from the menu using the item number: ")
if input_e == "1":
  print
  print "*************************************************************************"
  print
  print "Welcome to The Cadet Poop Calculator"
  print
  print
  print
  print "Alright, Cadet %s, it's time to see what you know." %(input_a)
  input_f = raw_input("When you are ready to test your poop, type 'Enter': ")
  if input_f == 'enter' or 'Enter' or 'ENTER':
    input_g = raw_input("Name the first of the THREE GENERAL ORDERS: ")
    if input_g != "I will guard everything within the limits of my post and quit my post only when properly relieved":
      print "WRONG! Maybe Annapolis is a better fit for you."
    elif input_g == "I will guard everything within the limits of my post and quit my post only when properly relieved":
      print "Well done, Cadet %s.  You're not as stupid as you look." %(input_a)
      input_k = raw_input("Ready for the next one? Enter Yes...or type Menu if you want the coward's way out: ")
      if input_k == "Yes" or "yes" or "YES":
        input_l = raw_input("Name the second of the THREE GENERAL ORDERS: ")
        if input_l != "I will obey my special orders and perform all of my duties in a military manner":
          print "INCORRECT!  Might as well pack your bags and head home to Duluth..."
        elif input_l == "I will obey my special orders and perform all of my duties in a military manner":
          input_m = raw_input("Not bad.  But can you get the third?  Enter yes to give it a whack...or I'll give you a whack... ")
          if input_m == "Yes" or "yes" or "YES":
            input_o = raw_input("Name the third of the THREE GENERAL ORDERS: ")
            if input_o != "I will report violations of my special orders, emergencies, and anything not covered in my instructions to the commander of the relief":
              print "Negative.  Might as well pack your bags!"
            if input_o == "I will report violations of my special orders, emergencies, and anything not covered in my instructions to the commander of the relief":
              input_p = raw_input("So your memory is pretty good.  But can you sing? Type next to advance to the next round: ")
              if input_p == "Next" or "next" or "NEXT":
                print "Type the next line in this verse of the West Point Alma Mater: "
                input_q = raw_input("Teach us by day, by night, __ ____ _____ _____ ______ ")
                if input_q != "to keep thine honor bright":
                  print "Thankfully for you, the Coast Guard Academy's song is easier to learn."
                if input_q == "to keep thine honor bright":
                  print "You are correct."

if input_e == "2":
  print "Welcome to the USMA Academic Calendar for the Spring 2017 Semester!"
  print "1. Enter a month to view scheduled events"
  print "2. Enter a keyword to search for matching event info (ex: Graduation)"
  print "3. Time Machine: Look up a date in West Point's history OR view the events of a single date through a specified date range (ex: January 27, 1778 or January 27)"
  

if input_e == "3":
  print "*************************************************************************"
  print
  print "Welcome to the USMA News Network: Where we're only interested in shit that happens re: West Point"
  print
  print "Latest Headlines from Google:"
  import feedparser
  d = feedparser.parse("https://news.google.com/news?cf=all&hl=en&pz=1&ned=us&q=west+point+military+academy&output=rss")
  print d['feed']['title']
  print d['feed']['link']
  print d.feed.subtitle
  print
  print
  print d['entries'][0]['title']
  print
  print d.entries[0]['link']
  print
  print d['entries'][1]['title']
  print
  print d.entries[1]['link']
  print
  print d['entries'][2]['title']
  print
  print d.entries[2]['link']
  print
  print d['entries'][3]['title']
  print
  print d.entries[3]['link']
  print
  print d['entries'][4]['title']
  print
  print d.entries[4]['link']
  print
  print d['entries'][5]['title']
  print
  print d.entries[5]['link']
  print
  print d['entries'][6]['title']
  print
  print d.entries[6]['link']
  print
  print d['entries'][7]['title']
  print
  print d.entries[7]['link']
  print
  print d['entries'][8]['title']
  print
  print d.entries[8]['link']
  print
  print d['entries'][9]['title']
  print
  print d.entries[9]['link']
  print
  print d['entries'][10]['title']
  print
  print d.entries[10]['link']

    
    











  
#Teach us by day, by night, 

#To keep thine honor bright, 

#For thee to fight. 
#When we depart from thee, 
#Serving on land or sea, 
#May we still loyal be, 
#West Point, to thee.

#And when our work is done, 
#Our course on earth is run, 
#May it be said, "Well done; 
#Be thou at peace." 
#E'er may that line of gray 
#Increase from day to day 
#Live, serve, and die, we pray, 
#West Point, for thee.                           
  #input_q = raw_input("Which verse of the alma mater is INCORRECT: "                   
                    
                            









  #elif: inputf = 2:
    #return correspoding calendar date for datetime
    #elif: inputf = 3:
      #return latest google alerts headlines
      #elif: inputf = 4:
        #generate usma video
        #elif: inputf = 5:
          
          






#print ("Welcome to The Cadet Poop Calculator")
#print
#print
#print

#print ("Alright, Cadet %s, it's time to see what you know." % (inputa))

#inputd = raw_input("When you are ready to test your poop, type 'Enter': ")

#if inputd == 'enter' or 'Enter' or 'ENTER':
    #inpute = raw_input("Name the first of the THREE GENERAL ORDERS: ")

#if inpute == "I will guard everything within the limits of my post and quit my post only when properly relieved":
  #print "Well done, Cadet %s.  You're not as stupid as you look." % (inputa)
  
#else:
  #print "WRONG! Maybe Annapolis is a better fit for you."
