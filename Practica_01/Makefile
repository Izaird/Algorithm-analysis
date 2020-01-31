CFLAGS = -O0 -g 
CC = g++
NumTest: main.o sorting.o
		$(CC) $(CFLAGS) -o main main.o sorting.o
main.o: main.cpp
		$(CC) $(CFLAGS) -c main.cpp
sorting.o: sorting.cpp
		$(CC) $(CFLAGS) -c sorting.cpp

clean:
	rm -f core *.o