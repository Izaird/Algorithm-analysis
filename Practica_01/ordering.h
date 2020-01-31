#include <iostream>
#include <fstream>
#include <vector>
#include <string>

class IntList
{
private:
    std::vector<int> list;
public:
    IntList(std::string file_name);
};
