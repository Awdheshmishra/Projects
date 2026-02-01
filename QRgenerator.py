import qrcode


#taking upi id as a input
upi_id=input("enter your upi_id")

#upi://pay?pa=UPI_ID&pn=NAME&am=Amount&cii=CURRENCY&tn=MEASSAGE
#parameters
#pn=recipent ka naam

# defining the payment url based on the upi id and the payment app
phonepe_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_pay_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

# mc=merchent code

# create qr code for each payment app
phonepe_qr=qrcode.make(phonepe_url)

google_pay_qr=qrcode.make(google_pay_url)

paytm_qr=qrcode.make (paytm_url)
# save the qr code to image file optional hai bhaiya
phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
google_pay_qr.save('g_paye_qr.png')

# display thw qr codes for that  you may install pillow library

phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()

# LO BHAIYA DUBEY RUN KARA LO 