import pikepdf

old_pdf = pikepdf.Pdf.open("p.pdf")

no_etra = pikepdf.Permissions(extract=False)

old_pdf.save("pro_new.pdf",encryption = pikepdf.Encryption(user="1234",owner="pratik",allow=no_etra))