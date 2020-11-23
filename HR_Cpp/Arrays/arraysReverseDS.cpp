//
//  arraysReverseDS.cpp
//  
//
//  Created by Japneet Singh on 11/23/20.
//

#include <stdio.h>

vector<int> reverseArray(vector<int> a) {
    int first = 0;
    int second = a.size() - 1;
    while (first < second) {
        swap(a[first], a[second]);
        first++;
        second--;
    }
    return a;
}
