#include "fibonacci.h"

int main(){
    // std::vector<std::string>cases{"best_case/b_", "worst_case/w_", "rand_case/rand_"};
    // IntList list;
    // std::ofstream data;
    // data.open("data");
    // for (int x=0; x < cases.size();x++){
    //     for (int i = 1; i < 101; i++){
    //         list.setList(cases[x]+ std::to_string(i) + "000");
    //         auto start = std::chrono::high_resolution_clock::now(); 
    //         list.insertionSort();
    //         auto stop = std::chrono::high_resolution_clock::now(); 
    //         auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(stop - start);
    //         data << duration.count() << ", ";
    //         std::cout << i << "\t" << x << std::endl;
    //     }
    //     data << "\n"; 
    // }

    // for (int x=0; x < cases.size();x++){
    //     for (int i = 1; i < 101; i++){
    //         list.setList(cases[x]+ std::to_string(i) + "000");
    //         auto start = std::chrono::high_resolution_clock::now(); 
    //         list.bubbleSort();
    //         auto stop = std::chrono::high_resolution_clock::now(); 
    //         auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(stop - start); 
    //         data << duration.count() << ", "; 
    //         std::cout << i << "\t" << x << std::endl;


    //     }
    //     data << "\n"; 
    // }

    // data.close();
    
    fib_01(5);
    return 0;
}