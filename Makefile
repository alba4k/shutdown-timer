build: ShutdownTimer.py unixlib.py winlib.py shutdown
	pyinstaller --onefile --noconsole ShutdownTimer.py

clean:
	rm -r build __pycache__ dist ShutdownTimer.spec