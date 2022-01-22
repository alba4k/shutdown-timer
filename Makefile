buttons.o: shutdown/buttons.cpp
	g++ -c shutdown/buttons.cpp -o shutdown/buttons.o

buttons: shutdown/buttons.o
	g++ shutdown/buttons.o -o shutdown/buttons

clean:
	rm shutdown/*.o shutdown/buttons