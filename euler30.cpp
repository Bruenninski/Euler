/*
This program solves the euler problem number 30, the sum of all numbers, that can be written an the fifth power of their digits.
the highest digit is 9 and 9^5 is 59049, due to this number we can assume that we have a upper value for our numbers from round about 360000.
In fact it is a little lower and we could save computational power if we would calculate permutations only once but 360000 numbers aren't that big so i took the bruteforce method
*/
#include<iostream>

int power5(int x){
    return x*x*x*x*x;
}

bool isDigitFifthPowerTheNumber(int number){
    int calcnumber = number;
    int sum = 0;
    while(calcnumber > 0){
        sum += power5(calcnumber%10);
        calcnumber/=10;
    }
    if (sum == number){
        return true;
    }
    else{
        return false;
    }
}

int main(){
    int sumOfNumbers = 0; //the sum of numbers where the 5th power of the digits is equal to their value

    for(int i=2; i<360000; i++){ //1 is in the definition of the task no sum so we start to count at number 2
        if(isDigitFifthPowerTheNumber(i)){
            sumOfNumbers += i;
        }
        if(i%1000==0){
            std::cout << i << "\n";
        }
    }

    std::cout << sumOfNumbers;
    return 0;
}
