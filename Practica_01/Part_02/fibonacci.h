#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <chrono>

class IntList
{
private:
    std::vector<int> list;
public:
    IntList();
    void setList(std::string file_name);
    void insertionSort();
    void bubbleSort();
};


int fib_01(int n);
int fib_02(int x);
int fib_03(int x);