
def show_menu():
    print("=================================================")
    print("       MY BAZAAR          ")
    print("=================================================")

    print("Hello! welcome to the gorcery store!\nFollowing are the products available in the shop:")

    print("CODE | DESCRIPTION |   CATEGORY   | COST (Rs)")
    print("0  | Tshirt      | Apparels     | 500")
    print("1  | Trousers    | Apparels     | 600")
    print("2  | Scarf       | Apparels     | 250")
    print("3  | Smartphone  | Electronics  | 20,000")
    print("4  | iPad        | Electronics  | 30,000")
    print("5  | Laptop      | Electronics  | 50,000")
    print("6  | Eggs        | Eatables     | 5")
    print("7  | Chocolate   | Eatables     | 10")
    print("8  | Juice       | Eatables     | 100")
    print("9  | Milk        | Eatables     | 45")

    while True:
      ans=input("Would you like to buy in bulk? (Would you like to buy in bulk? (y or Y / n or N):")
      if ans=='y' or ans=='Y' or ans=='n' or ans=='N':
        break

def get_regular_input():
  print('-------------------------------------------------\nENTER ITEMS YOU WISH TO BUY\n-------------------------------------------------')
  print('Enter the item codes (space-separated):')
  inpt=list(map(int,input().split()))
  for i in inpt:
      if i not in range(0,10):
       inpt.remove(i)
  l1=10*[0]
  for i in inpt:
    l1[i]+=1
  return l1

items={0:['Tshirt',500],1:['Trousers',600],2:['Scarf',250],3:['Smartphone',20000],4:['iPad',30000],5:['Laptop',50000],6:['Eggs',5],7:['Chocolate',10],8:['Juice',100],9:['Milk',45]}
def get_bulk_input():
   print('-------------------------------------------------\nENTER ITEMS AND QUANTITIES\n-------------------------------------------------')
   l1=10*[0]
   print('Enter code and quantity (leave blank to stop):')
   l2=list(map(int,input().split()))
   if l2[0] not in range(1,11):
     print("Invalid code. Try again.")
   elif l2[1]<0:
     print("Invalid quantity. Try again")
   else:
     print("You added",l2[1],items[l2[0]][0])
     l1[l2[0]]+=l2[1]
   while True:
     l2=list(map(int,input().split()))
     if l2==[]:
       print('Your order has been finalized.')
       break
     if l2[0] not in range(1,11):
       print("Invalid code. Try again.")
     elif l2[1]<0:
       print("Invalid quantity. Try again")
     else:
       print("You added",l2[1],items[l2[0]][0])
       l1[l2[0]]+=l2[1]
   return l1

def print_order_details(quantities):
  print('-------------------------------------------------\nORDER DETAILS\n-------------------------------------------------')
  c=1
  for i in range(0,10):
    if quantities[i]!=0:
      print('[',c,']',end=" ")
      print(items[i][0],'X',quantities[i],'=','Rs',items[i][1],'*',quantities[i],'=','Rs',quantities[i]*items[i][1])
      c+=1

def calculate_category_wise_cost(quantities):
  print('-------------------------------------------------\nCATEGORY-WISE COST\n-------------------------------------------------')
  apparel=0;elec=0;eatable=0
  for i in range(10):
    if i in [0,1,2]:
      apparel+=quantities[i]*items[i][1]
    elif i in [3,4,5]:
      elec+=quantities[i]*items[i][1]
    else:
      eatable+=quantities[i]*items[i][1]
  print('Apparels = Rs',apparel)
  print('Electronics = Rs',elec)
  print('Eatables = Rs',eatable)
  return (apparel,elec,eatable)

def get_discount(cost, discount_rate):
    '''
    Description: This is a helper function. DO NOT CHANGE THIS. 
    This function must be used whenever you are calculating discounts.
    
    Parameters: Takes 2 parameters:
    - cost: Integer
    - discount_rate: Float: 0 <= discount_rate <= 1

    Returns: The discount on the cost provided.
    '''
    return int(cost * discount_rate)

