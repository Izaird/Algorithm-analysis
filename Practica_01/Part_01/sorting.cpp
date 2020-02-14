
#include "sorting.h"

IntList::IntList(){}

void IntList::setList(std::string file_name){
    std::fstream file(file_name);
    std::string str;
    //We need to clean the vector to erase previous data
    list.clear();
    //We read the document line per line and insert the data into a vector 
    while(std::getline(file,str)){
        if(str.size() > 0)
            list.push_back(std::stoi(str));
    }
}

void IntList::insertionSort(){
    int j= 0,aux = 0;
    for (int i = 1; i < list.size(); i++){
        j = i - 1;
        while(j>=0 && list[j]>list[j+1]){
            aux = list[j];
            list[j] = list[j+1];
            list[j+1] = aux;
            j = j - 1;
        }
    }
    
}

void IntList::bubbleSort(){
    int aux = 0;
    for (int i = 0; i < list.size()-1; i++){
        for (int j = 0; j < list.size()-i-1; j++){
            //checking if previous value is
            //grater than next one or not
            if(list[j]>list[j+1]){
                //temp will temporarly store
                //the value of vector[j]
                //then we will swap the values
                aux = list[j];
                list[j] = list[j+1];
                list[j+1] = aux;
            }
        }
        
    }
}
