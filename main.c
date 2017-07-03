//
//  main.c
//  fish distr
//
//  Created by Jack Parsons on 30/06/2017.
//  Copyright © 2017 Jack Parsons. All rights reserved.
//

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define TRIALS 100000000
#define POINTS 1000000
#define MAXRANGE 26
#define MEAN 10
#define STORE 1000

int cmp(const void *x, const void *y){
    int *a = (int *) x;
    int *b = (int *) y;
    if (*a > *b) {return 1;}
    else if (*a < *b){ return -1;}
    else {return 0;}
}

int binsearch(int n, int* l, int size){
    int upper = size;
    int lower = 0;
    int i = size>>1;
    while ((upper-lower) > 1){
        i = (upper+lower)>>1;
        if (l[i] > n){
            upper = i;
        }
        else if (l[i] < n){
            lower = i;
        }
        else{
            return i;
        }
    }
    return lower;
}


int main(int argc, const char * argv[]) {
    
    clock_t start = clock();
    int points[POINTS];
    int totals[STORE];
    int n, mx=0;
    const int squaresize = ((2<<MAXRANGE)*MEAN)/POINTS;
    const int upperrand = (2<<MAXRANGE)-squaresize;
    int lower, upper;
    for (int i=0; i < POINTS; i++){
        points[i] = arc4random_uniform(2<<MAXRANGE);
    }
    for (int i=0; i < 1000; i++){
        totals[i] = 0;
    }
    qsort(points, POINTS, sizeof(float), *cmp);
    for(int trial=0; trial<TRIALS; trial++){
        lower = arc4random_uniform(upperrand);
        upper = lower + squaresize;
        n = binsearch(upper, points, POINTS) - binsearch(lower, points, POINTS);
        totals[n]++;
    }
    for(int i=0; i < STORE; i++){
        if (totals[i]){
            mx = i;
        }
    }
    for (int i=0; i < mx; i++){
        printf("%i\n", totals[i]);
    }
    clock_t end = clock();
    printf("%f seconds exectution", (double)0.000001*(end-start));
    
    return 0;
}
