def warn_the_sheep(queue):
    if queue[-1] == "wolf":
            return "Pls go away and stop eating my sheep"
    else:
        reversed = queue[::-1]
        return "Oi! Sheep number " + str(reversed.index('wolf')) + "! You are about to be eaten by a wolf!"