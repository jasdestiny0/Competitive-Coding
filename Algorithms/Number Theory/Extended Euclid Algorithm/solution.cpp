#include<iostream>
using namespace std;


int gcd(int a,int b){
    if(b==0){
        return a;
    }
    return gcd(b,a%b);
}

int x,y,GCD;

void extendedEuclid(int a,int b){

    if(b==0){
        x = 1;
        y = 0;
        GCD = a;
        return;
    }

    extendedEuclid(b,a%b);
    int cX = y;
    int cY = x - (a/b)*y;

    x = cX;
    y = cY;

}

int main(){

    // 18X + 30Y = 6 // solution
    extendedEuclid(18,30);
    cout<<x<<" "<<y<<endl;

    return 0;
}