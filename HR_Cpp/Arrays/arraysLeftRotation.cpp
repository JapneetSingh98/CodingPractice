//
//  arraysLeftRotation.cpp
//  
//
//  Created by Japneet Singh on 11/25/20.
//

#include <stdio.h>

vector<int> rotateLeft(int d, vector<int> arr) {
    vector<int> soln;
    
    for (int i = d; i < arr.size(); i++) {
        soln.push_back(arr[i]);
    }
    for (int i = 0; i < d; i++) {
        soln.push_back(arr[i]);
    }
    
    return soln;
}
