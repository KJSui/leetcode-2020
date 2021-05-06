#include<iostream>
using namespace std;
class Shape{
public:
    void setWidth(int w){
        width = w;
    }
    void setLength(int l){
        length = l;
    }
protected:
    int width;
    int length;
};

class Rectangle: public Shape{
public:
    int getArea(){
        width * length;
    }
};

int main(void){
    Rectangle Rect;
    Rect.setLength(2);
    Rect.setWidth(3);
    count << "Total area:" << Rect.getArea() <<endl;
    return 0;
}