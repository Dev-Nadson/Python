def SecConv(Time):
    i = 0
    Seconds = 0
    List = list(Time)
    for h in List:
        if i in range(len(List)):
            h = int(h)
            if i == 0:
                Seconds += (h*60) * 60
            elif i == 1 and h > 0:
                Seconds += h*60
            elif i == 2 and h > 0:  
                Seconds += h 
        i += 1
    return Seconds

Time = input("Enter the hour: ").split(":")
All = SecConv(Time)
print(All)