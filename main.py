# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line


scorer_Gullit = 'Ruud Gullit'
scorer_van_Basten = 'Marco van Basten' 

goal_0 = 32
goal_1 = 54

when_they_scored = [goal_0, goal_1]  

scorers = f"{scorer_Gullit } {str (goal_0)}, { scorer_van_Basten } {str (goal_1)}"
print (scorers)
 


x = scorer_Gullit.find ('Ruud Gullit')
print (x)
y = scorer_van_Basten .find ('Marco van Basten')
print (y)

report = f"{scorer_Gullit} scored in the {goal_0}nd minute \n{scorer_van_Basten} scored in the {goal_1}th minute"  

print (report)

player = 'Ronald Koeman'
first_name = player[:player.find (' ')]
print (first_name)

last_name_len = len(player [:player.find(' ')+1:])
print (last_name_len)

name_short = player[0] + '.' [:player.find(' ')+1:]  
print (name_short)
chant = 'Ronald' '!'  * len(first_name)

print(chant.lstrip()) 
good_chant =  chant !=  ' '
print (good_chant)



