def frac1( numerator, denominator):  
    for divisor in range(2,100):
        if (numerator % divisor == 0 and denominator % divisor == 0):
            return(frac1(numerator / divisor, denominator / divisor))
    return('{} / {}'.format(numerator, denominator))
def frac2( numerator, denominator):  
    for divisor in range(2,100):
        if (numerator % divisor == 0 and denominator % divisor == 0):
            return(frac2(numerator / divisor, denominator / divisor))
    return('{} : {}'.format(numerator, denominator))
while(1):
    print("1. Liqidity ratio\n")
    print("2. Solvency ratio\n")
    print("3. Activity ratio\n")
    print("4. Profitability ratio\n")
    print("press 1 to 4\n")
    print("to exit press 0\n")
    input1=int(input())
    if input1==0:
        exit()
    while(input1):
        if input1==1:
            print("press 1 or 2\n")
            print("1. Current ratio\n")
            print("2. Liquid ratio or Quick ratio\n")
            input2=int(input())
            if input2==1:
                print("enter current asset\n")
                current_asset=float(input())
                print("enter current liability\n")
                current_liability=float(input())
                ans=frac2(current_asset,current_liability)
                print('Current ratio '+str(ans))
                break
            elif input2==2:
                print("enter liquid asset or quick asset\n")
                liquid_asset_or_quick_asset=float(input())
                print("enter current liability\n")
                current_liability=float(input())
                ans=frac2(liquid_asset_or_quick_asset,current_liability)
                print('Liquid ratio or Quick ratio '+str(ans))
                break
            else:
                break


                
        elif input1==2:
            print("press 1 to 4 \n")
            print("1. Dept to quity ratio\n")
            print("2. Total asset to debt ratio\n")
            print("3. Proproetary ratio\n")
            print("4. Interest coverage ratio\n")
            input2=int(input())
            if input2==1:
                print("enter Dept\n")
                Dept=float(input())
                print("enter Share holders fund or Equity\n")
                Share_holders_fund_or_Equity=float(input())
                ans=frac2(Dept,Share_holders_fund_or_Equity)
                print('Dept to quity ratio '+str(ans))
                break
            elif input2==2:
                print("enter Total asset\n")
                Total_asset=float(input())
                print("enter Dept(long term)\n")
                Dept_long=float(input())
                ans=frac2(Total_asset,Dept_long)
                print('Total asset to debt ratio '+str(ans))
                break
            elif input2==3:
                print("enter Equity\n")
                Dept=float(input())
                print("enter Total asset\n")
                Share_holders_fund_or_Equity=float(input())
                ans=frac1(Dept,Share_holders_fund_or_Equity)
                print('Proproetary ratio '+str(ans))
                break
            elif input2==4:
                print("enter Profit before interest and tax\n")
                Profit_before_interest_and_tax=float(input())
                print("enter interest on longterm debt\n")
                Share_holders_fund_or_Equity=float(input())
                ans=Profit_before_interest_and_tax/Share_holders_fund_or_Equity
                print('Interest coverage ratio '+str(ans)+' '+'rate')
                break
            else:
                break


        elif input1==3:
            print("press 1 to 4 \n")
            print("1. Inventory turnover ratio\n")
            print("2. Trade receivables Turnover ratio\n")
            print("3. Trade payables turnover ratio\n")
            print("4. Working capital turnover ratio\n")
            input2=int(input())
            if input2==1:
                print("enter Cost of revenue from operation(COGS)\n")
                COGS=float(input())
                print("enter Average inventory\n")
                Average_inventory=float(input())
                ans=COGS/Average_inventory
                print(str(ans)+' '+'rate')
                break
            elif input2==2:
                print("enter Credit revenue from operation\n")
                Credit_revenue_from_operation=float(input())
                print("enter Average trade receivable\n")
                Average_trade_receivable=float(input())
                ans=Credit_revenue_from_operation/Average_trade_receivable
                print(str(ans)+' '+'rate')
                break
            elif input2==3:
                print("enter Net credit purchases\n")
                Net_credit_purchases=float(input())
                print("enter Average trade payables\n")
                Average_trade_payables=float(input())
                ans=Net_credit_purchases/Average_trade_payables
                print(str(ans)+' '+'rate')
                break
            elif input2==4:
                print("enter Revenue from operation\n")
                Revenue_from_operation=float(input())
                print("enter Working capital\n")
                Working_capital=float(input())
                ans=Revenue_from_operation/Working_capital
                print(str(ans)+' '+'rate')
                break
            else:
                break



        elif input1==4:
            print("press 1 to 5 \n")
            print("1. Gross profit ratio\n")
            print("2. Operating ratio\n")
            print("3. Operating profit ratio\n")
            print("4. Net profit ratio\n")
            print("5. Return on invesment or Return on capital employed\n")
            input2=int(input())
            if input2==1:
                print("enter Gross profit\n")
                Gross_profit=float(input())
                print("enter Revenue from operation\n")
                Revenue_from_operation=float(input())
                ans=(Gross_profit/Revenue_from_operation)*100
                print(str(ans)+' '+'%')
                break
            elif input2==2:
                print("enter cost of revenue from operation")
                cost1=float(input())
                print("enter operating expence\n")
                cost2=float(input())
                cost_f=cost1+cost2
                print("enter Revenue from operation\n")
                Revenue_from_operation=float(input())
                ans=(cost_f/Revenue_from_operation)*100
                print(str(ans)+' '+'%')
                break
            elif input2==3:
                print("enter Operating profit\n")
                Operating_profit=float(input())
                print("enter Revenue from operation\n")
                Revenue_from_operation=float(input())
                ans=(Operating_profit/Revenue_from_operation)*100
                print(str(ans)+' '+'%')
                break
            elif input2==4:
                print("enter Net profit after tax\n")
                Net_profit_after_tax=float(input())
                print("enter Revenue from operation\n")
                Revenue_from_operation=float(input())
                ans=(Net_profit_after_tax/Revenue_from_operation)*100
                print(str(ans)+' '+'%')
                break
            elif input2==5:
                print("enter Profit before interest tax & Dividend\n")
                Net_profit_after_tax=float(input())
                print("enter Capital employed\n")
                Capital_employed=float(input())
                ans=(Net_profit_after_tax/Capital_employed)*100
                print(str(ans)+' '+'%')
                break
            else:
                break

            
