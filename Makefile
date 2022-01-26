unix: shutdown/buttons.cpp
	g++ shutdown/buttons.cpp -o shutdown/buttons

windows: shutdown/buttons.cpp
	i686-w64-mingw32-g++ shutdown/buttons.cpp -o shutdown/buttons.exe

clean:
	rm shutdown/*.exe shutdown/buttons