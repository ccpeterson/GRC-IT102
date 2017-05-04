while True:
    dayOfWeek = input ("What day is is today?")

    if dayOfWeek.lower() == "monday" or dayOfWeek.lower() == "mon" or dayOfWeek.lower() == "m":
        print ("Monday's words of encouragement:")
        print ("Go as far as you can see; when you get there, you'll be able to see further.")
        break
    elif dayOfWeek.lower() == "tuesday" or dayOfWeek.lower() == "tues" or dayOfWeek.lower() == "t":
        print ("Tuesday's words of encouragement:")
        print ("You get to decide where your time goes. You can either spend it moving forward,")
        print ("or you can spend it putting out fires. You decide. And if you don't decide,")
        print ("others will decide for you.")
        print ("-Tony Morgan")
        break
    elif dayOfWeek.lower() == "wednesday" or dayOfWeek.lower() == "wed" or dayOfWeek.lower() == "w":
        print ("Wednesday's words of encouragement:")
        print ("Believe you can and you're halfway there.")
        print ("-Theodore Roosevelt")
        break
    elif dayOfWeek.lower() == "thursday" or dayOfWeek.lower() == "thur" or dayOfWeek.lower() == "th":
        print ("Thursday's words of encouragement:")
        print ("Success is the sum of small efforts repeated day in and day out")
        print ("-Robert Collier")
        break
    elif dayOfWeek.lower() == "friday" or dayOfWeek.lower() == "fri" or dayOfWeek.lower() == "f":
        print ("Friday's words of encouragement:")
        print ("Failure is the condiment that gives success its flavor")
        print ("-Truman Capote")
        break
    elif dayOfWeek.lower() == "saturday" or dayOfWeek.lower() == "sat":
        print ("Saturday's words of encouragement:")
        print ("People rarel succeed unless they have fun in what they are doing")
        print ("-Dale Carnegie")
        break
    elif dayOfWeek.lower() == "sunday" or dayOfWeek.lower() == "sun":
        print ("Sunday's words of encouragement:")
        print ("Fall 7 times, stand up 8")
        print ("-Japanese Proverb")
        break
    else:
        print ("Sorry, I didn't understand you.")
