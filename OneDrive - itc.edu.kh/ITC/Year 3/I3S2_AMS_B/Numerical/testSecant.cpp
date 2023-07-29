#include <iostream>
#include <math.h>
#include<iomanip>
#include<chrono>
using namespace std::chrono; 
using namespace std;

static double function(double x);

int main()
{

  double x0;
  double x1;
  double x_new;
  double precision;

  cout << "function(x)  "<<endl;
  cout << "Enter initial guess x0: ";
  cin >> x0;

  cout << "\nEnter initial guess x1: ";
  cin >> x1;

  cout << "\nEnter precision of method: ";
  cin >> precision;
  

int iter=0;
cout<<setw(3)<<"\niterations"<<setw(8)<<"x0"<<setw(16)<<"x1"<<setw(25)<<"function(x_new)"<<endl;

auto start = high_resolution_clock::now(); 
 
 do{
            x_new=x1-(function(x1)*(x1-x0))/(function(x1)-function(x0));
            iter++;

            cout<<setprecision(10)<<setw(3)<<iter<<setw(15)<<x0<<setw(15)<<x1<<setw(20)<<function(x_new)<<endl;

            x0=x1;
            x1=x_new;
    }while(fabs(function(x_new-x1))<precision);//Terminating case
    
  auto stop = high_resolution_clock::now(); 
  auto duration = duration_cast<microseconds>(stop - start); 


    cout<<"\nRoot = "<<x_new;
    cout<<"\nf(x)="<<function(x_new)<<endl;
    cout << duration.count()<<" microseconds"<< endl; 

    return 0;
}

static double function(double x)
{
  return (exp(x)-2*x-2) ;
}