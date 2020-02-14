CFLAGS = -O0 -g 
CC = g++
NumTest: main.o fibonacci.o
		$(CC) $(CFLAGS) -o main main.o fibonacci.o
main.o: main.cpp
		$(CC) $(CFLAGS) -c main.cpp
fibonacci.o: fibonacci.cpp
		$(CC) $(CFLAGS) -c fibonacci.cpp

clean:
	rm -f core *.o