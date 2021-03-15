# Write code usingfind() and stringslicing(see section6.10) to extract
# the number at the end of the line below.Convert the extracted value
# to a floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475";
pos = text.find('0')
text = text[pos:]
print(float(text))