buttons: shutdown/buttons.o
	g++ shutdown/buttons.o -o shutdown/buttons

buttons.o: shutdown/buttons.cpp
	g++ -c shutdown/buttons.cpp -o shutdown/buttons.o

clean:
	rm shutdown/*.o shutdown/buttons