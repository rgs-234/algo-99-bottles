def bottle_song(num_beers):

	if num_beers < 2:
		print("That's not enough beers.")
	elif num_beers > 2:
		for idx in range(num_beers, 2, -1):
			print(f"{idx} bottles of beer on the wall, {idx} bottles of beer.")
			print(f"Take one down and pass it around, {idx - 1} bottles of beer on the wall.")

	print("""2 bottles of beer on the wall, 2 bottles of beer.
Take one down and pass it around, 1 bottle of beer on the wall.
1 bottle of beer on the wall, 1 bottle of beer.
Take one down and pass it around, no more bottles of beer on the wall.
No more bottles of beer on the wall, no more bottles of beer.
Go to the store and buy some more, 99 bottles of beer on the wall.""")
	
bottle_song(99)