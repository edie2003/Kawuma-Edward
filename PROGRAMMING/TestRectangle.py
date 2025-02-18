from Rect import Rectangle
def main():
    rect1 = Rectangle(5, 10)
    print('area of a rectangle with width', rect1.width, 'and length', rect1.length, 'is', rect1.getArea())
    print('perimeter is ', rect1.getPerimeter())
     
    rect2 = Rectangle(2, 4)
    print('area of a rectangle with width', rect2.width, 'and length', rect2.length, 'is', rect2.getArea())
    print('perimeter is ', rect1.getPerimeter())
    #modify radius
    rect2.width = 20
    rect2.length =30
    print('\t', 'area of a modified rectangle with width', rect2.width, 'and length', rect2.length,'is', rect2.getArea(), '\n')
    print('\t', 'and perimeter is ', rect2.getPerimeter())

    
    #modify dimensions  using the method
    rect3 = Rectangle()
    rect3.setsetWidth = (4)
    rect3.setsetLength = 5
    print(rect3.getArea())
# call the main method
main()