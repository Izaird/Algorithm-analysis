#include "sorting.h"

int main(){
    std::string path = "rand_numbers/rand_";
    IntList list;
    for (int i = 1; i < 101; i++){
        list.setList(path+ std::to_string(i) + "000");
        auto start = std::chrono::high_resolution_clock::now(); 
        list.insertionSort();
        auto stop = std::chrono::high_resolution_clock::now(); 
        auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(stop - start); 
        std::cout << duration.count() << " ms" << std::endl; 

    }

    for (int i = 1; i < 101; i++){
        list.setList(path+ std::to_string(i) + "000");
        auto start = std::chrono::high_resolution_clock::now(); 
        list.bubbleSort();
        auto stop = std::chrono::high_resolution_clock::now(); 
        auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(stop - start); 
        std::cout << duration.count() << " ms" << std::endl; 
    }
    
    
    return 0;
}