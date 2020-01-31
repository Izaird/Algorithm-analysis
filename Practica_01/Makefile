CFLAGS = -O0 -g 
CC = g++
NumTest: main.o ordering.o
		$(CC) $(CFLAGS) -o main main.o ordering.o
main.o: main.cpp
		$(CC) $(CFLAGS) -c main.cpp
ordering.o: ordering.cpp
		$(CC) $(CFLAGS) -c ordering.cpp

clean:
	rm -f core *.o