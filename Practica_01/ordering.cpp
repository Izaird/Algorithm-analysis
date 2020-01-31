
#include "ordering.h"



IntList::IntList(std::string file_name){
    std::fstream file("rand_numbers/" + file_name);
    std::string str;

    //We read the document line per line and insert the data into a vector 
    while(std::getline(file,str)){
        if(str.size() > 0)
            list.push_back(std::stoi(str));
    }
}
