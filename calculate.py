
print ("Tip Calculator" )
bill = float(input(" toatal bill ? Euro"))
tip = int(input("I would like to give  10 percent "))
Guest = int(input("how many Guest to spilt the bill?")) 

tip_percent = tip / 100
tip_amount = bill * tip_percent
total_bill = bill + tip_amount
total_per_person = total_bill / Guest
final = round (total_per_person,2)

print (f"you should pay each Guest {final} Euro" )

