print ( "-----------------Height Converstion-----------------" )
print ( "----------Centimetres to Feet and inches----------" )

#Getting Height in cm from User
cm   = int ( input ( "Enter your Height in Centimetres : " ) )

#Calculation:
feet  = ( cm/30.48 )
inch = ( feet - int(feet) ) * 12

#Printing the User's Height in Feet and Inches
print ( "Your height in feet and inches : {0}'{1} ".format
      ( int(feet) ,round (inch) ) ) 
