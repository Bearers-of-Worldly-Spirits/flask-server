from mailjet_rest import Client
import os
import base64

def convertBase64():
    with open("f8843.pdf", "rb") as pdf_file:
        encoded_string = base64.b64encode(pdf_file.read())
        return encoded_string.decode("utf-8")
    
api_key = '7521d680ccec71a6fc6a09eb484d9d2b'
api_secret = '62b107e56512a1b9481bf410befe4724'
mailjet = Client(auth=(api_key, api_secret), version='v3.1')
data = {
  'Messages': [
				{
						"From": {
								"Email": "lightscmagic@gmail.com",
								"Name": "Melon"
						},
						"To": [
								{
										"Email": "mpwadekar@ucdavis.edu",
										"Name": "User"
								}
						],
						"Subject": "Hooray! Here is your form",
						"TextPart": "Thank you for using Melon.",
                        "HTMLPart": "<p><span style=\"font-family: Helvetica;\">Greetings from <span style=\"color: rgb(97, 189, 109);\"><strong>Melon!</strong></span></span></p><article><font face=\"Helvetica\">You are one in a <span style=\"color: rgb(97, 189, 109);\">Melon</span>. Your form(s) has been attached below.</font></article><article><br></article><article><font face=\"Helvetica\"><span style=\"color: rgb(97, 189, 109); font-size: 12px;\">P.S.: Don&apos;t forget to squeeze those melons.</span></font></article><footer><font face=\"Helvetica\">Stay Safe,</font></footer><footer><font face=\"Helvetica\"><strong><span style=\"color: rgb(97, 189, 109);\">Team Melon</span></strong></font></footer>",
						"Attachments": [
								{
                                    "ContentType": "application/pdf",
                                    "Filename": "8843.pdf",
                                    "Base64Content": convertBase64()
								}
						]
				}
		]
}
result = mailjet.send.create(data=data)
print(result.status_code)
print(result.json())