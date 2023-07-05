//Author Skromnyy
//Github: https://github.com/hoangmanhkhiem
#include<bits/stdc++.h>
using namespace std;
#define f1(x,y,z)  (1-0.5*y-0.3*z)/(-6)
#define f2(x,y,z)  (2+0.4*x+0.2*z)/(-2)
#define f3(x,y,z)  (3+0.4*x-0.5*y)/6
int main()
{
 float x0=0, y0=0, z0=0, x1, y1, z1, e1, e2, e3, e, err_r;
 int it=1;
 cout<<"Nhap sai so: ";
 cin>>e;
 do
 {
  x1 = f1(x0,y0,z0);
  y1 = f2(x0,y0,z0);
  z1 = f3(x0,y0,z0);
  cout<< it<<"\t"<< x1<<"\t"<< y1<<"\t"<< z1<< endl;
  e1 = fabs(x0-x1);
  e2 = fabs(y0-y1);
  e3 = fabs(z0-z1);
  err_r=max(e1,max(e2,e3));
  it++;
  x0 = x1;
  y0 = y1;
  z0 = z1;
 }while (err_r>e);
 cout<< endl<<"Nghiem: x = "<< x1<<", y = "<< y1<<" and z = "<< z1;
 return 0;
}



