# Say a box of cookies can hold 24 cookies, and a container can hold 75
# boxes of cookies. Write a program that prompts the user to enter the total
# number of cookies, then outputs the number of boxes and the number of
# containers to ship the cookies. Note that each box must contain the
# specified number of cookies, and each container must contain the specified
# number of boxes. If the last box of cookies contains less than the number of
# specified cookies, you can discard it and output the number of leftover
# cookies. Similarly, if the last container contains less than the number of
# specified boxes, you can discard it and output the number of leftover boxes.

cookies=int(input("Enter the total number of cookies:"))
boxes=cookies//24
container=boxes//75
left_cookies=cookies-boxes*24
left_boxes=boxes-container*75

print(boxes)
print(container)
print(left_cookies)
print(left_boxes)
