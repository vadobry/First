x=5
y=66
z=777
print ("A - '{}' B - '{}' C - '{}'".format(x,y,z) )

x=5
y=66
z=777
print ("C - '{2}' A - '{0}' B - '{1}' C again - '{2}'".format(x,y,z) )

x=5
y=66
z=777
print ("C - '{2:4}' A - '{0:4}' B - '{1:4}' C again - '{2:4}'".format(x,y,z) )

my_fruit = ["Apples","Oranges","Grapes","Pears"]
my_calories = [4,300,70,30]

for i in range(4):
    print(my_fruit[i],"are",my_calories[i],"calories.")

my_fruit = ["Apples","Oranges","Grapes","Pears"]
my_calories = [4,300,70,30]

for i in range(4):
    print("{:7} are {:3} calories.".format(my_fruit[i],my_calories[i]) )

my_fruit = ["Apples","Oranges","Grapes","Pears"]
my_calories = [4,300,70,30]

for i in range(4):
    print("{:>7} are {:<3} calories.".format(my_fruit[i],my_calories[i]) )

#
# for hours in range(1,13):
#     for minutes in range(0,60):
#         print( "Time {:02}:{:02}".format(hours, minutes) )

x=0.1
y=123.456789
print( "{:.1}  {:.1}".format(x,y) )
print( "{:.2}  {:.2}".format(x,y) )
print( "{:.3}  {:.3}".format(x,y) )
print( "{:.4}  {:.4}".format(x,y) )
print( "{:.5}  {:.5}".format(x,y) )
print( "{:.6}  {:.6}".format(x,y) )
print()
print( "{:.1f}  {:.1f}".format(x,y) )
print( "{:.2f}  {:.2f}".format(x,y) )
print( "{:.3f}  {:.3f}".format(x,y) )
print( "{:.4f}  {:.4f}".format(x,y) )
print( "{:.5f}  {:.5f}".format(x,y) )
print( "{:.6f}  {:.6f}".format(x,y) )

x=0.1
y=123.456789
print( "'{:10.1}'  '{:10.1}'".format(x,y) )
print( "'{:10.2}'  '{:10.2}'".format(x,y) )
print( "'{:10.3}'  '{:10.3}'".format(x,y) )
print( "'{:10.4}'  '{:10.4}'".format(x,y) )
print( "'{:10.5}'  '{:10.5}'".format(x,y) )
print( "'{:10.6}'  '{:10.6}'".format(x,y) )
print()
print( "'{:10.1f}'  '{:10.1f}'".format(x,y) )
print( "'{:10.2f}'  '{:10.2f}'".format(x,y) )
print( "'{:10.3f}'  '{:10.3f}'".format(x,y) )
print( "'{:10.4f}'  '{:10.4f}'".format(x,y) )
print( "'{:10.5f}'  '{:10.5f}'".format(x,y) )
print( "'{:10.6f}'  '{:10.6f}'".format(x,y) )


cost1 = 3.07
tax1 = cost1 * 0.06
total1 = cost1 + tax1

print("Cost:  ${0:5.2f}".format(cost1) )
print("Tax:    {0:5.2f}".format(tax1) )
print("------------")
print("Total: ${0:5.2f}".format(total1) )

cost1 = 3.07
tax1 = cost1 * 0.06
total1 = cost1 + tax1

print("Cost:  ${0:5.2f}".format(cost1) )
print("Tax:    {0:5.2f}".format(tax1) )
print("------------")
print("Total: ${0:5.2f}".format(total1) )

cost2 = 5.07
tax2 = cost2 * 0.06
total2 = cost2 + tax2

print()
print("Cost:  ${0:5.2f}".format(cost2) )
print("Tax:    {0:5.2f}".format(tax2) )
print("------------")
print("Total: ${0:5.2f}".format(total2) )


print()
grand_total = total1 + total2
print("Grand total: ${0:5.2f}".format(grand_total) )


cost1 = 3.07
tax1 = round(cost1 * 0.06,2)
total1 = cost1 + tax1

print("Cost:  ${0:5.2f}".format(cost1) )
print("Tax:    {0:5.2f}".format(tax1) )
print("------------")
print("Total: ${0:5.2f}".format(total1) )

cost2 = 5.07
tax2 = round(cost2 * 0.06,2)
total2 = cost2 + tax2

print()
print("Cost:  ${0:5.2f}".format(cost2) )
print("Tax:    {0:5.2f}".format(tax2) )
print("------------")
print("Total: ${0:5.2f}".format(total2) )


print()
grand_total = total1 + total2
print("Grand total: ${0:5.2f}".format(grand_total) )


x=1234.5678
print( round(x,2) )
print( round(x,1) )
print( round(x,0) )
print( round(x,-1) )
print( round(x,-2) )
score=41237
highscore=1023407

print("Очки: {:10,}".format(score) )
print("Рекорд: {:>10,}".format(highscore) )