def calculate_discounted_prices(apparels_cost, electronics_cost, eatables_cost):
  print('-------------------------------------------------\nDISCOUNTS\n-------------------------------------------------')
  dis=0
  if apparels_cost>=2000:
    dis+=int(0.1*apparels_cost)
    print('[APPPAREL] Rs',apparels_cost,'-','Rs',int(0.1*apparels_cost),'=',end=" ")
    apparels_cost-=apparels_cost*0.1
    print(int(apparels_cost))
  if electronics_cost>=25000:
    dis+=int(0.1*electronics_cost)
    print('[ELECTRONICS] Rs',electronics_cost,'-','Rs',int(0.1*electronics_cost),'=',end=" ")
    electronics_cost-=electronics_cost*0.1
    print(int(electronics_cost))
  if eatables_cost>=500:
    dis+=int(0.1*eatables_cost)
    print('[EATABLES] Rs',eatables_cost,'-','Rs',int(0.1*eatables_cost),'=',end=" ")
    eatables_cost-=eatables_cost*0.1
    print(int(eatables_cost))
  print("TOTAL DISCOUNT = Rs",dis)
  print('TOTAL COST = Rs',int(apparels_cost+ electronics_cost+eatables_cost))
  return (int(apparels_cost), int(electronics_cost), int(eatables_cost))


def get_tax(cost, tax):
    '''
    Description: This is a helper function. DO NOT CHANGE THIS.
    This function must be used whenever you are calculating discounts.

    Parameters: Takes 2 parameters:
    - cost: Integer
    - tax: 	Float: 0 <= tax <= 1

    Returns: The tax on the cost provided.
    '''
    return int(cost * tax)


def calculate_tax(apparels_cost, electronics_cost, eatables_cost):
  print('-------------------------------------------------\nTAX\n-------------------------------------------------')
  discounted_cost=(apparels_cost, electronics_cost, eatables_cost)
  print('[APPPAREL] Rs',discounted_cost[0],'* 0.10 = Rs',int(discounted_cost[0]*0.1))
  print('[ELECTRONICS] Rs',discounted_cost[1],'* 0.15 = Rs',int(discounted_cost[1]*0.15))
  print('[APPPAREL] Rs',discounted_cost[2],'* 0.05 = Rs',int(discounted_cost[2]*0.05))
  tax=discounted_cost[0]*0.1+discounted_cost[1]*0.15+discounted_cost[2]*0.05
  tc=apparels_cost+ electronics_cost+ eatables_cost+tax
  return (int(tc),int(tax))

def apply_coupon_code(total_cost):
  print('-------------------------------------------------\nCOUPON CODE\n-------------------------------------------------')
  dis=0
  while True:
    inp=input('Enter coupon code (else leave blank):')
    if inp=="":
      print("No coupon code applied.")
      print()
      break
    elif inp == 'CHILL50' and total_cost>=50000:
      dis=10000
      print('[',inp,'] min(10000, Rs',total_cost,'* 0.50) = Rs',min(10000,int(total_cost* 0.50)))
      total_cost-=10000
      break
    elif inp == 'HELLE25' and total_cost>=25000:
      dis=5000
      print('[',inp,'] min(5000, Rs',total_cost,'* 0.25) = Rs',min(5000,int(total_cost* 0.25)))
      total_cost-=5000
      break
    else:
      print("Invalid coupon code. Try again.")
      print()
  print("TOTAL COUPON DISCOUNT = Rs",dis)
  print("TOTAL COST = Rs",total_cost)
  return (total_cost,dis)

def main():

    show_menu()
    get_regular_input()
    get_bulk_input()
    print_order_details()
    calculate_category_wise_cost()
    calculate_discounted_prices()
    get_tax()
    calculate_tax()
    apply_coupon_code()

if __name__ == '__main__':
    main()