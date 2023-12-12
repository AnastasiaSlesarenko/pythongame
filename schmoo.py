import random
import math
import sys

def game_running():
    print(" " * 30 + "SCHMOO")
    print(" " * 15 + "CREATIVE COMPUTINGMORRISTOWN NEW JERSEY\n\n\n")

    print("THIS IS A NEW SCHMOO GAME. SCHOOMS")
    print("ARE IMAGINARY CREATURES WHO LOVE")
    print("BEING SPLATTED WITH JUICY MUD BALLS")
    print("YOU, BEING A SCHMOO LOVER, TRY TO")
    print("MAKE SCHMOOS HAPPY BY TOSSING MUD")
    print("BALLS AT THEM.  YOU HAVE A")
    print("MECHANICAL MUD SLINGER THAT WILL")
    print("SLING MUD TO A MAXIMUM DISTANCE")
    print("OF 46,500 INCHES. YOUR JOB IS TO")
    print("SET THE MUD SLINGER AT THE CORRECT")
    print("ELEVATION (0 TO 90) AND THE CORRECT")
    print("DIRECTIONAL ANGLE (0 TO 360) TO SPLAT THE")
    print("SCHMOO.  A HIT WITHIN 100 INCHES OF THE SCHMOO")
    print("WILL SPLATTER HIM.\n\n")

    K1 = 0

    Z = int(1 + random.random() * 4 - 1E-08)

    if Z == 1:
        P = -1
        Q = -1
    elif Z == 2:
        P = -1
        Q = 1
    elif Z == 3:
        P = 1
        Q = -1
    elif Z == 4:
        P = 1
        Q = 1

    X = (int(26000 * random.random() + 5000)) * P
    Y = (int(26000 * random.random() + 5000)) * Q

    print("COORDINATES OF THE SCHMOO ARE ({},{})".format(X, Y))

    while True:
        S = 0
        K1 += 1

        if K1 >= 2:
            R = int(7 * random.random() + 5)

        if K1 >= 2:

            while True:
                B = float(input("MUD SLINGER ELEVATION: "))
                C = float(input("DIRECTIONAL ANGLE OF MUD SLINGER: "))

                if B > 90:
                    print("THE ELEVATION MUST BE BETWEEN 1 AND 90")
                elif B == 90:
                    print("YOU DOPE!  YOU SPLATTED YOURSELF.")
                    sys.exit()
                elif B < 1:
                    print("THE ELEVATION MUST BE BETWEEN 1 AND 90.")
                elif C < 0:
                    print("DIRECTIONAL ANGLE MUST BE FROM 0 TO 360.")
                elif C > (360 - 1E-08):
                    print("DIRECTIONAL ANGLE MUST BE FROM 0 TO 360.")
                else:
                    break

            S += 1

            if K1 >= 2:
                R2 = int(abs(300 * random.random() * (11 - 2 * S)) + 90)
                J = math.pi / 180
                D = abs(int(93000 * math.sin(B * J) * math.cos(B * J)))
                X1 = int(D * math.cos(C * math.pi / 180))
                Y1 = int(D * math.sin(C * math.pi / 180))
                D1 = math.sqrt((X - X1) ** 2 + (Y - Y1) ** 2)

                if D1 <= 100:
                    print("*SCHMOO SPLATTED*", S, " MUD BALLS TOSSED.\n")
                    restart()
                else:
                    print("YOU MISSED THE SCHMOO AT (", X, ",", Y, ").")
                    print("YOUR MUD HIT (", X1, ",", Y1, ").")

                if S >= R:
                    print("THE SCHMOO HAS SPLATTED YOU!")
                    print("CLEAN UP AND GOODBYE!")
                    sys.exit()

def restart():
    print("I SEE ANOTHER SCHMOO.  TO SPLAT")
    print("HIM, TYPE MUD.  TO QUIT, TYPE QUIT.")
    while True:
        user_input = input("")
        if user_input == "MUD":
            game_running()
        elif user_input == "QUIT":
            sys.exit()

game_running()
