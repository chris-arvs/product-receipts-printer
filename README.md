# product-recites-printer

In this project the user has to give a file with receipts in format like ReceiptFileBig.
After that the user has two choices for printing:

choice 2 is to give a product and it will print how many of this products were sold by AFM in ascending order.Each line has AFM and SUM_OF_PRICING for this product.

choice 3 is to give an AFM and it will print the products which were sold to this AFM in ascending alphabetical order.Each line has PRODUCT_NAME and PRICE.

def print_Menu():
	print('1:read new input file.......................').
	print('2:print statistics for a specific product...').
	print('3:print statistics for a specific AFM.......').
	print('4:Exit the program..........................').
	
NOTES: AFM must be a 10 digit int and the format of receipts must be in format like ReceiptFileBig.
There are a lot of comments in script computeSales.py
